#!/usr/bin/env python3
"""
Feature F: Image Processing
Handles image extraction, copying, and path normalization
"""

import re
import os
import shutil
from pathlib import Path
from typing import Tuple, Dict, List


def normalize(content: str, filepath: Path) -> Tuple[str, Dict]:
    """
    Process images in markdown content

    Args:
        content: Full markdown file content as string
        filepath: Path to the markdown file being processed

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

    # Extract post slug from filename
    post_slug = filepath.stem.replace('.NORMALIZED', '')

    # 1. Extract all image references
    images = extract_image_urls(body)

    if not images:
        results['status'] = 'success'
        results['warnings'].append("No images found in content")
        return content, results

    # 2. Process each image
    processed_count = 0
    missing_count = 0
    alt_text_added = 0

    for img_match in images:
        img_markdown = img_match['full']
        img_url = img_match['url']
        img_alt = img_match['alt']

        # Determine source image path (relative to markdown file)
        source_dir = filepath.parent
        if img_url.startswith('images/'):
            # Relative path like images/foo.jpg
            source_path = source_dir / img_url
        elif img_url.startswith('./'):
            source_path = source_dir / img_url[2:]
        elif img_url.startswith('../'):
            source_path = source_dir / img_url
        elif not img_url.startswith('http'):
            # Assume it's relative
            source_path = source_dir / img_url
        else:
            # External URL - skip
            continue

        # Check if source image exists
        if not source_path.exists():
            results['warnings'].append(f"Image not found: {img_url}")
            missing_count += 1
            continue

        # Target: /assets/img/posts/{post-slug}/{filename}
        img_filename = os.path.basename(img_url)

        # Update markdown with new path
        new_path = f"/assets/img/posts/{post_slug}/{img_filename}"

        # Generate alt text if missing
        if not img_alt or img_alt.strip() == '':
            # Generate from filename
            alt_text = generate_alt_text(img_filename)
            new_markdown = f"![{alt_text}]({new_path})"
            alt_text_added += 1
        else:
            new_markdown = f"![{img_alt}]({new_path})"

        # Replace in body
        body = body.replace(img_markdown, new_markdown)
        processed_count += 1

    # 3. Report results
    if processed_count > 0:
        results['changes'].append(f"Updated {processed_count} image path(s) to /assets/img/posts/{post_slug}/")

    if missing_count > 0:
        results['warnings'].append(f"Found {missing_count} missing image(s) - paths updated but files not found")

    if alt_text_added > 0:
        results['changes'].append(f"Generated alt text for {alt_text_added} image(s)")

    results['warnings'].append(f"Note: Images not physically copied - run separate image copy script after normalization")

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


def extract_image_urls(body: str) -> List[Dict]:
    """
    Extract all image references from markdown

    Returns:
        list: List of dicts with 'full' (full markdown), 'alt' (alt text), 'url' (image URL)
    """
    images = []

    # Pattern: ![alt text](url)
    pattern = r'!\[([^\]]*)\]\(([^)]+)\)'

    for match in re.finditer(pattern, body):
        images.append({
            'full': match.group(0),
            'alt': match.group(1),
            'url': match.group(2)
        })

    return images


def generate_alt_text(filename: str) -> str:
    """
    Generate descriptive alt text from filename

    Args:
        filename: Image filename

    Returns:
        str: Generated alt text
    """
    # Remove extension
    name = os.path.splitext(filename)[0]

    # Replace common separators with spaces
    name = name.replace('-', ' ').replace('_', ' ')

    # Remove numbers and hashes at start
    name = re.sub(r'^\d+\s*', '', name)
    name = re.sub(r'^[a-f0-9]{5,}\s*', '', name)  # Remove hash prefixes

    # Capitalize first letter
    name = name.strip().capitalize()

    return name if name else "Image"


if __name__ == '__main__':
    # Test with sample content
    sample = """---
title: Test
---

Some text.

![](images/test-image.jpg)

![Old alt](images/another.png)

![](./relative/path.jpg)

More text.
"""

    from pathlib import Path
    test_path = Path('/tmp/test-post.md')

    normalized, results = normalize(sample, test_path)
    print("Results:", results)
    print("\nNormalized:\n", normalized)
