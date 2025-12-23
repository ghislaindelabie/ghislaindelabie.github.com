#!/usr/bin/env python3
"""
Feature A: Frontmatter Standardization
Ensures all posts have complete, standardized frontmatter for Jekyll
"""

import re
from datetime import datetime
import yaml


def normalize(content):
    """
    Normalize frontmatter in markdown content

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

    # Parse frontmatter and body
    frontmatter, body = parse_frontmatter(content)

    if not frontmatter:
        results['issues'].append("No frontmatter found")
        results['status'] = 'error'
        return content, results

    # Standardize frontmatter fields
    normalized_fm = {}

    # 1. Layout (always 'post')
    normalized_fm['layout'] = 'post'
    if frontmatter.get('layout') != 'post':
        results['changes'].append(f"Set layout: post (was: {frontmatter.get('layout', 'missing')})")

    # 2. Title (required)
    if 'title' in frontmatter:
        normalized_fm['title'] = frontmatter['title']
    else:
        results['issues'].append("Missing title field")
        normalized_fm['title'] = "MISSING TITLE"

    # 3. Date (required, normalize format)
    if 'date' in frontmatter:
        normalized_date = normalize_date(frontmatter['date'])
        if normalized_date:
            normalized_fm['date'] = normalized_date
            if str(frontmatter['date']) != normalized_date:
                results['changes'].append(f"Normalized date format: {normalized_date}")
        else:
            results['issues'].append(f"Invalid date format: {frontmatter['date']}")
            normalized_fm['date'] = frontmatter['date']
    else:
        results['issues'].append("Missing date field")
        normalized_fm['date'] = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        results['changes'].append("Added current date (missing)")

    # 4. Description (generate if missing)
    if 'description' in frontmatter and frontmatter['description']:
        normalized_fm['description'] = frontmatter['description']
    else:
        # Generate from first paragraph
        description = generate_description(body)
        normalized_fm['description'] = description
        results['changes'].append(f"Generated description: {description[:50]}...")

    # 5. Tags (preserve and add 'transport' tag)
    if 'tags' in frontmatter:
        # Ensure it's a list
        tags = frontmatter['tags']
        if isinstance(tags, str):
            tags = [tag.strip() for tag in tags.split(',')]
        # Add 'transport' tag if not already present
        if 'transport' not in tags:
            tags.append('transport')
            results['changes'].append("Added 'transport' tag")
        normalized_fm['tags'] = tags if tags else ['transport']
    else:
        normalized_fm['tags'] = ['transport']
        results['changes'].append("Set tags: ['transport']")

    # 6. Categories (set to 'post' for WordPress blog migration)
    normalized_fm['categories'] = ['post']
    if 'categories' in frontmatter and frontmatter['categories'] != ['post']:
        old_cats = frontmatter['categories']
        if isinstance(old_cats, str):
            old_cats = old_cats
        elif isinstance(old_cats, list):
            old_cats = ', '.join(old_cats)
        results['changes'].append(f"Set categories to ['post'] (was: {old_cats})")

    # 7. Language (hardcoded to French for WordPress import)
    normalized_fm['lang'] = 'fr'
    if 'lang' not in frontmatter:
        results['changes'].append("Added lang: fr (WordPress import)")

    # 8. Original URL (preserve if exists, indicates WordPress source)
    if 'original_url' in frontmatter:
        normalized_fm['original_url'] = frontmatter['original_url']

    # 9. Preserve other WordPress fields that might be useful
    if 'coverImage' in frontmatter:
        normalized_fm['coverImage'] = frontmatter['coverImage']

    if 'featuredImage' in frontmatter:
        normalized_fm['featuredImage'] = frontmatter['featuredImage']

    # 10. Translation status (default false)
    normalized_fm['translated'] = frontmatter.get('translated', False)

    # Reconstruct content with normalized frontmatter
    normalized_content = serialize_frontmatter(normalized_fm) + "\n\n" + body

    results['status'] = 'success' if not results['issues'] else 'warning'
    return normalized_content, results


def parse_frontmatter(content):
    """
    Parse YAML frontmatter from markdown content

    Returns:
        tuple: (frontmatter_dict, body_content)
    """
    # Match frontmatter pattern: ---\n...\n---
    pattern = r'^---\s*\n(.*?)\n---\s*\n(.*)$'
    match = re.match(pattern, content, re.DOTALL)

    if not match:
        return None, content

    try:
        frontmatter = yaml.safe_load(match.group(1))
        body = match.group(2)
        return frontmatter, body
    except yaml.YAMLError as e:
        print(f"YAML parsing error: {e}")
        return None, content


def normalize_date(date_value):
    """
    Normalize date to YYYY-MM-DD HH:MM:SS format

    Args:
        date_value: Date in various formats (string, date object)

    Returns:
        str: Normalized date string or None if invalid
    """
    if isinstance(date_value, datetime):
        return date_value.strftime('%Y-%m-%d %H:%M:%S')

    if isinstance(date_value, str):
        # Try various date formats
        formats = [
            '%Y-%m-%d %H:%M:%S',
            '%Y-%m-%d',
            '%Y/%m/%d',
            '%d/%m/%Y',
            '%Y-%m-%dT%H:%M:%S',
            '%Y-%m-%dT%H:%M:%SZ',
        ]

        for fmt in formats:
            try:
                dt = datetime.strptime(date_value, fmt)
                return dt.strftime('%Y-%m-%d %H:%M:%S')
            except ValueError:
                continue

    # Try parsing datetime object
    try:
        if hasattr(date_value, 'strftime'):
            return date_value.strftime('%Y-%m-%d %H:%M:%S')
    except:
        pass

    return None


def generate_description(body):
    """
    Generate description from first paragraph of body content

    Args:
        body: Markdown body content

    Returns:
        str: Generated description (max 160 chars)
    """
    # Remove markdown formatting
    text = body.strip()

    # Remove headers
    text = re.sub(r'^#{1,6}\s+.*$', '', text, flags=re.MULTILINE)

    # Remove images
    text = re.sub(r'!\[.*?\]\(.*?\)', '', text)

    # Remove links but keep text
    text = re.sub(r'\[([^\]]+)\]\([^\)]+\)', r'\1', text)

    # Remove HTML tags
    text = re.sub(r'<[^>]+>', '', text)

    # Remove extra whitespace
    text = re.sub(r'\s+', ' ', text).strip()

    # Get first sentence or 160 chars
    first_para = text.split('\n\n')[0] if '\n\n' in text else text

    # Truncate to 160 chars (SEO best practice)
    if len(first_para) > 160:
        description = first_para[:157] + '...'
    else:
        description = first_para

    return description if description else "Article de blog"


def serialize_frontmatter(frontmatter):
    """
    Serialize frontmatter dict back to YAML

    Args:
        frontmatter: Dictionary of frontmatter fields

    Returns:
        str: YAML frontmatter with --- delimiters
    """
    yaml_str = yaml.dump(
        frontmatter,
        default_flow_style=False,
        allow_unicode=True,
        sort_keys=False
    )

    return f"---\n{yaml_str}---"


if __name__ == '__main__':
    # Test with sample content
    sample = """---
title: Test Post
date: 2020-01-15
categories: test
---

This is a test post content."""

    normalized, results = normalize(sample)
    print("Results:", results)
    print("\nNormalized:\n", normalized)
