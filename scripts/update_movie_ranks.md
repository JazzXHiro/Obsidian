<%*
const editor = app.workspace.getActiveViewOfType(MarkdownView)?.editor;
if (!editor) return;

const text = editor.getValue();
const lines = text.split("\n");

// Find table
let start = -1;
let end = -1;

for (let i = 0; i < lines.length; i++) {
  if (lines[i].startsWith("|") && start === -1) start = i;
  if (start !== -1 && i > start && !lines[i].startsWith("|")) {
    end = i;
    break;
  }
}
if (start === -1) return;
if (end === -1) end = lines.length;

const table = lines.slice(start, end);

// Header + separator stay untouched
let rank = 1;
for (let i = 2; i < table.length; i++) {
  const cols = table[i].split("|");
  if (cols.length > 2) {
    cols[1] = ` ${rank} `;
    rank++;
    table[i] = cols.join("|");
  }
}

lines.splice(start, end - start, ...table);
editor.setValue(lines.join("\n"));
%>
