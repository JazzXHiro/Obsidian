---
cards-deck: 2 - Source Notes::Programming::C++::<% tp.file.title %>
tags:
---

# Flashcards for: <% tp.file.title %>

## I. Definitions & Purpose

What is the primary function of a comment in programming?
?
A **comment** is a programmer-readable note in the source code that is **ignored by the compiler**. It's used solely for the programmer’s documentation.

Which specific group are comments intended for?
?
They are for the **programmer's use only** (yourself or other developers).

## II. Syntax and Types

What symbol begins a C++ single-line comment?
::
`//`

What symbols denote a C-style multi-line comment?
::
They begin with `/*` and end with `*/`.

What is one crucial rule to remember when using multi-line comments?
?
**Don't use multi-line comments inside other multi-line comments** (they don't nest). Wrapping single-line comments inside a multi-line comment is okay.

## III. Proper Use of Comments

What are the three primary uses for comments, based on the **What, How, Why** model?
?
**1. What:** Describe *what* a library, program, or function does (at the top).
**2. How:** Describe *how* the code is going to accomplish its goal (within the body).
**3. Why:** Describe *why* the code is doing something (at the statement level).

At the *statement level*, should a good comment explain *what* or *why* the code is doing something?
::
**Why** the code is doing something.

## IV. Concepts

The player just drank a potion of blindness and can not see anything. :: // The player just drank a potion of blindness and can not see anything.
sight = 0;

**What makes this a *Good* statement-level comment?**
?
It explains the **reason** (*why*) the specific action (`sight = 0;`) is being performed, which is not obvious just by looking at the statement.

**What is the term for temporarily excluding code from being compiled by turning it into a comment?**
::
**Commenting out** your code.

Comments are a great way to remind yourself (or tell someone else) the reason you made a decision about **{{c1::how to solve a problem}}**.

What is [Doxygen](https://www.doxygen.nl/)?
?
A **documentation generation program** designed to standardize code documentation, generate diagrams, and export documentation to formats like HTML.