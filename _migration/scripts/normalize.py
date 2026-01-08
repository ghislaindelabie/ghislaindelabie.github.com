#!/usr/bin/env python3
"""
WordPress to Jekyll Post Normalization Script
Main script to normalize WordPress-exported markdown posts

Features implemented:
- A: Frontmatter standardization ✓
- B: Heading normalization (TODO)
- C: Markdown cleanup (TODO)
- D: Code block standardization (TODO)
- E: Embed detection & conversion (TODO)
- F: Image processing (TODO)
- G: Link checking & Wayback integration (TODO)
"""

import os
import sys
import argparse
from pathlib import Path

# Import feature modules
sys.path.insert(0, str(Path(__file__).parent))
from utils import frontmatter, headings, markdown_cleanup, code_blocks, embeds, images, links


def normalize_post(filepath, config):
    """
    Normalize a single WordPress-exported markdown post

    Args:
        filepath: Path to markdown file
        config: Configuration dict with feature flags

    Returns:
        dict: Results with status and any issues found
    """
    results = {
        'file': str(filepath),
        'features': {},
        'issues': [],
        'status': 'pending'
    }

    # Read file
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
    except Exception as e:
        results['status'] = 'error'
        results['issues'].append(f"Failed to read file: {e}")
        return results

    original_content = content

    # Feature A: Frontmatter standardization
    if config.get('frontmatter', True):
        print("  → Running Feature A: Frontmatter standardization...")
        content, feature_results = frontmatter.normalize(content)
        results['features']['frontmatter'] = feature_results

        # Display results
        if feature_results['changes']:
            print(f"    ✓ Changes: {len(feature_results['changes'])}")
            for change in feature_results['changes']:
                print(f"      - {change}")

        if feature_results['warnings']:
            print(f"    ⚠ Warnings: {len(feature_results['warnings'])}")
            for warning in feature_results['warnings']:
                print(f"      - {warning}")

        if feature_results['issues']:
            print(f"    ✗ Issues: {len(feature_results['issues'])}")
            for issue in feature_results['issues']:
                print(f"      - {issue}")

    # Feature B: Heading normalization
    if config.get('headings', True):
        print("  → Running Feature B: Heading normalization...")
        content, feature_results = headings.normalize(content)
        results['features']['headings'] = feature_results

        # Display results
        if feature_results['changes']:
            print(f"    ✓ Changes: {len(feature_results['changes'])}")
            for change in feature_results['changes']:
                print(f"      - {change}")

        if feature_results['warnings']:
            print(f"    ⚠ Warnings: {len(feature_results['warnings'])}")
            for warning in feature_results['warnings']:
                print(f"      - {warning}")

        if feature_results['issues']:
            print(f"    ✗ Issues: {len(feature_results['issues'])}")
            for issue in feature_results['issues']:
                print(f"      - {issue}")

    # Feature C: Markdown cleanup
    if config.get('markdown_cleanup', True):
        print("  → Running Feature C: Markdown cleanup...")
        content, feature_results = markdown_cleanup.normalize(content)
        results['features']['markdown_cleanup'] = feature_results

        # Display results
        if feature_results['changes']:
            print(f"    ✓ Changes: {len(feature_results['changes'])}")
            for change in feature_results['changes']:
                print(f"      - {change}")

        if feature_results['warnings']:
            print(f"    ⚠ Warnings: {len(feature_results['warnings'])}")
            for warning in feature_results['warnings']:
                print(f"      - {warning}")

        if feature_results['issues']:
            print(f"    ✗ Issues: {len(feature_results['issues'])}")
            for issue in feature_results['issues']:
                print(f"      - {issue}")

    # Feature D: Code block standardization
    if config.get('code_blocks', True):
        print("  → Running Feature D: Code block standardization...")
        content, feature_results = code_blocks.normalize(content)
        results['features']['code_blocks'] = feature_results

        # Display results
        if feature_results['changes']:
            print(f"    ✓ Changes: {len(feature_results['changes'])}")
            for change in feature_results['changes']:
                print(f"      - {change}")

        if feature_results['warnings']:
            print(f"    ⚠ Warnings: {len(feature_results['warnings'])}")
            for warning in feature_results['warnings']:
                print(f"      - {warning}")

        if feature_results['issues']:
            print(f"    ✗ Issues: {len(feature_results['issues'])}")
            for issue in feature_results['issues']:
                print(f"      - {issue}")

    # Feature E: Embed detection & conversion
    if config.get('embeds', True):
        print("  → Running Feature E: Embed detection & conversion...")
        content, feature_results = embeds.normalize(content)
        results['features']['embeds'] = feature_results

        # Display results
        if feature_results['changes']:
            print(f"    ✓ Changes: {len(feature_results['changes'])}")
            for change in feature_results['changes']:
                print(f"      - {change}")

        if feature_results['warnings']:
            print(f"    ⚠ Warnings: {len(feature_results['warnings'])}")
            for warning in feature_results['warnings']:
                print(f"      - {warning}")

        if feature_results['issues']:
            print(f"    ✗ Issues: {len(feature_results['issues'])}")
            for issue in feature_results['issues']:
                print(f"      - {issue}")

    # Feature F: Image processing
    if config.get('images', True):
        print("  → Running Feature F: Image processing...")
        content, feature_results = images.normalize(content, filepath)
        results['features']['images'] = feature_results

        # Display results
        if feature_results['changes']:
            print(f"    ✓ Changes: {len(feature_results['changes'])}")
            for change in feature_results['changes']:
                print(f"      - {change}")

        if feature_results['warnings']:
            print(f"    ⚠ Warnings: {len(feature_results['warnings'])}")
            for warning in feature_results['warnings']:
                print(f"      - {warning}")

        if feature_results['issues']:
            print(f"    ✗ Issues: {len(feature_results['issues'])}")
            for issue in feature_results['issues']:
                print(f"      - {issue}")

    # Feature G: Link checking & Wayback integration
    if config.get('links', True):
        print("  → Running Feature G: Link checking...")
        content, feature_results = links.normalize(content)
        results['features']['links'] = feature_results

        # Display results
        if feature_results['changes']:
            print(f"    ✓ Changes: {len(feature_results['changes'])}")
            for change in feature_results['changes']:
                print(f"      - {change}")

        if feature_results['warnings']:
            print(f"    ⚠ Warnings: {len(feature_results['warnings'])}")
            for warning in feature_results['warnings']:
                print(f"      - {warning}")

        if feature_results['issues']:
            print(f"    ✗ Issues: {len(feature_results['issues'])}")
            for issue in feature_results['issues']:
                print(f"      - {issue}")

    # Write normalized content
    if not config.get('dry_run', False):
        output_path = filepath.parent / f"{filepath.stem}.NORMALIZED.md"
        try:
            with open(output_path, 'w', encoding='utf-8') as f:
                f.write(content)
            results['output'] = str(output_path)
            print(f"  ✓ Written to: {output_path.name}")
        except Exception as e:
            results['issues'].append(f"Failed to write file: {e}")
            results['status'] = 'error'
            return results
    else:
        print("  (Dry run - no files written)")
        results['output'] = '(dry run)'

    # Overall status
    has_errors = any(
        feat.get('status') == 'error'
        for feat in results['features'].values()
    )
    has_issues = any(
        feat.get('issues')
        for feat in results['features'].values()
    )

    if has_errors:
        results['status'] = 'error'
    elif has_issues:
        results['status'] = 'warning'
    else:
        results['status'] = 'success'

    return results


def main():
    parser = argparse.ArgumentParser(
        description='Normalize WordPress-exported markdown posts for Jekyll',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Normalize a single post (all features)
  python normalize.py test_articles/2020-06-30-retour-vers-le-futur.md

  # Normalize with specific feature only
  python normalize.py test_articles/post.md --feature A

  # Dry run (show changes without writing)
  python normalize.py test_articles/post.md --dry-run

  # Normalize all posts in directory
  python normalize.py test_articles/
        """
    )
    parser.add_argument(
        'input',
        help='Input markdown file or directory'
    )
    parser.add_argument(
        '--feature',
        choices=['A', 'B', 'C', 'D', 'E', 'F', 'G'],
        help='Run only specific feature (A-G)'
    )
    parser.add_argument(
        '--dry-run',
        action='store_true',
        help='Show what would be done without writing files'
    )

    args = parser.parse_args()

    # Configuration (enable/disable features)
    config = {
        'frontmatter': True,
        'headings': True,
        'markdown_cleanup': True,
        'code_blocks': True,
        'embeds': True,
        'images': True,
        'links': True,
        'dry_run': args.dry_run
    }

    # Override if specific feature requested
    if args.feature:
        # Disable all
        config = {k: False for k in config}
        config['dry_run'] = args.dry_run

        # Enable only requested feature
        feature_map = {
            'A': 'frontmatter',
            'B': 'headings',
            'C': 'markdown_cleanup',
            'D': 'code_blocks',
            'E': 'embeds',
            'F': 'images',
            'G': 'links',
        }
        if args.feature in feature_map:
            config[feature_map[args.feature]] = True
            print(f"\n🎯 Running Feature {args.feature} only\n")

    # Process file(s)
    input_path = Path(args.input)

    if not input_path.exists():
        print(f"❌ Error: {input_path} does not exist")
        sys.exit(1)

    print(f"\n{'='*60}")
    print(f"WordPress to Jekyll Normalization")
    print(f"{'='*60}\n")

    results_summary = []

    if input_path.is_file():
        print(f"📄 Processing: {input_path.name}\n")
        results = normalize_post(input_path, config)
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
            results = normalize_post(md_file, config)
            results_summary.append(results)
            print()

    else:
        print(f"❌ Error: {input_path} is not a valid file or directory")
        sys.exit(1)

    # Summary
    print(f"\n{'='*60}")
    print("Summary")
    print(f"{'='*60}\n")

    success_count = sum(1 for r in results_summary if r['status'] == 'success')
    warning_count = sum(1 for r in results_summary if r['status'] == 'warning')
    error_count = sum(1 for r in results_summary if r['status'] == 'error')

    print(f"✓ Success: {success_count}")
    print(f"⚠ Warnings: {warning_count}")
    print(f"✗ Errors: {error_count}")
    print(f"\nTotal processed: {len(results_summary)}")

    if error_count > 0:
        print("\n⚠️  Some files had errors. Review the output above.")
        sys.exit(1)


if __name__ == '__main__':
    main()
