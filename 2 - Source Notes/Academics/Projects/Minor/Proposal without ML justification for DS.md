Yes — **there _is_ a solid data-science justification** for this project **even without a recommendation engine**.  
You just need to frame it correctly. Below is a **clear, academically defensible justification** you can use in reviews, viva, or reports.

---

## Short Answer (for viva)

> _This project focuses on data collection, preprocessing, exploratory analysis, and analytics-driven insights rather than predictive modeling. It addresses the foundational stages of the data science lifecycle, which are often more critical than model building itself._

That alone is already valid.

---

## Where Data Science Exists in Your Project

### 1️⃣ Data Collection (Primary DS Stage)

Your system **generates real behavioral data**, not scraped or synthetic data.

**Data captured:**

- Game launch timestamps
    
- Session duration
    
- Frequency of play
    
- Time-of-day usage
    
- Weekly patterns
    

📌 This is **user behavior telemetry**, which is a core data science domain.

> Many DS projects _fail_ because they skip reliable data collection. Yours doesn’t.

---

### 2️⃣ Data Storage & Structuring

You are converting raw events into **structured datasets**:

|Raw Event|Structured Feature|
|---|---|
|Game opened|Session start|
|Game closed|Session end|
|Duration|Session length|
|Timestamp|Hour / Day / Weekend|

This is:

- Data normalization
    
- Feature engineering (without ML)
    
- Time-series structuring
    

📌 **Feature engineering is data science**, not just ML.

---

### 3️⃣ Exploratory Data Analysis (EDA)

Your analytics layer directly supports EDA concepts:

- Peak gaming hours
    
- Most-played titles
    
- Average vs long sessions
    
- Weekday vs weekend behavior
    

These answer **analytical questions**, such as:

- _When does the user play most?_
    
- _Which games show high engagement?_
    
- _What usage patterns exist over time?_
    

📌 EDA is explicitly a **data science pillar**.

---

### 4️⃣ Descriptive & Diagnostic Analytics

Your project falls under **descriptive + diagnostic analytics**, which are formal DS categories:

|Analytics Type|Your Project|
|---|---|
|Descriptive|Total playtime, session stats|
|Diagnostic|Why engagement is higher at certain times|
|Predictive|❌ (intentionally excluded)|
|Prescriptive|❌|

⚠️ **Important academic point:**

> Data Science ≠ Machine Learning

Most universities accept:

> _Analytics systems that extract insights from behavioral data_

---

### 5️⃣ Time-Series & Behavioral Analysis

Session logs form **time-series data**:

- Irregular intervals
    
- Event-driven sequences
    
- User-centric timelines
    

This is the same data type used in:

- App usage analytics
    
- Streaming platforms
    
- Fitness trackers
    
- Productivity tools
    

📌 You are solving a **behavioral analytics problem**, not a recommendation problem.

---

## How to Justify “No ML” Academically

Use this sentence (it works):

> _The project intentionally focuses on data acquisition, preprocessing, feature extraction, and exploratory analysis, as these stages form the foundation of any data-driven system. Predictive modeling is considered future work once sufficient high-quality data is accumulated._

This shows **maturity**, not limitation.

---

## If Examiner Asks: “Why Not Machine Learning?”

Answer:

> _Machine learning models require large, labeled, multi-user datasets. This project operates on single-user local data, where descriptive analytics provides higher accuracy and interpretability than predictive models._

That is **technically correct and defensible**.

---

## Data Science Lifecycle Mapping (Very Strong)

|DS Phase|Covered?|How|
|---|---|---|
|Problem definition|✅|Fragmented game usage|
|Data collection|✅|Session logging|
|Data cleaning|✅|Validation, normalization|
|Feature engineering|✅|Time-based metrics|
|EDA|✅|Usage insights|
|Visualization|✅|Analytics UI|
|Modeling|❌|Out of scope|
|Evaluation|✅|Accuracy of tracking|

📌 Covering **6 out of 8 stages** is more than enough.

---

## One-Line Summary (Use This in Proposal)

> _Vortex is a data-driven behavioral analytics system that applies core data science principles—data collection, structuring, exploratory analysis, and visualization—to improve user understanding of gaming habits._

---

## If You Want (Optional Upgrade)

Without adding ML, you _could_ optionally include:

- Engagement scoring (rule-based)
    
- Trend detection
    
- Usage clustering (still non-ML if rule-based)
    

But **you don’t need to** for justification.

---

### Verdict

✅ **Yes, this is a legitimate Data Science project**  
✅ Stronger than many ML-only “toy models”  
✅ Academically safe for proposal, viva, and grading

If you want, I can:

- Add a **“Data Science Justification” subsection** directly into your MD
    
- Draft **viva Q&A answers**
    
- Reframe domain as **“Applied Data Analytics”** if your guide prefers that wording