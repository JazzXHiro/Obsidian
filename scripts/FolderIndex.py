import os
import re
import sys

if len(sys.argv) < 2:
    print("Usage: python generate_index.py <folder_path>")
    sys.exit(1)

TARGET_FOLDER = sys.argv[1]
OUTPUT_FILE = os.path.join(TARGET_FOLDER, "INDEX.md")

heading_pattern = re.compile(r"^(#{1,6})\s+(.*)", re.MULTILINE)

lines = []
lines.append(f"# 📚 Index for `{TARGET_FOLDER}`\n")

for root, _, files in os.walk(TARGET_FOLDER):
    for file in files:
        if not file.endswith(".md"):
            continue
        if file == "INDEX.md":
            continue

        path = os.path.join(root, file)
        rel_path = os.path.relpath(path, TARGET_FOLDER)

        with open(path, "r", encoding="utf-8") as f:
            content = f.read()

        headings = heading_pattern.findall(content)
        if not headings:
            continue

        lines.append(f"## 📄 {file}\n")

        for hashes, text in headings:
            level = len(hashes)
            indent = "  " * (level - 1)
            lines.append(f"{indent}- [[{file}#{text}]]")

        lines.append("")

with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
    f.write("\n".join(lines))

print(f"✅ Index generated: {OUTPUT_FILE}")