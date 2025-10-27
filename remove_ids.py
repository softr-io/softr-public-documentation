#!/usr/bin/env python3
"""
Script to remove IDs from file and folder names and update docs.json navigation.
Generates a report of all changes made.
"""

import os
import json
import re
from pathlib import Path
from typing import Dict, List, Tuple

class IDRemover:
    def __init__(self, base_path: str = "."):
        self.base_path = Path(base_path)
        self.docs_json_path = self.base_path / "docs.json"
        self.changes_report = []
        self.path_mapping = {}  # Maps old paths to new paths

    def extract_filename_without_id(self, name: str) -> str:
        """
        Extract the filename/folder name without the ID.
        ID appears to be 20+ character alphanumeric strings.
        Format: "name/ID/name/ID" -> "name/name"
        """
        # ID pattern: 22-character alphanumeric strings (could be longer/shorter)
        # They look like: 9kNyHJ3UeZkJc8Z6JuypBS, si84FeKzFRrGL6u53ckCQU
        id_pattern = r'^[A-Za-z0-9]{20,}$'

        parts = name.split('/')
        cleaned_parts = []

        for part in parts:
            if not re.match(id_pattern, part):
                cleaned_parts.append(part)

        return '/'.join(cleaned_parts)

    def get_mdx_files(self) -> List[Path]:
        """Find all .mdx files in the docs structure."""
        return list(self.base_path.glob('**/*.mdx'))

    def rename_files_and_folders(self) -> None:
        """Rename all files and folders, removing IDs."""
        # Recursively process and move all files to their new paths
        for old_path_str, new_path_str in sorted(self.path_mapping.items()):
            old_file = self.base_path / (old_path_str + '.mdx')
            new_file_path = self.base_path / (new_path_str + '.mdx')

            if old_file.exists():
                # Create parent directories if they don't exist
                new_file_path.parent.mkdir(parents=True, exist_ok=True)

                # Move file to new location
                old_file.rename(new_file_path)
                print(f"Moved file: {old_path_str}.mdx -> {new_path_str}.mdx")

        # Clean up empty directories
        self.cleanup_empty_directories()

    def cleanup_empty_directories(self) -> None:
        """Remove empty directories after file moves."""
        # Get all directories, sorted in reverse (deepest first)
        all_dirs = sorted([d for d in self.base_path.glob('**') if d.is_dir() and d != self.base_path],
                         key=lambda p: len(p.parts), reverse=True)

        for directory in all_dirs:
            try:
                if not any(directory.iterdir()):  # Check if directory is empty
                    directory.rmdir()
                    print(f"Removed empty directory: {directory.relative_to(self.base_path)}")
            except OSError:
                pass  # Directory not empty or other error

    def build_path_mapping(self) -> None:
        """Build a mapping of old paths to new paths."""
        with open(self.docs_json_path, 'r') as f:
            docs = json.load(f)

        pages = self.extract_all_pages(docs['navigation'])

        for old_path in pages:
            new_path = self.convert_path(old_path)
            if old_path != new_path:
                self.path_mapping[old_path] = new_path

    def convert_path(self, path: str) -> str:
        """Convert a path by removing IDs."""
        return self.extract_filename_without_id(path)

    def extract_all_pages(self, nav_obj) -> List[str]:
        """Extract all page paths from navigation structure."""
        pages = []

        if isinstance(nav_obj, dict):
            if 'pages' in nav_obj:
                for page in nav_obj['pages']:
                    if isinstance(page, str):
                        pages.append(page)
                    elif isinstance(page, dict):
                        pages.extend(self.extract_all_pages(page))
            for key, value in nav_obj.items():
                if key != 'pages':
                    pages.extend(self.extract_all_pages(value))
        elif isinstance(nav_obj, list):
            for item in nav_obj:
                pages.extend(self.extract_all_pages(item))

        return pages

    def update_docs_json(self) -> None:
        """Update all paths in docs.json."""
        with open(self.docs_json_path, 'r') as f:
            docs = json.load(f)

        # Update navigation
        docs['navigation'] = self.update_nav_structure(docs['navigation'], self.path_mapping)

        # Write updated docs.json
        with open(self.docs_json_path, 'w') as f:
            json.dump(docs, f, indent=2)

        print(f"Updated docs.json with {len(self.path_mapping)} path changes")

    def update_nav_structure(self, nav_obj, mapping: Dict[str, str]):
        """Recursively update navigation structure."""
        if isinstance(nav_obj, dict):
            if 'pages' in nav_obj:
                nav_obj['pages'] = [
                    mapping.get(page, page) if isinstance(page, str) else self.update_nav_structure(page, mapping)
                    for page in nav_obj['pages']
                ]
            for key, value in nav_obj.items():
                if key != 'pages':
                    nav_obj[key] = self.update_nav_structure(value, mapping)
        elif isinstance(nav_obj, list):
            nav_obj = [
                mapping.get(item, item) if isinstance(item, str) else self.update_nav_structure(item, mapping)
                for item in nav_obj
            ]

        return nav_obj

    def generate_report(self) -> None:
        """Generate a report of all changes."""
        report = {
            "total_changes": len(self.path_mapping),
            "changes": [
                {
                    "source": f"/{old_path}",
                    "destination": f"/{new_path}"
                }
                for old_path, new_path in sorted(self.path_mapping.items())
            ]
        }

        report_path = self.base_path / "id_removal_report.json"
        with open(report_path, 'w') as f:
            json.dump(report, f, indent=2)

        print(f"\nReport generated: {report_path}")
        print(f"Total changes: {len(self.path_mapping)}")

    def run(self) -> None:
        """Execute the full ID removal process."""
        print("Starting ID removal process...\n")

        print("Step 1: Building path mapping from docs.json...")
        self.build_path_mapping()

        print("Step 2: Renaming files and folders...")
        self.rename_files_and_folders()

        print("Step 3: Updating docs.json...")
        self.update_docs_json()

        print("Step 4: Generating report...")
        self.generate_report()

        print("\nID removal process completed successfully!")

if __name__ == "__main__":
    remover = IDRemover()
    remover.run()
