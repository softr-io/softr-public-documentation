#!/usr/bin/env python3
"""
Convert step content into Mintlify Steps component format.

This script reads step definitions and converts them into the proper
Mintlify Steps JSX component format.
"""

import re
import sys
from pathlib import Path


def convert_steps(content: str) -> str:
    """
    Convert markdown step definitions into Mintlify Steps component.

    Supports multiple formats:
    1. Numbered list format (1., 2., 3., etc.)
    2. Heading format (## Step 1, ## Step 2, etc.)
    3. Custom delimiter format (e.g., ### Step Title)

    Args:
        content: The input content containing steps

    Returns:
        Formatted Mintlify Steps JSX component
    """

    steps = []

    # Find all heading-based steps (### or ##)
    # Pattern: heading (### or ##) followed by content until next heading
    heading_pattern = r'^(#{2,4})\s+(.+?)$'

    lines = content.split('\n')
    current_step = None
    current_content = []

    for line in lines:
        heading_match = re.match(heading_pattern, line)

        if heading_match:
            # Save previous step if exists
            if current_step:
                step_content = '\n'.join(current_content).strip()
                steps.append((current_step, step_content))

            # Start new step and remove "Step N: " prefix and ** markers
            title = heading_match.group(2).strip()
            # Remove ** markers first
            title = title.replace('**', '')
            # Remove "Step N: " prefix (with flexible spacing)
            title = re.sub(r'^Step\s+\d+:\s*', '', title, flags=re.IGNORECASE)
            current_step = title
            current_content = []
        else:
            # Add content to current step
            if current_step is not None:
                current_content.append(line)

    # Don't forget the last step
    if current_step:
        step_content = '\n'.join(current_content).strip()
        steps.append((current_step, step_content))

    # Build the JSX component
    jsx_lines = ['<Steps>']

    for title, step_content in steps:
        jsx_lines.append(f'  <Step title="{title}">')
        if step_content:
            # Preserve content structure, including blank lines for readability
            lines_content = step_content.split('\n')
            for line in lines_content:
                if line.strip():
                    jsx_lines.append(f'    {line}')
                elif jsx_lines[-1] != '':  # Avoid multiple consecutive blank lines
                    jsx_lines.append('')
        else:
            jsx_lines.append(f'    These are instructions or content that only pertain to {title.lower()}.')
        jsx_lines.append('  </Step>')

    jsx_lines.append('</Steps>')

    return '\n'.join(jsx_lines)


def convert_file(input_file: str, output_file: str = None) -> str:
    """
    Convert a markdown file containing steps into Mintlify component.

    Args:
        input_file: Path to input .mdx file
        output_file: Path to output file (if None, defaults to same as input_file)

    Returns:
        The converted JSX component as string
    """

    input_path = Path(input_file)

    if not input_path.exists():
        print(f"Error: File '{input_file}' not found", file=sys.stderr)
        sys.exit(1)

    # If no output file specified, use the same as input file
    if output_file is None:
        output_file = input_file

    # Read the input file
    with open(input_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Convert the content
    result = convert_steps(content)

    # Write to output file
    output_path = Path(output_file)
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(result)
    print(f"Converted steps written to: {output_file}")

    return result


if __name__ == '__main__':
    convert_file('steps.mdx')
