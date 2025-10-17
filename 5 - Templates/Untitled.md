---
# 🧠 Flashcards Note Template
# Automatically uses the note title as the deck name (via plugin settings)
# ⚙️ Make sure "Use note title as deck name (if no deck specified)" is enabled in plugin settings.

cards-deck: <% tp.file.title %>
tags: [flashcards]
created: <% tp.date.now("YYYY-MM-DD") %>
---

# <% tp.file.title %>

---

## 📝 Notes
Add your study notes or concepts here.

---

## 🃏 Flashcards

**Q:** What is <% tp.file.title %>?  
**A:** (Your answer here)

---

**Q:** (Next question)  
**A:** (Next answer)

---

> 💡 Tip: Use `---` between flashcards and `**Q:**` / `**A:**` format for easy export to Anki.
