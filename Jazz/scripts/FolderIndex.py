import os
import re
import sys

# ---------------- CONFIG ----------------

if len(sys.argv) < 2:
    print("Usage: python generate_index.py <folder_path>")
    input("Press Enter to exit...")
    sys.exit(1)

TARGET_FOLDER = sys.argv[1]
OUTPUT_FILE = os.path.join(TARGET_FOLDER, "INDEX.md")

# Match markdown headings
HEADING_PATTERN = re.compile(r"^(#{1,6})\s+(.*)", re.MULTILINE)

# ---------------- SAFE FILE READER ----------------

def safe_read(path):
    """
    Reads a file safely regardless of encoding.
    Tries UTF-8 first, falls back to latin-1.
    """
    try:
        with open(path, "r", encoding="utf-8") as f:
            return f.read()
    except UnicodeDecodeError:
        with open(path, "r", encoding="latin-1", errors="ignore") as f:
            return f.read()

# ---------------- MAIN LOGIC ----------------

lines = []
lines.append(f"# 📚 Index for `{TARGET_FOLDER}`\n")

for root, _, files in os.walk(TARGET_FOLDER):
    for file in files:
        if not file.endswith(".md"):
            continue
        if file == "INDEX.md":
            continue

        path = os.path.join(root, file)
        content = safe_read(path)

        headings = HEADING_PATTERN.findall(content)
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

print(f"✅ Index generated successfully!")
print(f"📄 Location: {OUTPUT_FILE}")
input("\nPress Enter to exit...")