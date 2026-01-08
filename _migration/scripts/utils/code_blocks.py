#!/usr/bin/env python3
"""
Feature D: Code Block Standardization
Converts all code blocks to fenced format with language hints
"""

import re
from typing import Tuple, Dict


def normalize(content: str) -> Tuple[str, Dict]:
    """
    Normalize code blocks in markdown content

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

    # 1. Convert indented code blocks to fenced
    body, indented_count = convert_indented_to_fenced(body)
    if indented_count > 0:
        results['changes'].append(f"Converted {indented_count} indented code blocks to fenced format")

    # 2. Convert <pre> tags to fenced
    body, pre_count = convert_pre_to_fenced(body)
    if pre_count > 0:
        results['changes'].append(f"Converted {pre_count} <pre> tags to fenced format")

    # 3. Convert tilde fences (~~~) to backtick fences (```)
    body, tilde_count = convert_tilde_to_backtick(body)
    if tilde_count > 0:
        results['changes'].append(f"Converted {tilde_count} tilde fences to backtick fences")

    # 4. Add language hints where detectable
    body, hint_count = add_language_hints(body)
    if hint_count > 0:
        results['changes'].append(f"Added {hint_count} language hints to code blocks")

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


def convert_indented_to_fenced(body: str) -> Tuple[str, int]:
    """
    Convert indented code blocks (4 spaces or tab) to fenced format

    Returns:
        tuple: (converted_body, count_of_conversions)
    """
    count = 0
    lines = body.split('\n')
    result_lines = []
    in_code_block = False
    code_buffer = []

    i = 0
    while i < len(lines):
        line = lines[i]

        # Check if line is indented code (4 spaces or tab)
        is_code_line = (line.startswith('    ') or line.startswith('\t')) and line.strip()

        if is_code_line and not in_code_block:
            # Start of indented code block
            in_code_block = True
            code_buffer = [line[4:] if line.startswith('    ') else line[1:]]
        elif is_code_line and in_code_block:
            # Continue code block
            code_buffer.append(line[4:] if line.startswith('    ') else line[1:])
        elif in_code_block and not is_code_line:
            # End of code block
            if line.strip() == '':
                # Blank line - might continue
                # Look ahead to see if more code follows
                if i + 1 < len(lines) and (lines[i + 1].startswith('    ') or lines[i + 1].startswith('\t')):
                    code_buffer.append('')
                else:
                    # End of block
                    result_lines.append('```')
                    result_lines.extend(code_buffer)
                    result_lines.append('```')
                    result_lines.append('')
                    in_code_block = False
                    code_buffer = []
                    count += 1
            else:
                # Definitely end of block
                result_lines.append('```')
                result_lines.extend(code_buffer)
                result_lines.append('```')
                result_lines.append(line)
                in_code_block = False
                code_buffer = []
                count += 1
                i += 1
                continue
        else:
            # Regular line
            result_lines.append(line)

        i += 1

    # Handle case where file ends with code block
    if in_code_block and code_buffer:
        result_lines.append('```')
        result_lines.extend(code_buffer)
        result_lines.append('```')
        count += 1

    return '\n'.join(result_lines), count


def convert_pre_to_fenced(body: str) -> Tuple[str, int]:
    """
    Convert <pre> and <code> tags to fenced code blocks

    Returns:
        tuple: (converted_body, count_of_conversions)
    """
    count = 0

    # Pattern for <pre><code>...</code></pre>
    def replace_pre_code(match):
        nonlocal count
        count += 1
        code_content = match.group(1)
        # Decode HTML entities
        code_content = code_content.replace('&lt;', '<')
        code_content = code_content.replace('&gt;', '>')
        code_content = code_content.replace('&amp;', '&')
        code_content = code_content.replace('&quot;', '"')
        return f"```\n{code_content}\n```"

    body = re.sub(r'<pre><code>(.*?)</code></pre>', replace_pre_code, body, flags=re.DOTALL | re.IGNORECASE)

    # Pattern for <pre>...</pre> without <code>
    def replace_pre(match):
        nonlocal count
        count += 1
        code_content = match.group(1)
        code_content = code_content.replace('&lt;', '<')
        code_content = code_content.replace('&gt;', '>')
        code_content = code_content.replace('&amp;', '&')
        code_content = code_content.replace('&quot;', '"')
        return f"```\n{code_content}\n```"

    body = re.sub(r'<pre>(.*?)</pre>', replace_pre, body, flags=re.DOTALL | re.IGNORECASE)

    return body, count


def convert_tilde_to_backtick(body: str) -> Tuple[str, int]:
    """
    Convert tilde code fences (~~~) to backtick fences (```)

    Returns:
        tuple: (converted_body, count_of_conversions)
    """
    count = 0

    # Count tilde fence blocks
    tilde_pattern = r'^~~~.*?$'
    matches = re.findall(tilde_pattern, body, re.MULTILINE)
    count = len(matches)

    if count > 0:
        # Replace opening and closing tilde fences
        body = re.sub(r'^~~~(.*)$', r'```\1', body, flags=re.MULTILINE)

    return body, count


def add_language_hints(body: str) -> Tuple[str, int]:
    """
    Add language hints to fenced code blocks where detectable

    Returns:
        tuple: (body_with_hints, count_of_hints_added)
    """
    count = 0

    # Pattern to find fenced code blocks without language hints
    # Matches: ```\n or ```  \n (with optional whitespace)
    pattern = r'^```\s*\n(.*?)^```'

    def analyze_and_add_hint(match):
        nonlocal count
        code_content = match.group(1)

        # Detect language based on content
        language = detect_language(code_content)

        if language:
            count += 1
            return f"```{language}\n{code_content}```"
        else:
            # No language detected, keep as-is
            return match.group(0)

    body = re.sub(pattern, analyze_and_add_hint, body, flags=re.MULTILINE | re.DOTALL)

    return body, count


def detect_language(code: str) -> str:
    """
    Detect programming language from code content

    Returns:
        str: Language hint or empty string if unknown
    """
    code_lower = code.lower().strip()

    # Python indicators
    if any(keyword in code_lower for keyword in ['def ', 'import ', 'class ', 'from ', 'print(', '__init__']):
        return 'python'

    # JavaScript/TypeScript indicators
    if any(keyword in code_lower for keyword in ['const ', 'let ', 'var ', 'function ', '=>', 'console.log']):
        return 'javascript'

    # Bash/Shell indicators
    if code_lower.startswith('#!') or any(keyword in code_lower for keyword in ['#!/bin/', 'echo ', 'export ', 'if [', 'fi\n']):
        return 'bash'

    # HTML indicators
    if '<html' in code_lower or '<div' in code_lower or '<!doctype' in code_lower:
        return 'html'

    # CSS indicators
    if re.search(r'\{[^}]*:[^}]*;[^}]*\}', code):  # CSS property syntax
        return 'css'

    # JSON indicators
    if code.strip().startswith('{') and '"' in code and ':' in code:
        return 'json'

    # YAML indicators (but not frontmatter)
    if re.match(r'^[\w-]+:\s*[\w-]', code_lower):
        return 'yaml'

    # SQL indicators
    if any(keyword in code_lower for keyword in [' select ', ' from ', ' where ', ' insert ', ' update ']):
        return 'sql'

    return ''  # Unknown


if __name__ == '__main__':
    # Test with sample content
    sample = """---
title: Test
---

Some text.

    # This is indented code
    def hello():
        print("world")

More text.

<pre><code>function test() {
  console.log("test");
}</code></pre>

~~~python
print("tilde fence")
~~~

```
# No language hint
echo "test"
```
"""

    normalized, results = normalize(sample)
    print("Results:", results)
    print("\nNormalized:\n", normalized)
