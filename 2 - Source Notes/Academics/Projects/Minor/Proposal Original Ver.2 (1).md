Here's the completed proposal:

---

## Project Title: Vortex: A Unified Intelligent Game Library/Launcher

**Domain:** Intelligent Systems & Software Engineering

**Proposed By:** 
- Keerti Vardhan
- Yuvraj Bhardwaj
- Ayushmaan Kapruwan
- Aditya Kediyal

---

### 1. Abstract

Vortex is a unified game library management application with an intelligent recommendation system. The app detects games from multiple platforms into a single interface & also tracks playtime, session patterns, and user preferences. 

Built using C++ and Qt/QML for performance, Vortex implements a machine learning-based recommendation engine that uses content-based filtering and mood-aware personalization. The system analyses user behavior like play duration, time-of-day patterns, and explicit ratings to generate relevant game suggestions.  
A modular architecture allows users to customize features according to their needs, avoiding the bloat common in existing launchers. The project demonstrates practical application of recommender systems, data pipeline design, and native software development.  

Keywords: Game Library Management, Recommender Systems, Mood-Aware, Personalization, Desktop Application, Machine Learning

---

### 2. Introduction

#### Background

Digital game distribution has evolved significantly over the past decade. Users now own games across Steam, Epic Games Store, GOG, Xbox Game Pass, and other platforms. Each platform maintains its own launcher, library interface, and usage statistics, creating a fragmented experience for gamers who must switch between multiple applications.

#### Problem Statement

Current game launchers operate in isolation, offering no unified view of a user's complete game collection. Playtime data remains siloed, making it impossible to analyze overall gaming habits. Existing recommendation systems rely primarily on purchase history and popularity metrics rather than actual user behavior and contextual factors like mood or available time.

#### Motivation

Our users deserve a single application that:
- Aggregates all their games regardless of platform
- Provides meaningful insights into their gaming habits
- Recommends games based on current mood and context, not just past purchases

The rise of subscription services (Game Pass, EA Play) has further increased library sizes, making intelligent organization and recommendation more valuable than ever.

---

### 3. Literature Review

#### Existing Solutions

| Solution           | Description                        | Limitations                                     |
| ------------------ | ---------------------------------- | ----------------------------------------------- |
| **Playnite**       | Open-source unified game library   | No ML-based recommendations, basic UI           |
| **GOG Galaxy 2.0** | Multi-platform library aggregation | Limited personalization, no mood-aware features |
| **Steam**          | Largest PC game platform           | Single platform only, generic recommendations   |
| **LaunchBox**      | Game organization and emulation    | Focus on retro games, no behavior analytics     |

#### Academic Background

Content-based filtering and collaborative filtering are established techniques in recommender systems. Netflix, Spotify, and YouTube employ hybrid approaches combining multiple models. Context-aware recommendation systems that consider time, location, and user state have shown improved user satisfaction in research studies.

#### Gap Analysis

| Gap | Description |
|-----|-------------|
| **No Unified Analytics** | Existing launchers don't combine playtime data across platforms |
| **Static Recommendations** | Suggestions don't adapt to time-of-day or session patterns |
| **Resource Heavy** | Most launchers consume significant system resources |
| **No Mood Inference** | No system considers user's current gaming mood |

---

### 4. Objectives and Scope

#### Primary Objectives

1. **Unified Library Management** — Aggregate games from multiple sources into a single, searchable interface

2. **Intelligent Playtime Tracking** — Monitor session duration, time-of-day patterns, and engagement metrics

3. **ML-Powered Recommendations** — Implement content-based filtering with mood-aware adjustments

4. **Lightweight Modular Design** — Create a performant application where features can be toggled on/off

#### Scope

| In Scope                      | Out of Scope                                       |
| ----------------------------- | -------------------------------------------------- |
| Manual game addition          | Auto-detection from all platforms                  |
| Local playtime tracking       | Cloud sync across devices                          |
| Content-based recommendations | Collaborative filtering (requires multi-user data) |
| Basic mood inference          | Advanced emotion detection                         |
| Windows support               | Mac/Linux support (future work)                    |
| Like/Dislike preferences      | Social features, friend lists                      |

---

### 5. Methodology

#### Architecture Overview

```
┌─────────────────────────────────────────────────────────────────┐
│                        VORTEX ARCHITECTURE                      │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│   ┌─────────────┐     ┌─────────────┐     ┌─────────────┐       │
│   │   QML UI    │◄───►│   C++ Core  │◄───►│   SQLite    │       │
│   │  (Frontend) │     │  (Backend)  │     │    (Data)   │       │
│   └─────────────┘     └──────┬──────┘     └──────┬──────┘       │
│                              │                   │              │
│                              ▼                   ▼              │
│                       ┌─────────────────────────────┐           │
│                       │     Python ML Module        │           │
│                       │  (Recommendations Engine)   │           │
│                       └─────────────────────────────┘           │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

#### Technology Stack

| Category | Technology | Justification |
|----------|------------|---------------|
| Core Language | C++17 | Performance, system access |
| UI Framework | Qt 6 / QML | Native performance, cross-platform potential |
| Database | SQLite | Lightweight, local storage, no server needed |
| ML Language | Python 3.10+ | Rich ML ecosystem, rapid prototyping |
| ML Libraries | scikit-learn, pandas, numpy | Industry standard, well-documented |
| Build System | CMake | Cross-platform build management |

#### ML Approach [1]
[[]]

| Model | Purpose | Technique |
|-------|---------|-----------|
| **Content-Based Filter** | Game similarity | TF-IDF vectorization + Cosine similarity on genres/themes |
| **Mood Classifier** | Context inference | Rule-based heuristics + Decision tree on temporal features |
| **Hybrid Ranker** | Final recommendations | Weighted combination of content score + mood adjustment |

#### Feature Engineering Pipeline

```
Raw Data → Session Logs → Feature Extraction → User Vectors → ML Models → Recommendations
              │
              ├── Playtime (total, average, variance)
              ├── Session patterns (length, frequency)
              ├── Temporal signals (hour, weekday/weekend)
              └── Explicit preferences (likes, dislikes)
```

---

### 6. System Design

#### System Workflow

```
┌─────────────────────────────────────────────────────────────────┐
│                       USER WORKFLOW                              │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  ┌──────────┐    ┌──────────┐    ┌──────────┐    ┌──────────┐   │
│  │  Add     │───►│  Play    │───►│  Track   │───►│  Get     │   │
│  │  Games   │    │  Game    │    │  Session │    │  Recs    │   │
│  └──────────┘    └──────────┘    └──────────┘    └──────────┘   │
│       │              │               │               │          │
│       ▼              ▼               ▼               ▼          │
│  ┌──────────┐    ┌──────────┐    ┌──────────┐    ┌──────────┐   │
│  │ Library  │    │ Launcher │    │  Data    │    │   ML     │   │
│  │ Manager  │    │ Service  │    │ Pipeline │    │  Engine  │   │
│  └──────────┘    └──────────┘    └──────────┘    └──────────┘   │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

#### Data Flow

| Stage      | Input           | Process                         | Output                 |
| ---------- | --------------- | ------------------------------- | ---------------------- |
| Collection | User actions    | Event capture                   | Raw events             |
| Storage    | Raw events      | Validation, storage             | SQLite records         |
| Processing | SQLite records  | Aggregation, feature extraction | Feature vectors        |
| Inference  | Feature vectors | ML model prediction             | Ranked recommendations |
| Display    | Recommendations | UI rendering                    | User sees suggestions  |

### Data Types


| **Category** | **Data Item**     | **Used in Launcher** | **Used for ML Recommendation** | **Notes**                |
| ------------ | ----------------- | -------------------- | ------------------------------ | ------------------------ |
| Local Data   | Game Name         | No                   | No                             | Basic Identifier         |
| Local Data   | Version           | No                   | No                             | For compatibility checks |
| Local Data   | Install Directory | No                   | No                             | System reference only    |
| Local Data   | Genre/Tags        | No                   | No                             |                          |


#### User Personas

| Persona           | Description                                   | Primary Need                              |
| ----------------- | --------------------------------------------- | ----------------------------------------- |
| **Casual Gamer**  | Plays occasionally, owns 20-50 games          | Quick game selection, simple interface    |
| **Enthusiast**    | Plays daily, owns 100+ games across platforms | Unified library, playtime stats           |
| **Completionist** | Tracks achievements, completion rates         | Progress tracking, similar game discovery |

---

### 7. Feasibility and Risk Analysis

#### Technical Feasibility

| Aspect      | Assessment | Details                                           |
| ----------- | ---------- | ------------------------------------------------- |
| Team Skills | Feasible   | C++, Python, Qt knowledge present in team         |
| Hardware    | Feasible   | Standard development machines sufficient          |
| Software    | Feasible   | All tools are free/open-source                    |
| Timeline    | Feasible   | 10-12 weeks requires disciplined scope management |

#### Risk Analysis

| Risk | Probability | Impact | Mitigation |
|------|-------------|--------|------------|
| Platform API limitations | Medium | High | Focus on manual game addition for MVP |
| ML model accuracy issues | Medium | Medium | Start with simple models, iterate |
| Integration complexity (C++↔Python) | Medium | Medium | Use JSON file-based communication initially |
| Scope creep | High | High | Strict MVP definition, feature freezes |
| Team coordination issues | Low | Medium | Weekly syncs, clear role ownership |

---

### 8. Project Timeline

```
┌──────────────────────────────────────────────────────────────────────────────
│                           12-WEEK PROJECT TIMELINE                           │
├──────────────────────────────────────────────────────────────────────────────
│                                                                              │
│  PHASE 1: FOUNDATION (Weeks 1-3)                                             │
│  ├── Week 1: Requirements finalization, environment setup                    │
│  ├── Week 2: Database schema design, project structure                       │
│  └── Week 3: Basic UI shell, core data models                                │
│                                                                              │
│  PHASE 2: CORE DEVELOPMENT (Weeks 4-7)                                       │
│  ├── Week 4: Game library manager, add/edit/delete games                     │
│  ├── Week 5: Session tracking, playtime logging                              │
│  ├── Week 6: Like/Dislike system, preference storage                         │
│  └── Week 7: Python ML module setup, feature extraction                      │
│                                                                              │
│  PHASE 3: ML INTEGRATION (Weeks 8-10)                                        │
│  ├── Week 8: Content-based recommendation model                              │
│  ├── Week 9: Mood inference module                                           │
│  └── Week 10: C++↔Python integration, recommendation display                 │
│                                                                              │
│  PHASE 4: FINALIZATION (Weeks 11-12)                                         │
│  ├── Week 11: Testing, bug fixes, evaluation metrics                         │
│  └── Week 12: Documentation, presentation, viva preparation                  │
│                                                                              │
└──────────────────────────────────────────────────────────────────────────────
```

#### Gantt Chart

| Task | W1 | W2 | W3 | W4 | W5 | W6 | W7 | W8 | W9 | W10 | W11 | W12 |
|------|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:---:|:---:|:---:|
| Requirements & Setup | ██ | ██ | | | | | | | | | | |
| Database Design | | ██ | ██ | | | | | | | | | |
| UI Development | | | ██ | ██ | ██ | ██ | | | | | | |
| Backend Core | | | ██ | ██ | ██ | ██ | | | | | | |
| Data Pipeline | | | | | ██ | ██ | ██ | | | | | |
| ML Development | | | | | | | ██ | ██ | ██ | | | |
| Integration | | | | | | | | | ██ | ██ | | |
| Testing | | | | | | | | | | ██ | ██ | |
| Documentation | | | | | | | | | | | ██ | ██ |

#### PERT Chart

![[image-3.png|827x208]]

---

### 9. Expected Outcomes

#### Deliverables

| Deliverable | Description |
|-------------|-------------|
| **Vortex Application** | Functional Windows desktop application with unified game library |
| **ML Recommendation Engine** | Python module providing content-based + mood-aware recommendations |
| **Project Report** | Comprehensive documentation including architecture, methodology, results |
| **User Manual** | Guide for installation and usage |
| **Source Code** | Well-documented codebase on GitHub |

#### Success Metrics

| Metric | Target |
|--------|--------|
| Recommendation Precision@5 | > 60% |
| Application Startup Time | < 3 seconds |
| Memory Usage | < 200 MB |
| User Satisfaction (internal testing) | > 7/10 |

#### Academic Contributions

1. Demonstration of mood-aware recommendation in gaming context
2. Practical implementation of hybrid ML pipeline in native application
3. Modular architecture pattern for feature-rich desktop applications

---

## 10. References

1. M. Kozakov and N. Kozakova, “DEVELOPMENT OF A RECOMMENDATION SYSTEM FOR VIDEO GAMES”, GoS, no. 58, pp. 814–819, Nov. 2025. 

2. 

3. 

4. 

5. 

---

### Team Responsibilities

| Member                 | Role                            | Primary Responsibilities         |
| ---------------------- | ------------------------------- | -------------------------------- |
| **Keerti Vardhan**     | Backend & Systems Developer     |                                  |
| **Yuvraj Bhardwaj**    | ML & Algorithm Developer        |                                  |
| **Ayushmaan Kapruwan** | Frontend & UI Developer         | Design & Implement UI components |
| **Aditya Kediyal**     | Database & Integration Engineer |                                  |

---

*Proposal submitted for Minor Project evaluation.*