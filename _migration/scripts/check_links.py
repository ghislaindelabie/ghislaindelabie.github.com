#!/usr/bin/env python3
"""
Post-normalization Link Checker with Wayback Machine Integration
Checks external links and replaces broken ones with Wayback Machine archives
"""

import os
import sys
import re
import requests
import argparse
from pathlib import Path
from datetime import datetime
from urllib.parse import urlparse


def check_and_fix_links(filepath, config):
    """
    Check and fix links in a normalized markdown file

    Args:
        filepath: Path to markdown file
        config: Configuration dict with options

    Returns:
        dict: Results with status and changes
    """
    results = {
        'file': str(filepath),
        'total_links': 0,
        'broken_links': 0,
        'replaced_links': 0,
        'unreplaceable_links': [],
        'replacements': [],
        'status': 'pending'
    }

    # Read file
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
    except Exception as e:
        results['status'] = 'error'
        results['error'] = str(e)
        return results

    original_content = content

    # Extract frontmatter and body
    frontmatter, body = extract_frontmatter(content)

    # Extract all external links
    links = extract_external_links(body)
    results['total_links'] = len(links)

    if not links:
        results['status'] = 'success'
        return results

    print(f"  Found {len(links)} external link(s)")

    # Check each link
    for i, link_data in enumerate(links, 1):
        url = link_data['url']
        full_markdown = link_data['full']
        text = link_data['text']

        print(f"  [{i}/{len(links)}] Checking: {url[:60]}...")

        # Check if link is accessible
        is_broken = not check_link(url, timeout=config.get('timeout', 5))

        if is_broken:
            results['broken_links'] += 1
            print(f"    ✗ Broken link detected")

            # Try to find Wayback Machine archive
            if config.get('use_wayback', True):
                print(f"    → Querying Wayback Machine...")
                archive_url = query_wayback_machine(url)

                if archive_url:
                    # Replace link with archive
                    new_markdown = f"[{text}]({archive_url})"
                    body = body.replace(full_markdown, new_markdown)

                    results['replaced_links'] += 1
                    results['replacements'].append({
                        'original': url,
                        'archive': archive_url,
                        'text': text
                    })
                    print(f"    ✓ Replaced with: {archive_url[:60]}...")
                else:
                    results['unreplaceable_links'].append(url)
                    print(f"    ✗ No Wayback archive found")
        else:
            print(f"    ✓ Link OK")

    # Reconstruct content if changes were made
    if results['replaced_links'] > 0:
        normalized_content = frontmatter + body if frontmatter else body

        # Write updated file
        if not config.get('dry_run', False):
            try:
                with open(filepath, 'w', encoding='utf-8') as f:
                    f.write(normalized_content)
                results['status'] = 'updated'
                print(f"  ✓ File updated with {results['replaced_links']} replacement(s)")
            except Exception as e:
                results['status'] = 'error'
                results['error'] = str(e)
                return results
        else:
            results['status'] = 'dry_run'
            print(f"  (Dry run - would replace {results['replaced_links']} link(s))")
    else:
        results['status'] = 'no_changes'

    return results


def extract_frontmatter(content):
    """Extract frontmatter and body from markdown"""
    pattern = r'^(---\s*\n.*?\n---\s*\n\n)(.*)$'
    match = re.match(pattern, content, re.DOTALL)

    if match:
        return match.group(1), match.group(2)
    return '', content


def extract_external_links(body):
    """Extract all external HTTP(S) links from markdown"""
    links = []
    pattern = r'\[([^\]]+)\]\((https?://[^)]+)\)'

    for match in re.finditer(pattern, body):
        url = match.group(2)

        # Skip common stable domains
        parsed = urlparse(url)
        skip_domains = ['youtube.com', 'youtu.be', 'vimeo.com', 'twitter.com', 'github.com', 'archive.org']

        if not any(domain in parsed.netloc for domain in skip_domains):
            links.append({
                'full': match.group(0),
                'text': match.group(1),
                'url': url
            })

    return links


def check_link(url, timeout=5):
    """Check if a link is accessible"""
    try:
        response = requests.head(url, timeout=timeout, allow_redirects=True)
        return response.status_code < 400
    except:
        # Fallback to GET if HEAD fails
        try:
            response = requests.get(url, timeout=timeout, allow_redirects=True, stream=True)
            return response.status_code < 400
        except:
            return False


def query_wayback_machine(url):
    """Query Wayback Machine for archived version of URL"""
    try:
        api_url = f"http://archive.org/wayback/available?url={url}"
        response = requests.get(api_url, timeout=10)

        if response.status_code == 200:
            data = response.json()
            if data.get('archived_snapshots', {}).get('closest', {}).get('available'):
                return data['archived_snapshots']['closest']['url']

        return None
    except:
        return None


def main():
    parser = argparse.ArgumentParser(
        description='Check and fix broken links using Wayback Machine',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Check links in a single file
  python check_links.py _posts/2020-06-30-article.md

  # Check all files in directory
  python check_links.py _posts/

  # Dry run (show what would be changed)
  python check_links.py _posts/ --dry-run

  # Skip Wayback Machine lookup
  python check_links.py _posts/ --no-wayback
        """
    )
    parser.add_argument('input', help='Input markdown file or directory')
    parser.add_argument('--dry-run', action='store_true', help='Show changes without writing files')
    parser.add_argument('--no-wayback', action='store_true', help='Skip Wayback Machine lookup')
    parser.add_argument('--timeout', type=int, default=5, help='Request timeout in seconds (default: 5)')

    args = parser.parse_args()

    config = {
        'dry_run': args.dry_run,
        'use_wayback': not args.no_wayback,
        'timeout': args.timeout
    }

    # Process file(s)
    input_path = Path(args.input)

    if not input_path.exists():
        print(f"❌ Error: {input_path} does not exist")
        sys.exit(1)

    print(f"\n{'='*60}")
    print(f"Link Checker with Wayback Machine Integration")
    print(f"{'='*60}\n")

    results_summary = []

    if input_path.is_file():
        print(f"📄 Processing: {input_path.name}\n")
        results = check_and_fix_links(input_path, config)
        results_summary.append(results)

    elif input_path.is_dir():
        md_files = list(input_path.glob('*.md'))
        if not md_files:
            print(f"❌ No markdown files found in {input_path}")
            sys.exit(1)

        print(f"📁 Processing directory: {input_path}")
        print(f"   Found {len(md_files)} markdown file(s)\n")

        for md_file in md_files:
            print(f"📄 Processing: {md_file.name}")
            results = check_and_fix_links(md_file, config)
            results_summary.append(results)
            print()

    # Summary
    print(f"\n{'='*60}")
    print("Summary")
    print(f"{'='*60}\n")

    total_links = sum(r['total_links'] for r in results_summary)
    total_broken = sum(r['broken_links'] for r in results_summary)
    total_replaced = sum(r['replaced_links'] for r in results_summary)

    print(f"Total links checked: {total_links}")
    print(f"Broken links found: {total_broken}")
    print(f"Links replaced with Wayback: {total_replaced}")

    # Show unreplaceable links
    unreplaceable = []
    for r in results_summary:
        unreplaceable.extend(r['unreplaceable_links'])

    if unreplaceable:
        print(f"\n⚠️  {len(unreplaceable)} broken link(s) without Wayback archives:")
        for url in unreplaceable[:10]:  # Show first 10
            print(f"  - {url}")
        if len(unreplaceable) > 10:
            print(f"  ... and {len(unreplaceable) - 10} more")

    # Save detailed log
    if results_summary:
        log_path = Path('_migration/logs/link_check_log.md')
        log_path.parent.mkdir(parents=True, exist_ok=True)

        with open(log_path, 'w') as f:
            f.write(f"# Link Check Log - {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")
            f.write(f"## Summary\n\n")
            f.write(f"- Total links: {total_links}\n")
            f.write(f"- Broken: {total_broken}\n")
            f.write(f"- Replaced: {total_replaced}\n\n")

            f.write(f"## Replacements\n\n")
            for r in results_summary:
                if r['replacements']:
                    f.write(f"### {Path(r['file']).name}\n\n")
                    for rep in r['replacements']:
                        f.write(f"- **Original:** {rep['original']}\n")
                        f.write(f"  **Archive:** {rep['archive']}\n")
                        f.write(f"  **Text:** {rep['text']}\n\n")

            f.write(f"## Unreplaceable Links\n\n")
            for url in unreplaceable:
                f.write(f"- {url}\n")

        print(f"\n📝 Detailed log saved to: {log_path}")


if __name__ == '__main__':
    main()
