#!/usr/bin/env python3
"""
Feature E: Embed Detection & Conversion
Detects and converts embedded content (YouTube, Twitter, etc.) to Jekyll format
"""

import re
from typing import Tuple, Dict, List


def normalize(content: str) -> Tuple[str, Dict]:
    """
    Detect and convert embedded content in markdown

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

    # 1. Convert YouTube embeds (iframes)
    body, youtube_count, youtube_ids = convert_youtube_embeds(body)
    if youtube_count > 0:
        results['changes'].append(f"Converted {youtube_count} YouTube embed(s)")
        for vid_id in youtube_ids:
            results['warnings'].append(f"YouTube video {vid_id} - verify video is still available")

    # 1b. Convert plain YouTube URLs to markdown links
    body, youtube_url_count = convert_youtube_urls(body)
    if youtube_url_count > 0:
        results['changes'].append(f"Converted {youtube_url_count} plain YouTube URL(s) to links")

    # 2. Convert Vimeo embeds
    body, vimeo_count, vimeo_ids = convert_vimeo_embeds(body)
    if vimeo_count > 0:
        results['changes'].append(f"Converted {vimeo_count} Vimeo embed(s)")

    # 3. Convert Twitter embeds (blockquotes)
    body, twitter_count = convert_twitter_embeds(body)
    if twitter_count > 0:
        results['changes'].append(f"Converted {twitter_count} Twitter embed(s)")
        results['warnings'].append("Twitter embeds converted to blockquotes - API access may be required for live embedding")

    # 3b. Convert plain Twitter URLs to markdown links
    body, twitter_url_count = convert_twitter_urls(body)
    if twitter_url_count > 0:
        results['changes'].append(f"Converted {twitter_url_count} plain Twitter URL(s) to links")

    # 4. Detect and flag unknown embeds
    unknown_embeds = detect_unknown_embeds(body)
    if unknown_embeds:
        results['warnings'].append(f"Found {len(unknown_embeds)} unknown embed(s) - manual review needed")
        for embed in unknown_embeds[:3]:  # Show first 3
            results['warnings'].append(f"  Unknown embed: {embed[:50]}...")

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


def convert_youtube_embeds(body: str) -> Tuple[str, int, List[str]]:
    """
    Convert YouTube iframes to markdown links with preview note

    Returns:
        tuple: (converted_body, count_of_conversions, list_of_video_ids)
    """
    count = 0
    video_ids = []

    # Pattern for YouTube iframe
    # <iframe src="https://www.youtube.com/embed/VIDEO_ID" ...></iframe>
    youtube_pattern = r'<iframe[^>]*src=["\']https?://(?:www\.)?youtube\.com/embed/([^"\'?]+)[^>]*>.*?</iframe>'

    def replace_youtube(match):
        nonlocal count
        video_id = match.group(1)
        count += 1
        video_ids.append(video_id)

        # Convert to markdown link with note
        youtube_url = f"https://www.youtube.com/watch?v={video_id}"
        return f"\n> [YouTube Video: {youtube_url}]({youtube_url})\n"

    body = re.sub(youtube_pattern, replace_youtube, body, flags=re.IGNORECASE | re.DOTALL)

    # Also handle youtube-nocookie.com embeds
    youtube_nocookie_pattern = r'<iframe[^>]*src=["\']https?://(?:www\.)?youtube-nocookie\.com/embed/([^"\'?]+)[^>]*>.*?</iframe>'

    def replace_youtube_nocookie(match):
        nonlocal count
        video_id = match.group(1)
        count += 1
        video_ids.append(video_id)

        youtube_url = f"https://www.youtube.com/watch?v={video_id}"
        return f"\n> [YouTube Video: {youtube_url}]({youtube_url})\n"

    body = re.sub(youtube_nocookie_pattern, replace_youtube_nocookie, body, flags=re.IGNORECASE | re.DOTALL)

    return body, count, video_ids


def convert_youtube_urls(body: str) -> Tuple[str, int]:
    """
    Convert plain YouTube URLs to markdown links
    Handles: https://youtu.be/VIDEO_ID and https://www.youtube.com/watch?v=VIDEO_ID
    Also handles escaped characters (\_) from WordPress exports

    Returns:
        tuple: (converted_body, count_of_conversions)
    """
    count = 0

    # Pattern for plain YouTube URLs on their own line
    # Matches: https://youtu.be/VIDEO_ID or https://www.youtube.com/watch?v=VIDEO_ID
    # Allows for escaped underscores and hyphens (\\_ or \\-) from WordPress
    youtube_url_patterns = [
        r'(?:^|\n)(https?://(?:www\.)?youtu\.be/([-a-zA-Z0-9_\\]+))(?:\n|$)',
        r'(?:^|\n)(https?://(?:www\.)?youtube\.com/watch\?v=([-a-zA-Z0-9_\\]+))(?:\n|$)'
    ]

    for pattern in youtube_url_patterns:
        def replace_url(match):
            nonlocal count
            url = match.group(1)
            video_id = match.group(2)
            # Remove escape characters from URL for display
            clean_url = url.replace('\\', '')
            count += 1
            return f"\n[YouTube: {clean_url}]({clean_url})\n"

        body = re.sub(pattern, replace_url, body, flags=re.MULTILINE)

    return body, count


def convert_vimeo_embeds(body: str) -> Tuple[str, int, List[str]]:
    """
    Convert Vimeo iframes to markdown links

    Returns:
        tuple: (converted_body, count_of_conversions, list_of_video_ids)
    """
    count = 0
    video_ids = []

    # Pattern for Vimeo iframe
    # <iframe src="https://player.vimeo.com/video/VIDEO_ID" ...></iframe>
    vimeo_pattern = r'<iframe[^>]*src=["\']https?://player\.vimeo\.com/video/([^"\'?]+)[^>]*>.*?</iframe>'

    def replace_vimeo(match):
        nonlocal count
        video_id = match.group(1)
        count += 1
        video_ids.append(video_id)

        vimeo_url = f"https://vimeo.com/{video_id}"
        return f"\n> [Vimeo Video: {vimeo_url}]({vimeo_url})\n"

    body = re.sub(vimeo_pattern, replace_vimeo, body, flags=re.IGNORECASE | re.DOTALL)

    return body, count, video_ids


def convert_twitter_embeds(body: str) -> Tuple[str, int]:
    """
    Convert Twitter blockquotes to simplified markdown

    Returns:
        tuple: (converted_body, count_of_conversions)
    """
    count = 0

    # Pattern for Twitter blockquote
    # <blockquote class="twitter-tweet">...</blockquote>
    twitter_pattern = r'<blockquote[^>]*class=["\']twitter-tweet[^>]*>(.*?)</blockquote>'

    def replace_twitter(match):
        nonlocal count
        tweet_content = match.group(1)

        # Extract tweet URL if present
        url_match = re.search(r'href=["\']([^"\']*twitter\.com[^"\']*)["\']', tweet_content)
        if url_match:
            tweet_url = url_match.group(1)
            count += 1
            return f"\n> [Tweet: {tweet_url}]({tweet_url})\n"
        else:
            # No URL found, keep content as blockquote
            # Strip HTML tags
            clean_content = re.sub(r'<[^>]+>', '', tweet_content)
            clean_content = clean_content.strip()
            count += 1
            return f"\n> {clean_content}\n"

    body = re.sub(twitter_pattern, replace_twitter, body, flags=re.IGNORECASE | re.DOTALL)

    return body, count


def convert_twitter_urls(body: str) -> Tuple[str, int]:
    """
    Convert plain Twitter URLs to markdown links
    Handles: https://twitter.com/user/status/TWEET_ID

    Returns:
        tuple: (converted_body, count_of_conversions)
    """
    count = 0

    # Pattern for plain Twitter/X URLs on their own line
    # Matches: https://twitter.com/USER/status/TWEET_ID or https://x.com/USER/status/TWEET_ID
    twitter_url_pattern = r'(?:^|\n)(https?://(?:twitter\.com|x\.com)/[^/]+/status/\d+)(?:\n|$)'

    def replace_url(match):
        nonlocal count
        url = match.group(1)
        count += 1
        return f"\n[Tweet: {url}]({url})\n"

    body = re.sub(twitter_url_pattern, replace_url, body, flags=re.MULTILINE)

    return body, count


def detect_unknown_embeds(body: str) -> List[str]:
    """
    Detect iframes and other embed patterns that weren't converted

    Returns:
        list: List of unknown embed snippets
    """
    unknown = []

    # Find remaining iframes
    iframe_pattern = r'<iframe[^>]*>.*?</iframe>'
    iframes = re.findall(iframe_pattern, body, re.IGNORECASE | re.DOTALL)
    unknown.extend(iframes)

    # Find WordPress [embed] shortcodes
    embed_shortcode_pattern = r'\[embed[^\]]*\].*?\[/embed\]'
    embeds = re.findall(embed_shortcode_pattern, body, re.IGNORECASE | re.DOTALL)
    unknown.extend(embeds)

    # Find standalone <embed> or <object> tags
    object_pattern = r'<(?:embed|object)[^>]*>.*?</(?:embed|object)>'
    objects = re.findall(object_pattern, body, re.IGNORECASE | re.DOTALL)
    unknown.extend(objects)

    return unknown


if __name__ == '__main__':
    # Test with sample content
    sample = """---
title: Test
---

Some text.

<iframe width="560" height="315" src="https://www.youtube.com/embed/dQw4w9WgXcQ" frameborder="0"></iframe>

More text.

<blockquote class="twitter-tweet">
  <p>This is a tweet</p>
  <a href="https://twitter.com/user/status/123456">View tweet</a>
</blockquote>

<iframe src="https://player.vimeo.com/video/123456" width="640" height="360"></iframe>

<iframe src="https://unknown-embed.com/video/123"></iframe>
"""

    normalized, results = normalize(sample)
    print("Results:", results)
    print("\nNormalized:\n", normalized)
