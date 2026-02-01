
# Vortex: Modular Intelligent Game Library Management with Recommendation and Mood-Aware Personalization using Machine Learning Models

## 1. Core Idea
The project is a **lightweight, unified desktop game launcher** that brings games from multiple platforms (Steam, Epic, GOG, local installs, etc.) into a **single, clean interface**.  
The focus is on **performance, modularity, and user control**, avoiding the bloat seen in many modern launchers.

This is built with:
- **C++ as the core engine**
- **Qt/QML as the native UI layer** (preferred over React for performance)

---

## 2. MVP Philosophy (Important)
The initial goal is **only the shell / MVP**, not a polished final product.

MVP includes:
- Basic UI layout
- Game library view
- Game launch (or mock launch)
- Playtime tracking (basic)
- Settings with feature toggles

No heavy optimization, no edge-case handling, no feature overload in Phase 1.

---

## 3. Architecture Overview

### Backend (C++)
- Game library indexing
- Process monitoring & playtime tracking
- Metadata handling
- Local database (SQLite)
- Module management (enable/disable features)
- System-level APIs for launching games

### UI Layer (QML)
- Native, GPU-accelerated UI
- Low memory usage
- Fast startup
- Tight integration with C++

**Why not React?**
- React (Electron/WebView) uses significantly more RAM
- Higher CPU usage
- Background overhead
- Goes against the “lightweight, no-bloat” goal

---

## 4. Modular Design (Anti-Bloat Strategy)
All extra features are **optional modules**:
- Game guides
- Trailers
- Release tracking
- Forums / links
- System requirement checker
- Analytics

If a module is disabled:
- UI component disappears
- Backend logic is unloaded

This allows:
- Minimalist mode for casual users
- Power-user mode for advanced users

---

## 5. Data Structures Usage
The project is **heavily data-structure-driven** (real-world usage, not artificial).

Examples:
- `unordered_map` → fast game lookup by ID
- `vector` → sorted views (by playtime, name, last played)
- `set / multimap` → ordered stats
- `deque` → recent play sessions
- Caching structures (LRU cache)
- Optional `Trie` for fast search

This makes the project strong for **DS (Data Structures)** and **DAA justification**.

---

## 6. Is This a Data Science Project?
### By default:
- Not a Data Science project
- Software Engineering + Systems + Data Structures

The base launcher:
- Collects data
- Stores data
- Displays data  
This is **data handling**, not data science.

---

## 7. Making It Data Science / AI-Valid
The project becomes **legit Data Science / AI** if an **AI-based recommender system** is added.

### AI Feature: Game Recommendation System
- Suggests games based on:
  - Previously played games
  - Liked/disliked games
  - Genres
  - Playtime patterns
  - Session length
  - Time of day

### Mood / Persona-Based Recommendations
- Infer moods such as:
  - Relaxed
  - Competitive
  - Story-driven
  - Short-session
- Use clustering or classification models to infer mood/persona from behavior.

### Models That Count Academically
- Content-based filtering
- Collaborative filtering
- KNN similarity
- Clustering (K-means)
- Simple ML models with training & evaluation

### What Makes It “Real” Data Science
- Dataset (user data + public game metadata)
- Feature extraction
- Model training
- Evaluation metrics (Precision@K, Recall, RMSE, etc.)
- Comparison with a baseline (rule-based vs ML)

Rule-based logic alone does **not** count as AI/DS.

---

## 8. Final Project Nature
Without AI:
- **Software Engineering + Systems + Data Structures**

With AI recommender:
- **Hybrid Project**
  - Software Engineering
  - Applied Data Science
  - Recommender Systems
  - User Behavior Analysis

This significantly increases academic value and viva credibility.

---

## 9. Sample Project Titles

### Standard Academic
**Atlas: Unified Game Library Management and Playtime Analytics using a Native C++ Engine**

**Atlas: Intelligent Game Recommendation and Mood-Aware Personalization using Machine Learning Models**

### Outcome-Oriented
**Optimizing Game Access and Usage Analytics via a Modular Native Desktop Launcher**

**Personalizing Game Recommendations based on User Behavior and Mood using Hybrid Recommender Systems**