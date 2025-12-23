# WordPress Import Normalization Script - Development Plan

## Overview
Develop Phase 2 normalization scripts for WordPress-to-Jekyll migration using test-driven, iterative approach.

**Scope:** Features A-G from `BLOG_MIGRATION_PLAN.md` Phase 2.1

**Timeline:** Development in feature-by-feature iterations with continuous testing

---

## Development Approach

### Methodology
1. **Reference-driven development** - Use 1 article as primary test case
2. **Feature-by-feature iteration** - Build A→G incrementally
3. **Test after each feature** - Validate before moving to next
4. **Document everything** - Track decisions, issues, deferrals
5. **Validation phase** - Test on 5 additional articles after all features complete
6. **Collaborative debugging** - Work together to assess and refine

### Test Dataset
**Total articles:** 10 WordPress exports

**Breakdown:**
- **1 Reference article** - Primary development test case
- **5 Validation articles** - Secondary testing after feature completion
- **4 Reserve articles** - For edge cases or additional testing

---

## Phase 0: Setup & Preparation

### 0.1 WordPress Import Complete
- [x] Export WordPress XML
- [x] Export WordPress media files
- [x] Run `wordpress-export-to-markdown`
- [x] Organize in `wp-import/` folder

### 0.2 Select Reference Article
**Criteria for selection:**
- ✅ Has multiple types of issues (not too simple)
- ✅ Includes images
- ✅ Has code blocks or embeds
- ✅ Contains links (internal and external)
- ✅ Representative of typical content
- ✅ French language (to test language detection)
- ✅ Medium complexity (not edge case nightmare)

**Selected reference:** `wp-import/output/posts/YYYY-MM-DD-[article-name].md`

**Backup original:**
```bash
cp wp-import/output/posts/YYYY-MM-DD-reference.md \
   wp-import/output/posts/YYYY-MM-DD-reference.ORIGINAL.md
```

### 0.3 Create Development Workspace
```
_migration/
├── scripts/
│   ├── normalize.py              # Main script
│   ├── utils/
│   │   ├── frontmatter.py       # Feature A
│   │   ├── headings.py          # Feature B
│   │   ├── markdown_cleanup.py  # Feature C
│   │   ├── code_blocks.py       # Feature D
│   │   ├── embeds.py            # Feature E
│   │   ├── images.py            # Feature F
│   │   └── links.py             # Feature G
│   └── tests/
│       └── test_normalize.py    # Test suite
├── data/
│   ├── link_map.json
│   └── embed_patterns.json
├── logs/
│   └── iteration_log.md         # Development log
└── test_articles/
    ├── reference.md             # Copy of reference
    ├── validation_1.md          # Validation set
    ├── validation_2.md
    ├── validation_3.md
    ├── validation_4.md
    └── validation_5.md
```

### 0.4 Initial Script Structure
Create `_migration/scripts/normalize.py`:
```python
#!/usr/bin/env python3
"""
WordPress to Jekyll normalization script
Implements features A-G from BLOG_MIGRATION_PLAN.md Phase 2.1
"""

import os
import sys
import argparse
from pathlib import Path

# Feature modules (to be developed)
from utils import frontmatter
from utils import headings
from utils import markdown_cleanup
from utils import code_blocks
from utils import embeds
from utils import images
from utils import links


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
        'file': filepath,
        'features': {},
        'issues': [],
        'status': 'pending'
    }

    # Read file
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Feature A: Frontmatter standardization
    if config.get('frontmatter', True):
        content, feature_results = frontmatter.normalize(content)
        results['features']['frontmatter'] = feature_results

    # Feature B: Heading normalization
    if config.get('headings', True):
        content, feature_results = headings.normalize(content)
        results['features']['headings'] = feature_results

    # Feature C: Markdown cleanup
    if config.get('markdown_cleanup', True):
        content, feature_results = markdown_cleanup.normalize(content)
        results['features']['markdown_cleanup'] = feature_results

    # Feature D: Code block standardization
    if config.get('code_blocks', True):
        content, feature_results = code_blocks.normalize(content)
        results['features']['code_blocks'] = feature_results

    # Feature E: Embed detection & conversion
    if config.get('embeds', True):
        content, feature_results = embeds.normalize(content)
        results['features']['embeds'] = feature_results

    # Feature F: Image processing
    if config.get('images', True):
        content, feature_results = images.normalize(content, filepath)
        results['features']['images'] = feature_results

    # Feature G: Link checking & Wayback integration
    if config.get('links', True):
        content, feature_results = links.normalize(content)
        results['features']['links'] = feature_results

    # Write normalized content
    output_path = filepath.replace('.md', '.NORMALIZED.md')
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(content)

    results['status'] = 'complete'
    results['output'] = output_path

    return results


def main():
    parser = argparse.ArgumentParser(
        description='Normalize WordPress-exported markdown posts'
    )
    parser.add_argument('input', help='Input markdown file or directory')
    parser.add_argument('--feature', help='Run only specific feature (A-G)')
    parser.add_argument('--dry-run', action='store_true',
                       help='Show what would be done without writing files')

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
    }

    # Override if specific feature requested
    if args.feature:
        config = {k: False for k in config}
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

    # Process file(s)
    input_path = Path(args.input)

    if input_path.is_file():
        results = normalize_post(input_path, config)
        print(f"✅ Normalized: {results['output']}")
    elif input_path.is_dir():
        for md_file in input_path.glob('*.md'):
            results = normalize_post(md_file, config)
            print(f"✅ Normalized: {results['output']}")
    else:
        print(f"❌ Error: {input_path} is not a valid file or directory")
        sys.exit(1)


if __name__ == '__main__':
    main()
```

---

## Testing Strategy: Hybrid "Checkpoint" Approach

### Rationale
Balance robustness and efficiency by validating foundational features early while maintaining development momentum.

### Structure

**Phase 1: Foundation Features (A-C)**
```
Feature A (Frontmatter) → Test on reference → Document
Feature B (Headings) → Test on reference → Document
Feature C (Markdown cleanup) → Test on reference → Document

✅ Checkpoint 1: Test A+B+C together on 2-3 articles
   (Foundational - validate before proceeding)
```

**Phase 2: Content Features (D-E)**
```
Feature D (Code blocks) → Test on reference → Document
Feature E (Embeds) → Test on reference → Document

✅ Checkpoint 2: Test D+E on 2-3 articles
   (Less critical, quick validation)
```

**Phase 3: Complex Features (F-G)**
```
Feature F (Images) → Test on reference → Document
Feature G (Links/Wayback) → Test on reference → Document

✅ Checkpoint 3: Test F+G on 3-5 articles
   (Most complex, needs thorough validation)
```

**Phase 4: Full Validation**
```
✅ Final: Test A-G full pipeline on all 10 articles
```

### Benefits
- ✅ Catch fundamental issues at checkpoints
- ✅ Keep development momentum (not testing every feature individually)
- ✅ Deep-test complex features where edge cases live
- ✅ ~15-20 test runs total (vs. 35 or 10)
- ✅ Balance of robustness and efficiency

---

## Development Workflow (Per Feature)

### For Each Feature (A through G):

#### Step 1: Develop Feature Module
Create `_migration/scripts/utils/[feature].py` with:
- Core normalization logic
- Helper functions
- Error handling
- Return format: `(normalized_content, results_dict)`

#### Step 2: Test on Reference Article
```bash
# Run only this feature
python _migration/scripts/normalize.py \
  _migration/test_articles/reference.md \
  --feature A

# Output: reference.NORMALIZED.md
```

#### Step 3: Analyze Output
**Compare:**
- Input: `reference.md`
- Output: `reference.NORMALIZED.md`

**Check:**
- ✅ Expected changes applied correctly
- ⚠️ Unexpected changes (good or bad?)
- ❌ Errors or missed cases

**Use diff tool:**
```bash
diff -u reference.md reference.NORMALIZED.md | less
# Or use visual diff tool
```

#### Step 4: Document Iteration
**Add to `_migration/logs/iteration_log.md`:**

```markdown
## Feature [X]: [Feature Name]
### Iteration N
**Date:** YYYY-MM-DD
**Reference article:** `reference.md`

#### Input Sample
[Problematic section from input]

#### Expected Output
[What it should become]

#### Actual Output
[What script produced]

#### Status
- [ ] Working correctly
- [ ] Needs fixes
- [ ] Partially working
- [ ] Failed

#### Issues Found
1. Issue description
2. Issue description

#### Decisions Made
- Decision 1: [Why]
- Decision 2: [Why]
- Deferred to manual review: [What & why]

#### Changes to Make
- [ ] Fix issue 1
- [ ] Fix issue 2

#### Next Steps
[What to do next]
```

#### Step 5: Iterate Until Working
- Fix issues identified
- Re-run on reference article
- Re-analyze
- Document iteration
- Repeat until feature works correctly

#### Step 6: Git Commit
```bash
git add _migration/scripts/utils/[feature].py
git commit -m "feat: [Feature name] (Feature [X])"
```

#### Step 7: Move to Next Feature
Repeat workflow for next feature (B, C, D, etc.)

---

## Feature Development Order

### Feature A: Frontmatter Standardization
**File:** `_migration/scripts/utils/frontmatter.py`

**Tasks:**
1. Parse existing frontmatter (if any)
2. **Set language to French** (`lang: fr`) - WordPress import is French-only
3. Ensure required fields present:
   - `layout: post`
   - `title: "..."`
   - `date: YYYY-MM-DD HH:MM:SS`
   - `description: "..."`
   - `tags: [...]`
   - `categories: post`
   - `lang: fr` (hardcoded for WordPress)
   - `original_url: "..."` (if from WordPress)
4. Generate description from first paragraph if missing
5. Validate date format (ISO)
6. Return standardized frontmatter

**Testing criteria:**
- [ ] All required fields present
- [ ] Language set to French (`lang: fr`)
- [ ] Date in correct format
- [ ] Description generated if missing
- [ ] Preserves existing good data

**Note:** Language detection omitted for WordPress import (all French). Will implement if needed for other sources (Medium, etc.) later.

---

### Feature B: Heading Normalization
**File:** `_migration/scripts/utils/headings.py`

**Tasks:**
1. Ensure no H1 in body (title goes in frontmatter)
2. Fix heading hierarchy (no skipped levels)
3. Convert to ATX style (`##` not Setext underlines)
4. Remove duplicate headings
5. Ensure headings have blank line before/after

**Testing criteria:**
- [ ] No H1 in body
- [ ] Hierarchy is correct (H2→H3, not H2→H4)
- [ ] All ATX format
- [ ] Proper spacing around headings

---

### Feature C: Markdown Cleanup
**File:** `_migration/scripts/utils/markdown_cleanup.py`

**Tasks:**
1. Remove `&nbsp;`, `<br />`, `<br>`, `&amp;`
2. Remove empty `<p>` tags
3. Convert WordPress shortcodes to Jekyll equivalents
4. Fix escaped characters (remove unnecessary `\`)
5. Normalize list formatting
6. Remove excessive blank lines (max 2 consecutive)
7. Fix WordPress caption tags

**Testing criteria:**
- [ ] No HTML entities (`&nbsp;`, etc.)
- [ ] No empty tags
- [ ] Lists properly formatted
- [ ] Max 2 blank lines anywhere
- [ ] Captions converted to markdown

---

### Feature D: Code Block Standardization
**File:** `_migration/scripts/utils/code_blocks.py`

**Tasks:**
1. Detect all code blocks (indented, `<pre>`, `~~~`, ` ``` `)
2. Convert all to fenced format (` ``` `)
3. Add language hints where detectable
4. Preserve syntax highlighting classes

**Testing criteria:**
- [ ] All code blocks are fenced
- [ ] Language hints present where possible
- [ ] Code content unchanged
- [ ] No indented code blocks remain

---

### Feature E: Embed Detection & Conversion
**File:** `_migration/scripts/utils/embeds.py`

**Tasks:**
1. Detect embed patterns:
   - YouTube (`<iframe>` with youtube.com)
   - Vimeo (`<iframe>` with vimeo.com)
   - Twitter (`<blockquote class="twitter-tweet">`)
   - GitHub Gists
2. Convert to Jekyll includes where possible
3. Flag unknown embeds for manual review

**Testing criteria:**
- [ ] YouTube embeds → `{% include youtube.html %}`
- [ ] Other common embeds converted
- [ ] Unknown embeds flagged
- [ ] Embed content preserved

---

### Feature F: Image Processing
**File:** `_migration/scripts/utils/images.py`

**Tasks:**
1. Extract all image URLs from markdown
2. Check if image exists in media export
3. Copy images to `assets/img/posts/[post-slug]/`
4. Update markdown paths to new location
5. Flag missing images
6. Generate alt text if missing

**Testing criteria:**
- [ ] All images copied to assets folder
- [ ] Paths updated correctly
- [ ] Missing images flagged
- [ ] Alt text present

---

### Feature G: Link Checking & Wayback Integration
**File:** `_migration/scripts/utils/links.py`

**Tasks:**
1. Extract all external links
2. Test link status (HTTP HEAD with timeout)
3. For broken links:
   - Query Wayback Machine API
   - Replace with archive.org URL if available
   - Flag if no snapshot exists
4. Log all replacements

**Testing criteria:**
- [ ] All external links checked
- [ ] Broken links replaced with Wayback
- [ ] Replacements logged
- [ ] Links without archives flagged

---

## Validation Phase (After All Features Complete)

### Test on 5 Validation Articles

**Process for each article:**

1. **Run normalization script**
   ```bash
   python _migration/scripts/normalize.py \
     _migration/test_articles/validation_1.md
   ```

2. **Thorough inspection**
   - Read through entire normalized article
   - Check all features (A-G) visually
   - Test in Jekyll (build and preview)
   - Verify images load
   - Click all links

3. **Document findings**
   Add to `_migration/logs/validation_results.md`:
   ```markdown
   ## Validation Article 1: [Title]
   **Original:** `validation_1.md`
   **Normalized:** `validation_1.NORMALIZED.md`

   ### Feature A: Frontmatter
   - [x] All fields present
   - [x] Language correct
   - [ ] Issue: Description too short

   ### Feature B: Headings
   - [x] Hierarchy correct
   - [x] No H1 in body

   [etc. for all features]

   ### Overall Assessment
   - **Status:** ✅ Good / ⚠️ Needs fixes / ❌ Failed
   - **Issues found:** [List]
   - **Action items:** [What to fix]
   ```

4. **Fix issues if needed**
   - Update scripts
   - Re-run on all validation articles
   - Re-test

5. **Final approval**
   - Review all 5 validation results
   - Confirm scripts ready for full batch

---

## Collaboration Process

### Your Role
- Provide the 10 articles
- Help select reference article
- Review iteration logs
- Test manually alongside script testing
- Assess what should be automated vs. manual
- Make decisions on edge cases
- Final approval of script behavior

### My Role
- Develop feature modules
- Run scripts on reference article
- Analyze output vs. input
- Document iterations
- Fix bugs and refine logic
- Test on validation articles
- Propose solutions for issues

### Communication Protocol
**After each feature iteration:**
1. I share:
   - Iteration log entry
   - Input/output diff
   - Issues found
   - Proposed fixes or questions

2. You provide:
   - Feedback on behavior
   - Decisions on edge cases
   - Additional test cases if needed
   - Approval to proceed

**Decision-making:**
- **Script should handle:** Common, predictable issues
- **Manual review:** Ambiguous, complex, or rare cases
- **Defer:** Nice-to-have features that slow progress

---

## Success Criteria

### Per Feature
- [ ] Works correctly on reference article
- [ ] Documented with iteration log
- [ ] Git committed
- [ ] No regressions in previous features

### Overall (After All Features)
- [ ] All features A-G implemented
- [ ] Tested on reference article
- [ ] Validated on 5 articles
- [ ] Issues documented
- [ ] Scripts ready for full batch processing

### Ready for Production
- [ ] Script runs on all 10 test articles successfully
- [ ] <5% of cases need manual intervention
- [ ] All issues logged in manual review queue
- [ ] Documentation complete
- [ ] You approve script behavior

---

## Iteration Log Template

Use this template for each feature iteration:

```markdown
## Feature [X]: [Feature Name]

### Iteration [N] - [Date]

#### Input Sample
\`\`\`markdown
[Problematic section from reference article]
\`\`\`

#### Expected Output
\`\`\`markdown
[What it should look like after normalization]
\`\`\`

#### Actual Output
\`\`\`markdown
[What the script actually produced]
\`\`\`

#### Analysis
**What worked:**
- ✅ Item 1
- ✅ Item 2

**What needs improvement:**
- ⚠️ Issue 1: Description
- ⚠️ Issue 2: Description

**What to defer (don't over-engineer):**
- Edge case X: Reason
- Complex case Y: Reason

#### Decisions Made
1. **Decision:** [What was decided]
   **Rationale:** [Why]
   **Impact:** [What this means]

2. **Decision:** [What was decided]
   **Rationale:** [Why]
   **Impact:** [What this means]

#### Changes for Next Iteration
- [ ] Fix issue 1
- [ ] Fix issue 2
- [ ] Add test case for edge case

#### Status
- [ ] Feature complete
- [x] Needs another iteration
- [ ] Blocked (waiting on decision/feedback)

#### Next Steps
[What to do next]
```

---

## Timeline Estimate

**Per feature:** 1-3 iterations (depends on complexity)
**Total features:** A-G (7 features)
**Validation:** 5 articles × ~30min each

**Estimated timeline:**
- Week 1: Features A-C (frontmatter, headings, markdown cleanup)
- Week 2: Features D-E (code blocks, embeds)
- Week 3: Features F-G (images, links) - most complex
- Week 4: Validation phase + refinements

**Total:** ~3-4 weeks of collaborative development

---

## Notes

- Flexibility is key - adjust plan as we learn
- Don't over-engineer - flag complex cases for manual review
- Document decisions - future reference is valuable
- Test early, test often - catch issues before they compound
- Version control everything - easy rollback if needed

---

## Next Steps

1. ✅ WordPress import completes
2. ⬜ Select reference article (you + me review options)
3. ⬜ Copy 10 articles to `_migration/test_articles/`
4. ⬜ Set up development workspace
5. ⬜ Begin Feature A development
6. ⬜ First iteration on reference article
7. ⬜ Review together and proceed

Let's build this! 🚀
