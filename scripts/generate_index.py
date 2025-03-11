import os
import re

# Define your Obsidian vault path
vault_path = "C:/Users/yadav/OneDrive/Obsidian/Jazz"  # Replace with your vault's folder path
index_folder = os.path.join(vault_path, "4 - Indexes")

# Create the index folder if it doesn't exist
os.makedirs(index_folder, exist_ok=True)

# Regex pattern to match tags of the format [[t-tag_name]]
tag_pattern = r"\[\[t-([a-zA-Z0-9_]+)\]\]"

# Find all unique tags in the vault
def find_all_tags():
    tags = set()
    for root, _, files in os.walk(vault_path):
        for file in files:
            if file.endswith(".md"):
                file_path = os.path.join(root, file)
                with open(file_path, "r", encoding="utf-8") as f:
                    content = f.read()
                    matches = re.findall(tag_pattern, content)
                    tags.update(matches)
    return tags
# [[t-]]
# Find files with a specific tag
def find_files_with_tag(tag):
    files_with_tag = []
    for root, _, files in os.walk(vault_path):
        for file in files:
            if file.endswith(".md"):
                file_path = os.path.join(root, file)
                with open(file_path, "r", encoding="utf-8") as f:
                    content = f.read()
                    if f"[[t-{tag}]]" in content:
                        files_with_tag.append(file)  # Only save the file name
    return files_with_tag

# Create or update the tag index file
def create_tag_index(tag, files):
    index_file_path = os.path.join(index_folder, f"t-{tag}.md")
    with open(index_file_path, "w", encoding="utf-8") as f:
        f.write(f"# Index for t-{tag}\n\n")
        f.write("## Files using this tag:\n")
        for i, file in enumerate(files, 1):
            f.write(f"{i}. [[{file}]]\n")
    print(f"Index file created: {index_file_path}")

# Run the script
all_tags = find_all_tags()
if all_tags:
    for tag in all_tags:
        files_with_tag = find_files_with_tag(tag)
        create_tag_index(tag, files_with_tag)
else:
    print("No tags of the format [[t-tag_name]] found.")
