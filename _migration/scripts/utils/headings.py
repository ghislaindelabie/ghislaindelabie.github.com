#!/usr/bin/env python3
"""
Feature B: Heading Normalization
Ensures proper heading hierarchy and formatting in markdown
"""

import re
from typing import Tuple, Dict, List


def normalize(content: str) -> Tuple[str, Dict]:
    """
    Normalize headings in markdown content

    Args:
        content: Full markdown file content as string

    Returns:
        tuple: (normalized_content, results_dict)
    """
    results = {
        'status': 'pending',
        'changes': [],
        'issues': [],
        'warnings': []
    }

    # Separate frontmatter from body
    frontmatter, body = extract_frontmatter(content)

    if not body:
        results['issues'].append("No body content found")
        results['status'] = 'error'
        return content, results

    original_body = body

    # 1. Convert Setext headings to ATX style
    body, setext_count = convert_setext_to_atx(body)
    if setext_count > 0:
        results['changes'].append(f"Converted {setext_count} Setext headings to ATX style")

    # 2. Remove H1 headings from body (title should be in frontmatter)
    body, h1_count = remove_h1_from_body(body)
    if h1_count > 0:
        results['warnings'].append(f"Removed {h1_count} H1 heading(s) from body (title is in frontmatter)")

    # 3. Fix heading hierarchy (no skipped levels)
    body, hierarchy_fixes = fix_heading_hierarchy(body)
    if hierarchy_fixes:
        results['changes'].append(f"Fixed heading hierarchy: {hierarchy_fixes} adjustments")

    # 4. Ensure proper spacing around headings
    body, spacing_fixes = normalize_heading_spacing(body)
    if spacing_fixes > 0:
        results['changes'].append(f"Normalized spacing around {spacing_fixes} headings")

    # 5. Check for duplicate headings (warning only)
    duplicate_headings = find_duplicate_headings(body)
    if duplicate_headings:
        results['warnings'].append(f"Found {len(duplicate_headings)} duplicate heading(s): {', '.join(duplicate_headings[:3])}")

    # Reconstruct content
    normalized_content = frontmatter + body if frontmatter else body

    results['status'] = 'success' if not results['issues'] else 'warning'
    return normalized_content, results


def extract_frontmatter(content: str) -> Tuple[str, str]:
    """
    Extract frontmatter and body from markdown content

    Returns:
        tuple: (frontmatter_with_delimiters, body_content)
    """
    pattern = r'^(---\s*\n.*?\n---\s*\n\n)(.*)$'
    match = re.match(pattern, content, re.DOTALL)

    if match:
        return match.group(1), match.group(2)
    return '', content


def convert_setext_to_atx(body: str) -> Tuple[str, int]:
    """
    Convert Setext-style headings to ATX style

    Setext examples:
        Heading 1
        =========

        Heading 2
        ---------

    ATX equivalents:
        # Heading 1
        ## Heading 2

    Returns:
        tuple: (converted_body, count_of_conversions)
    """
    count = 0

    # H1: Line followed by ===
    def replace_h1(match):
        nonlocal count
        count += 1
        return f"# {match.group(1).strip()}"

    body = re.sub(r'^(.+)\n=+\s*$', replace_h1, body, flags=re.MULTILINE)

    # H2: Line followed by ---
    def replace_h2(match):
        nonlocal count
        count += 1
        return f"## {match.group(1).strip()}"

    body = re.sub(r'^(.+)\n-+\s*$', replace_h2, body, flags=re.MULTILINE)

    return body, count


def remove_h1_from_body(body: str) -> Tuple[str, int]:
    """
    Remove H1 headings from body (title should be in frontmatter only)

    Returns:
        tuple: (body_without_h1, count_removed)
    """
    # Find all H1 headings
    h1_pattern = r'^# [^\n]+\n?'
    h1_matches = re.findall(h1_pattern, body, flags=re.MULTILINE)
    count = len(h1_matches)

    if count > 0:
        # Remove H1 headings
        body = re.sub(h1_pattern, '', body, flags=re.MULTILINE)
        # Clean up any resulting multiple blank lines
        body = re.sub(r'\n{3,}', '\n\n', body)

    return body, count


def fix_heading_hierarchy(body: str) -> Tuple[str, int]:
    """
    Fix heading hierarchy to ensure no skipped levels
    (e.g., H2 → H4 should become H2 → H3)

    Returns:
        tuple: (fixed_body, count_of_fixes)
    """
    # Extract all headings with their levels
    heading_pattern = r'^(#{2,6})\s+(.+)$'
    headings = []

    for match in re.finditer(heading_pattern, body, re.MULTILINE):
        level = len(match.group(1))
        text = match.group(2)
        start, end = match.span()
        headings.append({
            'level': level,
            'text': text,
            'start': start,
            'end': end,
            'original': match.group(0)
        })

    if not headings:
        return body, 0

    # Determine correct levels
    fixes = 0
    current_level = 2  # Start at H2 (H1 is title)
    replacements = []

    for heading in headings:
        expected_level = current_level
        actual_level = heading['level']

        # If heading jumps more than 1 level, adjust it
        if actual_level > current_level + 1:
            expected_level = current_level + 1
            new_heading = f"{'#' * expected_level} {heading['text']}"
            replacements.append((heading['original'], new_heading))
            fixes += 1
            current_level = expected_level
        elif actual_level <= current_level:
            current_level = actual_level
        else:
            current_level = actual_level

    # Apply replacements
    for old, new in replacements:
        body = body.replace(old, new, 1)

    return body, fixes


def normalize_heading_spacing(body: str) -> Tuple[str, int]:
    """
    Ensure headings have blank line before and after
    (except at start of document or before/after other headings)

    Returns:
        tuple: (normalized_body, count_of_fixes)
    """
    lines = body.split('\n')
    normalized_lines = []
    fixes = 0

    for i, line in enumerate(lines):
        is_heading = re.match(r'^#{2,6}\s+', line)
        prev_line = lines[i-1] if i > 0 else ''
        next_line = lines[i+1] if i < len(lines)-1 else ''

        is_prev_heading = re.match(r'^#{2,6}\s+', prev_line)
        is_next_heading = re.match(r'^#{2,6}\s+', next_line)

        if is_heading:
            # Add blank line before heading (if not at start and prev isn't blank or heading)
            if i > 0 and prev_line.strip() and not is_prev_heading:
                if not normalized_lines or normalized_lines[-1].strip():
                    normalized_lines.append('')
                    fixes += 1

            normalized_lines.append(line)

            # Add blank line after heading (if next isn't blank or heading)
            if i < len(lines)-1 and next_line.strip() and not is_next_heading:
                # Check if next iteration would add a line
                if i+1 < len(lines) and lines[i+1].strip():
                    normalized_lines.append('')
                    fixes += 1
        else:
            normalized_lines.append(line)

    return '\n'.join(normalized_lines), fixes


def find_duplicate_headings(body: str) -> List[str]:
    """
    Find duplicate heading texts (warning only, don't modify)

    Returns:
        list: Duplicate heading texts
    """
    heading_pattern = r'^#{2,6}\s+(.+)$'
    headings = re.findall(heading_pattern, body, re.MULTILINE)

    # Find duplicates
    seen = set()
    duplicates = []

    for heading in headings:
        heading_lower = heading.strip().lower()
        if heading_lower in seen and heading.strip() not in duplicates:
            duplicates.append(heading.strip())
        seen.add(heading_lower)

    return duplicates


if __name__ == '__main__':
    # Test with sample content
    sample = """---
title: Test
---

# This is H1 (should be removed)

## First Section

Content here.
## Second Section
More content.

#### Skipped Level (should be H3)

Final content.

## Duplicate Section

## Duplicate Section
"""

    normalized, results = normalize(sample)
    print("Results:", results)
    print("\nNormalized:\n", normalized)
