#!/usr/bin/env python3
"""
Smart Image Copy Script
Copies only the images that each post actually references
"""

import os
import re
import shutil
import argparse
from pathlib import Path


def copy_post_images(post_path, image_source_dir, dry_run=False):
    """
    Copy images referenced in a post to the correct location

    Args:
        post_path: Path to the markdown post file
        image_source_dir: Directory containing source images
        dry_run: If True, show what would be done without copying

    Returns:
        dict: Results with counts and actions
    """
    results = {
        'post': post_path.name,
        'images_found': 0,
        'images_copied': 0,
        'images_missing': 0,
        'missing_files': [],
        'copied_files': []
    }

    # Read post content
    try:
        with open(post_path, 'r', encoding='utf-8') as f:
            content = f.read()
    except Exception as e:
        results['error'] = str(e)
        return results

    # Extract post slug from filename
    post_slug = post_path.stem

    # Find all image references in the post
    # Pattern: ![alt](/assets/img/posts/{post-slug}/filename.ext)
    pattern = rf'!\[([^\]]*)\]\(/assets/img/posts/{re.escape(post_slug)}/([^)]+)\)'
    matches = re.findall(pattern, content)

    results['images_found'] = len(matches)

    if not matches:
        return results

    # Create target directory
    target_dir = post_path.parent.parent / 'assets' / 'img' / 'posts' / post_slug

    if not dry_run:
        target_dir.mkdir(parents=True, exist_ok=True)

    # Copy each referenced image
    for alt_text, filename in matches:
        # Find source image in the source directory
        # The filename might have a hash prefix like "12abc-image.jpg"
        # We need to find it in the source directory

        source_path = None

        # Try exact match first
        exact_path = image_source_dir / filename
        if exact_path.exists():
            source_path = exact_path
        else:
            # Try to find by matching the end of the filename
            # Sometimes WordPress adds hash prefixes
            for img_file in image_source_dir.glob('*'):
                if img_file.name.endswith(filename) or filename in img_file.name:
                    source_path = img_file
                    break

        if source_path and source_path.exists():
            target_path = target_dir / filename

            if not dry_run:
                try:
                    shutil.copy2(source_path, target_path)
                    results['images_copied'] += 1
                    results['copied_files'].append(filename)
                except Exception as e:
                    results['images_missing'] += 1
                    results['missing_files'].append(f"{filename} (copy error: {e})")
            else:
                results['images_copied'] += 1
                results['copied_files'].append(filename)
        else:
            results['images_missing'] += 1
            results['missing_files'].append(filename)

    return results


def main():
    parser = argparse.ArgumentParser(
        description='Copy only the images referenced in posts',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Copy images for all posts
  python copy_images.py _posts/ _migration/test_articles/images/

  # Dry run
  python copy_images.py _posts/ _migration/test_articles/images/ --dry-run

  # Single post
  python copy_images.py _posts/2020-06-30-article.md _migration/test_articles/images/
        """
    )
    parser.add_argument('posts', help='Post file or directory')
    parser.add_argument('image_source', help='Source directory containing images')
    parser.add_argument('--dry-run', action='store_true', help='Show what would be done')

    args = parser.parse_args()

    posts_path = Path(args.posts)
    source_dir = Path(args.image_source)

    if not posts_path.exists():
        print(f"❌ Error: {posts_path} does not exist")
        return 1

    if not source_dir.exists():
        print(f"❌ Error: {source_dir} does not exist")
        return 1

    print(f"\n{'='*60}")
    print(f"Smart Image Copy - Per-Post Directories")
    print(f"{'='*60}\n")

    if args.dry_run:
        print("🔍 DRY RUN - No files will be copied\n")

    # Collect posts to process
    if posts_path.is_file():
        post_files = [posts_path]
    else:
        post_files = [f for f in posts_path.glob('*.md')
                     if not f.name.startswith('.')]

    if not post_files:
        print(f"❌ No markdown files found")
        return 1

    print(f"📁 Source images: {source_dir}")
    print(f"📄 Processing {len(post_files)} post(s)\n")

    # Process each post
    all_results = []
    for post_path in post_files:
        print(f"📄 {post_path.name}")
        results = copy_post_images(post_path, source_dir, args.dry_run)
        all_results.append(results)

        if 'error' in results:
            print(f"  ✗ Error: {results['error']}")
            continue

        print(f"  → Found {results['images_found']} image reference(s)")
        print(f"  → Copied {results['images_copied']} image(s)")

        if results['images_missing'] > 0:
            print(f"  ⚠ Missing {results['images_missing']} image(s):")
            for missing in results['missing_files'][:3]:
                print(f"    - {missing}")
            if len(results['missing_files']) > 3:
                print(f"    ... and {len(results['missing_files']) - 3} more")

        print()

    # Summary
    print(f"{'='*60}")
    print("Summary")
    print(f"{'='*60}\n")

    total_found = sum(r['images_found'] for r in all_results)
    total_copied = sum(r['images_copied'] for r in all_results)
    total_missing = sum(r['images_missing'] for r in all_results)

    print(f"Total images referenced: {total_found}")
    print(f"Images copied: {total_copied}")
    print(f"Images missing: {total_missing}")

    if not args.dry_run and total_copied > 0:
        # Calculate disk usage
        posts_parent = posts_path if posts_path.is_dir() else posts_path.parent
        img_dir = posts_parent.parent / 'assets' / 'img' / 'posts'

        if img_dir.exists():
            total_size = sum(f.stat().st_size for f in img_dir.rglob('*') if f.is_file())
            size_mb = total_size / (1024 * 1024)
            print(f"\n💾 Total disk usage: {size_mb:.1f} MB")

    return 0


if __name__ == '__main__':
    import sys
    sys.exit(main())
