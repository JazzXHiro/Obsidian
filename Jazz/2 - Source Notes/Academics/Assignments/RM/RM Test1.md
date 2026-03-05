	2025-09-09 03:07

Status: [[Jazz/3 - Tags/t-child]]

Tags: [[Jazz/3 - Tags/t-RM]] [[Jazz/3 - Tags/t-sem5]]

---

###  1. Research Significance 💡

**Significance** (or the "so what?" question) explains **why your research is important**. It's the justification for the study's existence and highlights its potential contribution.

- **Theoretical Contribution:** Does it fill a gap in existing knowledge, challenge an existing theory, or provide a new framework?
    
- **Practical Contribution:** Does it solve a real-world problem, improve a process, create a new technology, or inform policy?
    
- **Methodological Contribution:** Does it propose a new research method or refine an existing one?
    

In CS, significance could be developing an algorithm that is significantly faster (e.g., O(logn) vs O(n)), creating a more secure encryption method, or designing a system with better user accessibility.

---

### 2. Criteria for Good Research ✔️

Good research is systematic, logical, and verifiable. Key criteria include:

1. **Clear Purpose & Objective:** The research question should be unambiguous.
    
2. **Rigor:** The methodology must be scrupulous and well-defined.
    
3. **Testability:** The hypothesis must be verifiable and falsifiable.
    
4. **Replicability:** Another researcher should be able to repeat the study and get similar results.
    
5. **Validity:** The research accurately measures what it intends to measure.
    
    - **Internal Validity:** Confidence that the outcome is due to the intervention, not other factors.
        
    - **External Validity:** The extent to which results can be generalized to other populations or settings.
        
6. **Reliability:** The results are consistent and repeatable over time.
    
7. **Objectivity:** The conclusions are based on data, free from researcher bias.
    
8. **Ethical:** The research is conducted without harming participants and with their informed consent.
    

---

### 3. Errors in Research ❌

Errors can undermine the validity and reliability of your findings.

- **Type I Error (α):** **False Positive**. Rejecting a true null hypothesis (H0​). You conclude there is an effect when there isn't one. (e.g., Your new algorithm is declared faster, but it's not; the difference was due to chance).
    
- **Type II Error (β):** **False Negative**. Failing to reject a false null hypothesis (H0​). You conclude there is no effect when there actually is one. (e.g., Your algorithm _is_ faster, but your experiment failed to detect the difference).
    
- **Systematic Error (Bias):** A flaw in the experimental design or data collection process that causes results to be consistently skewed in one direction. Examples include selection bias, measurement bias, or confirmation bias.
    
- **Random Error:** Unpredictable variations in measurements. It can be reduced by increasing sample size.
    

---

### 4. Objective, Aim & Hypothesis

- **Aim:** A broad statement of what you hope to achieve. It's the **overall goal** of the research.
    
    - _Example:_ "The aim of this research is to improve the efficiency of database query processing."
        
- **Objective:** Specific, measurable steps you will take to achieve the aim. They are the **"how"** of the research.
    
    - _Example 1:_ "To design a novel indexing algorithm."
        
    - _Example 2:_ "To implement the algorithm and compare its performance against standard B-tree indexing."
        
- **Hypothesis:** A specific, testable prediction about the relationship between variables.
    
    - **Null Hypothesis (H0​):** States there is no effect or relationship. (e.g., "There is no significant difference in query speed between our new algorithm and the B-tree index.")
        
    - **Alternative Hypothesis (H1​ or Ha​):** States there _is_ an effect or relationship. (e.g., "Our new algorithm results in a significantly faster query speed than the B-tree index.")
        

---

### 5. Investigation Approaches

- **Empirical Approach:** Based on **observation and experimentation**. You collect and analyze data to draw conclusions. This is the cornerstone of most scientific research, including many areas of CS like HCI, software engineering performance testing, and network analysis.
    
    - _Example:_ Testing the usability of a new UI by observing users and measuring task completion times.
        
- **Mathematical/Theoretical Approach:** Uses **formal methods, logic, and mathematical proofs** to establish truths. It doesn't rely on real-world data collection. This is common in theoretical computer science, cryptography, and algorithm analysis.
    
    - _Example:_ Proving that an algorithm has a worst-case time complexity of O(nlogn) using mathematical analysis.
        

---

### 6. Dialectic Argumentation & Demonstration

- **Demonstration:** A straightforward, linear argument that moves from accepted premises to a conclusion. Think of a mathematical proof: If A and B are true, then C must be true. It's a monologue.
    
- **Dialectic Argumentation:** A process of discovering truth by examining opposing viewpoints. It's a **dialogue**. The classic structure is:
    
    1. **Thesis:** An initial proposition or argument.
        
    2. **Antithesis:** A counter-argument that contradicts the thesis.
        
    3. **Synthesis:** A new proposition that resolves the conflict between the thesis and antithesis, often by incorporating elements of both. This synthesis can then become a new thesis for further debate.
        

This approach is useful for exploring complex problems with no single right answer, such as a debate on AI ethics.

---

### 7. Induction & Deduction

These are two primary forms of logical reasoning.

- **Deductive Reasoning (Top-Down):** Starts with a **general theory** or premise and works towards a **specific conclusion**. If the premises are true, the conclusion _must_ be true.
    
    - **General Premise:** All sorting algorithms based on comparisons have a lower bound of Ω(nlogn).
        
    - **Specific Case:** Bubble Sort is a comparison-based sorting algorithm.
        
    - **Conclusion:** Therefore, Bubble Sort's best-case performance cannot be better than Ω(nlogn) in the general case.
        
- **Inductive Reasoning (Bottom-Up):** Starts with **specific observations** and works towards a **general theory** or conclusion. The conclusion is probable, but not guaranteed.
    
    - **Specific Observation 1:** I tested my program with input A, and it crashed.
        
    - **Specific Observation 2:** I tested my program with input B, and it crashed.
        
    - **Generalization/Conclusion:** My program is unstable and crashes on many inputs.
        

---

### 8. Toulmin Model of Argumentation

A practical model for analyzing or building an argument. It's more nuanced than a simple premise-conclusion structure.

1. **Claim:** The main point you are trying to prove. (e.g., "Our new machine learning model is more accurate.")
    
2. **Grounds/Data:** The evidence or facts used to support the claim. (e.g., "In our test on the ImageNet dataset, our model achieved 95% accuracy, while the previous state-of-the-art achieved 92%.")
    
3. **Warrant:** The underlying assumption or principle that connects the grounds to the claim. It's often unstated. (e.g., "A higher accuracy score on a benchmark dataset like ImageNet is a valid indicator of a better model.")
    
4. **Backing:** Additional support for the warrant. (e.g., "The ImageNet dataset is widely accepted by the research community for benchmarking computer vision models.")
    
5. **Qualifier:** Words that express the degree of certainty in the claim. (e.g., "Our model is _likely_ more accurate _in most cases_.")
    
6. **Rebuttal:** A counter-argument or an exception to the claim. (e.g., "...unless the input images are heavily distorted, in which case the older model performs slightly better.")
    

---

### 9. PRISMA, Ethics, Risk, and Benefit

- **PRISMA (Preferred Reporting Items for Systematic Reviews and Meta-Analyses):** A framework and checklist for conducting and reporting systematic reviews. It ensures transparency and completeness, allowing others to assess the quality of the review. It primarily involves a 27-item checklist and a four-phase flow diagram (Identification, Screening, Eligibility, Included).
    
- **Ethics in Research:** Moral principles guiding research. Key tenets include:
    
    - **Informed Consent:** Participants must understand the research and agree to participate voluntarily.
        
    - **Confidentiality & Anonymity:** Protecting participants' identities and data.
        
    - **Beneficence:** Maximizing benefits and minimizing harm to participants.
        
    - **Academic Integrity:** Avoiding plagiarism, fabrication of data, and misrepresentation of results.
        
- **Risk and Benefit Analysis:** A core ethical process.
    
    - **Risk:** Potential physical, psychological, social, or economic harm to participants. In CS, this could include data breaches, privacy violations, or psychological stress from usability testing.
        
    - **Benefit:** Potential positive outcomes for the individual participants, the community, or science.
        
    - **The Rule:** The potential benefits of the research must significantly outweigh the risks to the participants.
        

---

## Data Types and Collection Methods

### Data Types

#### 1. Qualitative Data

Descriptive, non-numerical data that focuses on qualities, characteristics, and meanings. It answers "why" and "how".

- _Examples:_ Interview transcripts, user feedback ("the interface feels clunky"), observational notes.
    

#### 2. Quantitative Data

Numerical data that can be measured and statistically analyzed. It answers "how many," "how much," or "how often".

- _Examples:_ CPU usage percentage, response time in milliseconds, number of bugs, user satisfaction rating on a scale of 1-5.
    

---

### ## Data Collection Methods

#### 1. Surveys & Questionnaires 📝

A set of standardized questions given to a group of people.

- **Advantages:**
    
    - Can collect data from a large sample size efficiently.
        
    - Relatively low cost.
        
    - Anonymity can lead to more honest answers.
        
    - Easy to analyze quantitative data.
        
- **Disadvantages:**
    
    - Low response rates can introduce bias.
        
    - Respondents may not interpret questions as intended.
        
    - Lacks the depth to understand complex issues (the "why").
        
    - Rigid format; no opportunity for follow-up questions.
        

#### 2. Interviews 🗣️

Direct, one-on-one or group conversations with participants. Can be structured, semi-structured, or unstructured.

- **Advantages:**
    
    - Provides rich, in-depth qualitative data.
        
    - Allows for clarification and follow-up questions (probing).
        
    - Can capture non-verbal cues (tone, body language).
        
    - Flexible and adaptable.
        
- **Disadvantages:**
    
    - Time-consuming and expensive to conduct and transcribe.
        
    - Small sample sizes limit generalizability.
        
    - Prone to interviewer bias (the interviewer's presence can influence answers).
        
    - Data analysis is complex and subjective.
        

#### 3. Observation 👀

Systematically watching and recording behaviors, events, or phenomena in their natural setting.

- **Advantages:**
    
    - Provides direct data on actual behavior, not just self-reported behavior.
        
    - Can reveal insights that participants might not be aware of or able to articulate.
        
    - Useful for studying complex interactions in a natural context (e.g., how a dev team collaborates).
        
- **Disadvantages:**
    
    - **Hawthorne Effect:** People may change their behavior when they know they are being watched.
        
    - Highly susceptible to observer bias.
        
    - Can be time-consuming.
        
    - Ethical concerns regarding privacy.
        

#### 4. Document & Record Analysis 📄

Analyzing existing documents and records (secondary data).

- **Advantages:**
    
    - Cost-effective and unobtrusive (no interaction with participants).
        
    - Provides historical context.
        
    - Data is often stable and can be reviewed repeatedly.
        
    - Large amounts of data may be available.
        
- **Disadvantages:**
    
    - Data may be incomplete, inaccurate, or outdated.
        
    - The documents may not have been created for research purposes, so they might not fit your needs.
        
    - Authenticity and bias of the original author can be a concern.
        

#### 5. Experiments 🔬

A controlled method where the researcher manipulates one or more independent variables to observe their effect on a dependent variable.

- **Advantages:**
    
    - The only method that can establish cause-and-effect relationships.
        
    - High level of control over variables, leading to high internal validity.
        
    - Can be replicated by other researchers to verify results.
        
- **Disadvantages:**
    
    - Artificial lab settings may not reflect the real world, leading to low external validity.
        
    - Can be complex and expensive to set up.
        
    - Ethical considerations can limit the manipulation of certain variables.
        
    - Prone to human error and confounding variables if not designed carefully.

---
# Reference
