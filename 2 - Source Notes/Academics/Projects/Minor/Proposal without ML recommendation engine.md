# Vortex: A Unified Intelligent Game Library & Launcher

Domain: Software Engineering & Intelligent Systems  

Proposed By:  
- Keerti Vardhan  
- Yuvraj Bhardwaj  
- Ayushmaan Kapruwan  
- Aditya Kediyal  

---

## Terminologies Used

1. Platforms – Game distribution platforms where users purchase or access games.  
2. Launcher – An application that manages and launches installed game executables.  
3. Playtime Tracking – Monitoring total and session-wise duration of gameplay.  
4. Session Analytics – Analysis of usage patterns such as session length and play frequency.

---

## 1. Abstract

Vortex is a unified desktop game library and launcher designed to aggregate games from multiple platforms into a single, lightweight interface. The application automatically detects installed games, launches them from one place, and tracks playtime and session statistics locally.

Built using C++ and Qt/QML, Vortex focuses on performance, modularity, and low resource consumption. The system records gameplay sessions, analyzes temporal usage patterns, and presents meaningful insights to users through a clean and minimal UI.  
By avoiding unnecessary background services and cloud dependencies, Vortex offers a privacy-friendly and efficient alternative to existing game launchers.

Keywords: Game Library Management, Desktop Application, Playtime Tracking, Software Engineering, System Design

---

## 2. Introduction

### Background

Modern gamers often own titles across multiple platforms such as Steam, GOG, Epic Games Store, and Xbox Game Pass. Each platform uses its own launcher, resulting in fragmented libraries and inconsistent tracking of playtime and usage data.

### Problem Statement

Existing game launchers:
- Operate independently without a unified library view  
- Track playtime only within their own ecosystem  
- Require multiple applications to manage different games  
- Consume significant system resources

This leads to inefficiency, poor usability, and fragmented analytics for users with large game collections.

### Motivation

The motivation behind Vortex is to:
- Centralize game management across platforms  
- Provide consistent playtime and session analytics  
- Reduce launcher clutter and resource usage
- Improve user experience with a single interface  

---

## 3. Literature Review

### Existing Solutions

| Solution       | Description                       | Limitations                  |
| -------------- | --------------------------------- | ---------------------------- |
| Playnite       | Open-source unified game launcher | Limited analytics, basic UI  |
| GOG Galaxy 2.0 | Multi-platform aggregation        | Heavy resource usage         |
| Steam          | Single-platform launcher          | No cross-platform visibility |

### Gap Analysis

| Gap | Description |
|----|-------------|
| Unified Library | No lightweight all-in-one solution |
| Cross-Platform Analytics | Playtime data remains siloed |
| Performance | Existing launchers are resource intensive |
| Modularity | Limited user control over features |

---

## 4. Objectives and Scope

### Primary Objectives

##### 1. Unified Game Library  -
   Aggregate games from multiple platforms into a single interface.

##### 2. Centralized Launcher  -
   Launch any installed game from one application.

##### 3. Playtime & Session Tracking  -
   Track total playtime, session duration, and usage frequency.

##### 4. Lightweight Modular Design  -
   Ensure low memory usage and high responsiveness.

---

### Scope

| In Scope | Out of Scope |
|--------|--------------|
| Game detection from supported platforms | Cloud synchronization |
| Local playtime tracking | Recommendation systems |
| Session analytics | Social features |
| Windows OS support | Linux/macOS (future work) |

**Supported platforms (initial):** Steam, GOG

---

## 5. Methodology

### Architecture Overview

```
┌──────────────────────────────────────────────┐
│              VORTEX ARCHITECTURE             │
├──────────────────────────────────────────────┤
│                                              │
│  ┌─────────────┐     ┌─────────────┐         │
│  │   QML UI    │◄───►│   C++ Core  │         │
│  │ (Frontend)  │     │ (Backend)   │         │
│  └─────────────┘     └──────┬──────┘         │
│                             │                │
│                             ▼                │
│                      ┌─────────────┐         │
│                      │   SQLite    │         │
│                      │ (Local DB)  │         │
│                      └─────────────┘         │
│                                              │
└──────────────────────────────────────────────┘

```


---

### Technology Stack

| Category | Technology | Justification |
|-------|-----------|--------------|
| Core Language | C++17 | High performance and system access |
| UI Framework | Qt 6 / QML | Native desktop UI |
| Database | SQLite | Lightweight local storage |
| Build System | CMake | Cross-platform build support |

---

### Session Analytics Pipeline

```
Game Launch
   ↓
Session Start Timestamp
   ↓
Game Exit
   ↓
Session Duration Calculation
   ↓
Local Storage (SQLite)
   ↓
Analytics Visualization

```

**Tracked Metrics:**
- Total playtime per game  
- Average session duration  
- Daily and weekly usage trends  
- Peak play hours  

---

## 6. System Design

### User Workflow

```
┌──────────┐ → ┌──────────┐ → ┌──────────┐ → ┌──────────┐
│ Add Game │   │ Launch   │   │ Track    │   │ View     │
│ Library  │   │ Game     │   │ Session  │   │ Stats    │
└──────────┘   └──────────┘   └──────────┘   └──────────┘

```

---

### Data Flow

| Stage | Input | Process | Output |
|-----|------|--------|-------|
| Detection | Installed games | Metadata extraction | Game list |
| Execution | User action | Launch monitoring | Session logs |
| Storage | Logs | Validation | SQLite records |
| Analysis | Records | Aggregation | Analytics |
| Display | Analytics | UI rendering | User insights |

#### Data Usage and Utilization

| **Category**       | **Data Item**           | **Used in Launcher** |
| ------------------ | ----------------------- | -------------------- |
| Local Data         | Game Name               | Yes                  |
| Local Data         | Version                 | Yes                  |
| Local Data         | Install Directory       | Yes                  |
| IGDB (External DB) | Genre/Tags              | Yes                  |
| IGDB (External DB) | Images                  | Yes                  |
| IGDB (External DB) | Game Length             | Yes                  |
| IGDB (External DB) | Developer/Publisher     | Yes                  |
| IGDB (External DB) | Ratings/Reviews         | Yes                  |
| Produced Data      | Session Start/End       | Yes                  |
| Produced Data      | Idle/ Inactive duration | Yes                  |
| Produced Data      | Session length          | Yes                  |
| Produced Data      | Liked/Disliked Games    | Yes                  |
| Distribution API   | In-game Achievements    | Yes                  |

---

## 7. Feasibility and Risk Analysis

### Technical Feasibility

| Aspect | Assessment |
|------|------------|
| Team Skills | Feasible |
| Hardware | Feasible |
| Software | Feasible |
| Timeline | Feasible |

---

### Risk Analysis

| Risk | Probability | Impact | Mitigation |
|----|-------------|--------|-----------|
| Platform API changes | Medium | Medium | Manual fallback |
| Scope creep | High | High | Strict MVP definition |
| Integration issues | Medium | Medium | Incremental testing |

---

## 8. Project Timeline
  
### Gantt Chart

| Task                         | W1  | W2  | W3  | W4  | W5  | W6  | W7  | W8  | W9  | W10 | W11 | W12 |
| ---------------------------- | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: |
| Requirements & Setup         | ██  | ██  |     |     |     |     |     |     |     |     |     |     |
| Database Design              |     | ██  | ██  | ██  |     |     |     |     |     |     |     |     |
| UI Development               |     |     | ██  | ██  | ██  | ██  |     |     |     |     |     |     |
| Backend Core                 |     |     | ██  | ██  | ██  | ██  |     |     |     |     |     |     |
| Session & Tracking Analytics |     |     |     |     | ██  | ██  | ██  | ██  |     |     |     |     |
| Integration                  |     |     |     |     |     |     | ██  | ██  | ██  | ██  |     |     |
| Testing                      |     |     |     |     |     |     |     |     | ██  | ██  | ██  |     |
| Documentation                |     |     |     |     |     |     |     |     |     |     | ██  | ██  |

### PERT Chart

![[image-4.png]]

---

## 9. Expected Outcomes

### Deliverables

| Deliverable | Description |
|-----------|-------------|
| Vortex Application | Unified game launcher |
| Analytics Module | Playtime & session statistics |
| Project Report | Complete technical documentation |
| Source Code | Well-documented repository |

---

### Success Metrics

| Metric                   | Target |
| ------------------------ | ------ |
| Application startup time |        |
| Memory usage             |        |
| Tracking accuracy        |        |
| User satisfaction        | > 7/10 |

---

## 10. References

1. https://api.playnite.link/docs/manual/gettingStarted/gettingStartedOverview.html  
2. https://docs.gog.com/quick-start/  
3. https://partner.steamgames.com/doc/home  
4. https://www.igdb.com/api

---

## Team Responsibilities

| Member | Role |
|------|-----|
| Keerti Vardhan | Backend & Systems Developer |
| Yuvraj Bhardwaj | Core Logic Developer |
| Ayushmaan Kapruwan | UI/UX Developer |
| Aditya Kediyal | Database & Integration Engineer |
