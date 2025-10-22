---
# Templater will automatically fill this YAML block
anki-deck: {{name_of_your_deck}}  # Replace with the exact name of your Anki deck (e.g., C++ Fundamentals)
anki-tags: flashcard, <% tp.file.title %> # Uses the note's title as a tag for easy searching
---

# Flashcard: <% tp.file.title %>

---

## Front (Question)

What is a <% tp.file.title %>?
::

## Back (Answer)

The answer goes here.

---
What is a <% tp.file.title %>? :: The answer goes here.