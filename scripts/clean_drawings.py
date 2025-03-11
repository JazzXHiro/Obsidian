#!/usr/bin/env python3
import os
import re

# ================= Configuration ====================
# Set the absolute paths to your attachments folder and source notes folder.
ATTACHMENTS_FOLDER = "C:/Users/yadav/OneDrive/Obsidian/Jazz/Excalidraw"  # <-- Replace with your attachments folder path.
SOURCE_NOTES_FOLDER = "C:/Users/yadav/OneDrive/Obsidian/Jazz/2 - Source Notes"  # <-- Replace with your source notes folder path.
# ====================================================

def get_referenced_files(source_folder):
    """
    Recursively scan the source folder for markdown files and extract
    file references using Obsidian's [[filename]] linking syntax.
    If a link uses an alias (e.g., [[filename|alias]]), only the first part is taken.
    """
    referenced_files = set()
    # Regex captures text inside [[...]]; splits on the pipe if present.
    pattern = re.compile(r'\[\[([^|\]]+)(?:\|[^\]]+)?\]\]')
    
    for root, _, files in os.walk(source_folder):
        for file in files:
            if file.lower().endswith('.md'):
                filepath = os.path.join(root, file)
                try:
                    with open(filepath, 'r', encoding='utf-8') as f:
                        content = f.read()
                    # Find all matches in the file content
                    matches = pattern.findall(content)
                    for match in matches:
                        # Extract just the base filename in case a relative path is provided
                        base = os.path.basename(match.strip())
                        if base:  # Only add non-empty names
                            referenced_files.add(base)
                except Exception as e:
                    print(f"Error reading {filepath}: {e}")
    return referenced_files

def clean_attachments(attachments_folder, referenced_files):
    """
    List all files in the attachments folder and delete those
    that are not referenced in any note.
    """
    for file in os.listdir(attachments_folder):
        file_path = os.path.join(attachments_folder, file)
        # Only consider regular files (skip directories)
        if os.path.isfile(file_path):
            if file not in referenced_files:
                print(f"Deleting unreferenced file: {file_path}")
                try:
                    os.remove(file_path)
                except Exception as e:
                    print(f"Failed to delete {file_path}: {e}")
            else:
                print(f"Keeping referenced file: {file_path}")

def main():
    # Validate that provided paths are directories.
    if not os.path.isdir(ATTACHMENTS_FOLDER):
        print(f"Error: {ATTACHMENTS_FOLDER} is not a valid directory.")
        return
    if not os.path.isdir(SOURCE_NOTES_FOLDER):
        print(f"Error: {SOURCE_NOTES_FOLDER} is not a valid directory.")
        return

    print("Scanning source notes for referenced attachments...")
    referenced_files = get_referenced_files(SOURCE_NOTES_FOLDER)
    print(f"Found {len(referenced_files)} referenced file(s).")
    
    print("Cleaning attachments folder...")
    clean_attachments(ATTACHMENTS_FOLDER, referenced_files)
    print("Cleanup complete.")

if __name__ == '__main__':
    main()
