	2026-01-03 20:15

Status: [[t-child]]

Tags: [[t-project]] [[t-programming]] [[t-webdev]]

---
# Utilized Tech Stack

1. **HTML**
2. **CSS**
3. **JavaScript**

# Details

Think of **HTML, CSS, and JavaScript** as a **layered system**, not three random tools.

## 🧱 The Core Web Tech Stack (Foundation of the Web)

```
┌───────────────┐
│   JavaScript  │  ← Logic, behavior, interactivity
├───────────────┤
│      CSS      │  ← Design, layout, responsiveness
├───────────────┤
│      HTML     │  ← Structure, content, semantics
└───────────────┘
```

Every modern framework (React, Angular, Vue) is **built on top of this**.

---

### 🟧 HTML (HyperText Markup Language)

#### 🔹 What HTML Is

HTML defines the **structure and meaning** of a webpage.

It answers:

- What is a heading?
    
- What is a paragraph?
    
- What is a navigation bar?
    
- What is a form?
    

HTML is **not a programming language**.  
It is a **markup language**.

---

#### 🔹 What HTML Does

- Defines content layout
    
- Gives semantic meaning
    
- Helps SEO and accessibility
    
- Acts as the DOM skeleton
    

Example:

```html
<header>
  <nav>
    <h1>Ishu Yadav</h1>
  </nav>
</header>
```

---

#### 🔹 Key HTML Concepts (Interview Level)

- Semantic tags: `<header> <nav> <main> <section> <article> <footer>`
    
- Attributes: `id`, `class`, `src`, `href`
    
- Forms & inputs
    
- Accessibility basics (`alt`, `label`)
    

---

#### 🔹 Why HTML Matters

Bad HTML =  
❌ Poor SEO  
❌ Accessibility issues  
❌ Messy JS later

Good HTML =  
✔ Clean structure  
✔ Easier styling  
✔ Easier scripting

---

### 🟦 CSS (Cascading Style Sheets)

#### 🔹 What CSS Is

CSS controls **how things look and where they appear**.

It answers:

- Colors?
    
- Fonts?
    
- Spacing?
    
- Layout?
    
- Responsiveness?
    

---

#### 🔹 What CSS Does

- Styling (colors, fonts)
    
- Layout (Flexbox, Grid)
    
- Animations & transitions
    
- Responsive design
    

Example:

```css
.card {
  padding: 1rem;
  border-radius: 8px;
  background-color: #020617;
}
```

---

#### 🔹 Modern CSS You Should Know

- Flexbox → 1D layouts
    
- Grid → 2D layouts
    
- Media queries → responsiveness
    
- Variables (`:root`)
    
- Transitions & animations
    

Example:

```css
@media (max-width: 768px) {
  .nav {
    flex-direction: column;
  }
}
```

---

#### 🔹 Why CSS Is Important

Recruiters **do judge UI**.

Good CSS shows:  
✔ Attention to detail  
✔ UX awareness  
✔ Professional polish

Bad CSS screams:  
❌ Tutorial clone  
❌ Weak frontend sense

---

### 🟨 JavaScript (The Brain)

#### 🔹 What JavaScript Is

JavaScript is a **programming language** that controls **behavior and logic**.

It answers:

- What happens on click?
    
- How does data change?
    
- When does UI update?
    
- How do components interact?
    

---

#### 🔹 What JavaScript Does

- DOM manipulation
    
- Event handling
    
- State management
    
- API calls
    
- Logic & conditions
    

Example:

```js
button.addEventListener("click", () => {
  count++;
  display.textContent = count;
});
```

---

#### 🔹 Core JavaScript Concepts (Must-Know)

- Variables (`let`, `const`)
    
- Functions
    
- Loops & conditionals
    
- DOM (`document.querySelector`)
    
- Events
    
- Arrays & objects
    

Advanced (nice to have):

- Closures
    
- Promises
    
- Async / Await
    
- Event delegation
    

---

#### 🔹 Why JavaScript Is Critical

Without JS:

- No interactivity
    
- No logic
    
- Static pages only
    

With JS:  
✔ Dynamic UI  
✔ Real applications  
✔ Framework readiness

---

### 🔁 How They Work Together (Very Important)

Example: Button click

#### HTML

```html
<button id="btn">Click</button>
```

#### CSS

```css
button {
  background: blue;
}
```

#### JavaScript

```js
document.getElementById("btn").onclick = () => {
  alert("Clicked!");
};
```

Each layer has **one responsibility**.

This separation is **software engineering discipline**.

---

### 🎯 Why This Stack Is Resume-Worthy

Using **HTML + CSS + JS** correctly shows:

- Strong fundamentals
    
- No framework dependency
    
- Understanding of the browser
    
- Readiness for React / Angular
    

In interviews, you can say:

> “Frameworks come and go, but HTML, CSS, and JavaScript are permanent.”

That’s a **strong statement**.

---

### 🧠 When to Move Beyond This Stack

You switch to React or other frameworks when:

- UI grows complex
    
- Components repeat
    
- State management becomes messy
    

Until then:

> Vanilla stack = **engineering discipline**

---

### 🧩 Summary (One-Glance)

| Tech       | Role                  |
| ---------- | --------------------- |
| HTML       | Structure & semantics |
| CSS        | Design & layout       |
| JavaScript | Logic & interactivity |


---
# Reference
