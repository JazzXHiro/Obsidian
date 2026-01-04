	2026-01-04 17:16

Status: [[t-child]]

Tags: [[t-programming]] [[t-git]]

---
# git ignore

## 🧠 What `.gitignore` Does

**`.gitignore` tells Git which files and folders it should _NOT track_.**

In simple terms:

> “These files exist locally, but I don’t want them in my repository.”

Git will:

- Ignore changes in those files
    
- Never commit them
    
- Never push them to GitHub
    

---

## 🔍 Why `.gitignore` Is Necessary

Some files should **never** be pushed because they are:

- Auto-generated
    
- Machine-specific
    
- Temporary
    
- Large
    
- Sensitive (API keys, configs)
    

Examples:

- VS Code settings
    
- `node_modules/`
    
- Build files
    
- `.env` files
    

---

## 📁 Where `.gitignore` Lives

- Create a file named **`.gitignore`**
    
- Place it in the **root of your repository**
    

Example:

```
PortWeb/
├── .gitignore
├── index.html
├── css/
├── js/
└── img/
```

---

## ✍️ How to Use `.gitignore` (Basic Syntax)

Each line is a **pattern**.

### Ignore a file

```gitignore
info.txt
```

### Ignore a folder

```gitignore
node_modules/
```

### Ignore all files of a type

```gitignore
*.log
```

### Ignore VS Code settings

```gitignore
.vscode/
```

---

## 🧪 Common `.gitignore` for Your Portfolio Website

For your **HTML / CSS / JS project**, use this:

```gitignore
# OS files
.DS_Store
Thumbs.db

# Editor settings
.vscode/

# Temporary files
*.log

# Build or cache
dist/
```

✅ Safe  
✅ Clean  
✅ Professional

---

## ⚠️ Very Important Rule (Most Common Mistake)

> **`.gitignore` does NOT work on files already tracked.**

If you already committed a file:

- Adding it to `.gitignore` will NOT remove it
    

You must untrack it first.

---

## 🛠️ How to Stop Tracking an Already Tracked File

Example: you already committed `info.txt`

```bash
git rm --cached info.txt
```

Then:

```bash
git commit -m "Remove info.txt from tracking"
```

Now `.gitignore` will work for it.

---

## 🧠 How Git Decides What to Ignore

Order matters:

1. `.gitignore`
    
2. `.git/info/exclude`
    
3. Global ignore file
    

But for 99% of projects:

> `.gitignore` is enough.

---

## 🧠 Interview-Ready Explanation

> “A `.gitignore` file tells Git which files and directories to exclude from version control, typically for generated, local, or sensitive files.”

---
## 🧠 One-Line Rule

> **If a file is not part of the product, it should be in `.gitignore`.**

---

## 🔥 Pro Tip (GitHub Shortcut)

GitHub lets you generate `.gitignore` automatically:

- When creating a repo
    
- Choose template → “Node”, “VisualStudioCode”, etc.
    

---

## 🧠 Example `.gitignore` (Final)

```gitignore
# VS Code
.vscode/

# OS
.DS_Store
Thumbs.db

# Logs
*.log
```

---

If you want next, I can:

- Review your `.gitignore`
    
- Explain **git add vs git commit**
    
- Explain **tracked vs untracked files**
    
- Help you push your portfolio cleanly
    

Just say the next command.

---
# Reference
