#!/usr/bin/env python3
import os
import re

# ================= Configuration ====================
# Set the absolute paths to your Excalidraw drawings folder and source notes folder.
EXCALIDRAW_FOLDER = "C:/Users/yadav/OneDrive/Obsidian/Jazz/Excalidraw"  # <-- Replace with your Excalidraw drawings folder path.
SOURCE_NOTES_FOLDER = "C:/Users/yadav/OneDrive/Obsidian/Jazz/2 - Source Notes"         # <-- Replace with your source notes folder path.
# ====================================================

def get_referenced_drawings(source_folder):
    """
    Recursively scan the source folder for markdown files and extract
    file references using Obsidian's [[filename]] linking syntax.
    
    For Excalidraw drawings, if a link doesn't explicitly include the
    '.excalidraw' extension, it is automatically appended.
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
                        # Get just the base filename in case a relative path is provided
                        base = os.path.basename(match.strip())
                        if base:
                            # If the reference doesn't end with '.excalidraw', assume it refers to an Excalidraw drawing.
                            if not base.lower().endswith('.excalidraw'):
                                base += ".excalidraw"
                            referenced_files.add(base)
                except Exception as e:
                    print(f"Error reading {filepath}: {e}")
    return referenced_files

def clean_excalidraw_drawings(drawings_folder, referenced_files):
    """
    List all files in the Excalidraw drawings folder and delete those
    that are not referenced in any note.
    """
    for file in os.listdir(drawings_folder):
        file_path = os.path.join(drawings_folder, file)
        # Only consider regular files (skip directories)
        if os.path.isfile(file_path):
            if file not in referenced_files:
                print(f"Deleting unreferenced drawing: {file_path}")
                try:
                    os.remove(file_path)
                except Exception as e:
                    print(f"Failed to delete {file_path}: {e}")
            else:
                print(f"Keeping referenced drawing: {file_path}")

def main():
    # Validate that provided paths are directories.
    if not os.path.isdir(EXCALIDRAW_FOLDER):
        print(f"Error: {EXCALIDRAW_FOLDER} is not a valid directory.")
        return
    if not os.path.isdir(SOURCE_NOTES_FOLDER):
        print(f"Error: {SOURCE_NOTES_FOLDER} is not a valid directory.")
        return

    print("Scanning source notes for referenced Excalidraw drawings...")
    referenced_files = get_referenced_drawings(SOURCE_NOTES_FOLDER)
    print(f"Found {len(referenced_files)} referenced drawing file(s).")
    
    print("Cleaning Excalidraw drawings folder...")
    clean_excalidraw_drawings(EXCALIDRAW_FOLDER, referenced_files)
    print("Cleanup complete.")

if __name__ == '__main__':
    main()
