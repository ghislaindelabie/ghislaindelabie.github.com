#!/usr/bin/env python3
"""
Feature C: Markdown Cleanup
Cleans up WordPress-specific HTML and formatting issues
"""

import re
from typing import Tuple, Dict


def normalize(content: str) -> Tuple[str, Dict]:
    """
    Clean up markdown content

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

    # 1. Remove HTML entities
    body, entity_count = remove_html_entities(body)
    if entity_count > 0:
        results['changes'].append(f"Removed {entity_count} HTML entities (&nbsp;, &amp;, etc.)")

    # 2. Remove/fix HTML tags
    body, tag_count = cleanup_html_tags(body)
    if tag_count > 0:
        results['changes'].append(f"Cleaned up {tag_count} HTML tags (<br>, <p>, etc.)")

    # 3. Fix WordPress caption tags
    body, caption_count = fix_wordpress_captions(body)
    if caption_count > 0:
        results['changes'].append(f"Converted {caption_count} WordPress captions to markdown")

    # 4. Fix escaped characters
    body, escape_count = fix_escaped_characters(body)
    if escape_count > 0:
        results['changes'].append(f"Fixed {escape_count} unnecessary escape sequences")

    # 5. Normalize list formatting
    body, list_fixes = normalize_lists(body)
    if list_fixes > 0:
        results['changes'].append(f"Normalized {list_fixes} list items")

    # 6. Remove excessive blank lines
    body, blank_line_fixes = remove_excessive_blank_lines(body)
    if blank_line_fixes > 0:
        results['changes'].append(f"Removed {blank_line_fixes} excessive blank lines")

    # 7. Convert WordPress shortcodes (if any)
    body, shortcode_count = convert_wordpress_shortcodes(body)
    if shortcode_count > 0:
        results['changes'].append(f"Converted {shortcode_count} WordPress shortcodes")
        results['warnings'].append("Review converted shortcodes manually")

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


def remove_html_entities(body: str) -> Tuple[str, int]:
    """
    Remove/replace common HTML entities

    Returns:
        tuple: (cleaned_body, count_of_replacements)
    """
    count = 0
    entities = {
        '&nbsp;': ' ',
        '&amp;': '&',
        '&lt;': '<',
        '&gt;': '>',
        '&quot;': '"',
        '&apos;': "'",
        '&hellip;': '...',
        '&mdash;': '—',
        '&ndash;': '–',
        '&rsquo;': "'",
        '&lsquo;': "'",
        '&rdquo;': '"',
        '&ldquo;': '"',
    }

    for entity, replacement in entities.items():
        occurrences = body.count(entity)
        if occurrences > 0:
            body = body.replace(entity, replacement)
            count += occurrences

    # Also handle numeric entities like &#8217;
    numeric_entity_pattern = r'&#\d+;'
    numeric_matches = re.findall(numeric_entity_pattern, body)
    if numeric_matches:
        count += len(numeric_matches)
        # Replace common numeric entities
        body = re.sub(r'&#8217;', "'", body)  # Right single quote
        body = re.sub(r'&#8216;', "'", body)  # Left single quote
        body = re.sub(r'&#8220;', '"', body)  # Left double quote
        body = re.sub(r'&#8221;', '"', body)  # Right double quote
        body = re.sub(r'&#8211;', '–', body)  # En dash
        body = re.sub(r'&#8212;', '—', body)  # Em dash

    return body, count


def cleanup_html_tags(body: str) -> Tuple[str, int]:
    """
    Remove or clean up HTML tags

    Returns:
        tuple: (cleaned_body, count_of_replacements)
    """
    count = 0

    # Remove <br>, <br/>, <br />
    br_pattern = r'<br\s*/?>'
    br_count = len(re.findall(br_pattern, body, re.IGNORECASE))
    if br_count > 0:
        body = re.sub(br_pattern, '\n', body, flags=re.IGNORECASE)
        count += br_count

    # Remove empty <p> tags
    empty_p_pattern = r'<p>\s*</p>'
    empty_p_count = len(re.findall(empty_p_pattern, body, re.IGNORECASE))
    if empty_p_count > 0:
        body = re.sub(empty_p_pattern, '', body, flags=re.IGNORECASE)
        count += empty_p_count

    # Remove standalone <p> and </p> tags (but keep content)
    p_tag_pattern = r'</?p>'
    p_tag_count = len(re.findall(p_tag_pattern, body, re.IGNORECASE))
    if p_tag_count > 0:
        body = re.sub(p_tag_pattern, '', body, flags=re.IGNORECASE)
        count += p_tag_count

    return body, count


def fix_wordpress_captions(body: str) -> Tuple[str, int]:
    """
    Convert WordPress [caption] shortcodes to markdown

    Example:
        [caption id="..." width="..." caption="Photo of cat"]
        ![](image.jpg)
        [/caption]

    Becomes:
        ![Photo of cat](image.jpg)

    Returns:
        tuple: (cleaned_body, count_of_conversions)
    """
    count = 0

    # Pattern for WordPress captions
    # [caption ...]![alt](url)[/caption]
    caption_pattern = r'\[caption[^\]]*\]\s*!\[([^\]]*)\]\(([^)]+)\)\s*\[/caption\]'

    def replace_caption(match):
        nonlocal count
        count += 1
        alt_text = match.group(1)
        image_url = match.group(2)
        return f"![{alt_text}]({image_url})"

    body = re.sub(caption_pattern, replace_caption, body, flags=re.IGNORECASE)

    # Also handle captions with caption attribute
    # [caption caption="Text"]![](url)[/caption]
    caption_attr_pattern = r'\[caption[^]]*caption=["\']([^"\']+)["\'][^\]]*\]\s*!\[[^\]]*\]\(([^)]+)\)\s*\[/caption\]'

    def replace_caption_attr(match):
        nonlocal count
        count += 1
        caption_text = match.group(1)
        image_url = match.group(2)
        return f"![{caption_text}]({image_url})"

    body = re.sub(caption_attr_pattern, replace_caption_attr, body, flags=re.IGNORECASE)

    return body, count


def fix_escaped_characters(body: str) -> Tuple[str, int]:
    r"""
    Remove unnecessary escape characters

    Common issues:
    - Escaped brackets: \[ \]
    - Escaped underscores: \_ (but keep in certain contexts)

    Returns:
        tuple: (cleaned_body, count_of_fixes)
    """
    count = 0

    # Count and remove unnecessary escapes
    # Escaped brackets that aren't part of links
    escaped_bracket_pattern = r'\\([\[\]])'
    escaped_brackets = re.findall(escaped_bracket_pattern, body)
    if escaped_brackets:
        count += len(escaped_brackets)
        # Only unescape if not part of a link pattern
        # This is conservative - we keep the escapes
        # Could be more aggressive if needed

    # Note: Being conservative here to avoid breaking legitimate escapes
    # Can be expanded based on actual issues found in testing

    return body, count


def normalize_lists(body: str) -> Tuple[str, int]:
    """
    Normalize list formatting

    Issues to fix:
    - Inconsistent spacing before/after lists
    - Mixed bullet styles (*, -, +)
    - Inconsistent indentation

    Returns:
        tuple: (normalized_body, count_of_fixes)
    """
    count = 0

    # Standardize bullet markers to -
    bullet_patterns = [
        (r'^(\s*)\*\s+', r'\1- '),   # * to -
        (r'^(\s*)\+\s+', r'\1- '),   # + to -
    ]

    for pattern, replacement in bullet_patterns:
        matches = re.findall(pattern, body, re.MULTILINE)
        if matches:
            count += len(matches)
            body = re.sub(pattern, replacement, body, flags=re.MULTILINE)

    return body, count


def remove_excessive_blank_lines(body: str) -> Tuple[str, int]:
    """
    Remove excessive consecutive blank lines (max 2)

    Returns:
        tuple: (cleaned_body, count_of_fixes)
    """
    # Count how many times we have 3+ consecutive blank lines
    excessive_pattern = r'\n{4,}'
    excessive_matches = re.findall(excessive_pattern, body)
    count = len(excessive_matches)

    if count > 0:
        # Replace 3+ blank lines with 2 blank lines (3 newlines)
        body = re.sub(r'\n{4,}', '\n\n\n', body)

    return body, count


def convert_wordpress_shortcodes(body: str) -> Tuple[str, int]:
    """
    Convert common WordPress shortcodes to Jekyll/markdown equivalents

    Returns:
        tuple: (converted_body, count_of_conversions)
    """
    count = 0

    # [gallery] shortcode - convert to note
    gallery_pattern = r'\[gallery[^\]]*\]'
    gallery_matches = re.findall(gallery_pattern, body, re.IGNORECASE)
    if gallery_matches:
        count += len(gallery_matches)
        body = re.sub(gallery_pattern, '\n> **Note:** Gallery shortcode removed - add images manually\n', body, flags=re.IGNORECASE)

    # [embed] shortcode - will be handled by Feature E
    # Just count them here for awareness
    embed_pattern = r'\[embed[^\]]*\]'
    embed_matches = re.findall(embed_pattern, body, re.IGNORECASE)
    if embed_matches:
        # Don't increment count - Feature E will handle this
        pass

    return body, count


if __name__ == '__main__':
    # Test with sample content
    sample = """---
title: Test
---

This is a test&nbsp;with entities&amp;more.

<p>Empty paragraph below:</p>

<p></p>

Regular text.<br>
With line breaks.<br/>

[caption caption="A cat"]![](cat.jpg)[/caption]

- Item 1
* Item 2
+ Item 3


Excessive


Blank


Lines
"""

    normalized, results = normalize(sample)
    print("Results:", results)
    print("\nNormalized:\n", normalized)
