 
## Gist

The patent claims a game recommendation engine designed to map video games to disabilities. This computer system works by storing games and disabilities as "objects" in separate databases, each with detailed attributes.

The core of the invention is a correlation engine. When a user submits a query, this engine finds statistical correlations between game attributes (like "use of red color" or "controller" interface) and disability attributes (like "color blindness" or "shaking").

Based on these correlations, the engine identifies quantified relationships.

Finally, the engine uses these relationships to generate recommendations, such as a "ranked listing" of games that are accessible to a player or a list of "compatibility scores" that tell a developer which features to change to make their game more compatible with a specific disability.

## Chosen Claims

1. **A Core System Architecture:** The patent claims a game recommendation engine built from a computer system, a Game Database (storing game objects), a Disability Database (storing disability objects), a Query Interface, and a Correlation Engine.

2. **A Specific Multi-Step Process:** The correlation engine is configured to establish correlations between game and disability attributes, identify relationships from those correlations, and generate a recommendation based on the relationships.

3. **Dual-Purpose Recommendations:** The recommendations serve two primary functions:
    - Indicating if a game attribute is "accessible" or "inaccessible" to individuals with a specific disability (for players).
    
    - Indicating if a disability is "compatible" or "incompatible" with a game (for developers).

4. **Quantified & Ranked Outputs:** The engine generates a "ranked listing of recommendations" that are sorted according to "compatibility scores" derived from the correlations.

5. **Advanced Applications (IDE & Diagnostics):** The system is claimed to support advanced uses, such as coupling with a development environment (IDE) for automatic queries and using a "representation of game play" as a query to generate a list of associated disabilities.

## Support for Claims

### 1. A Core System for Mapping Games to Disabilities

This system is built on several key components that work together:

- A game database that stores "game objects" (representing individual games) and their "game attributes" (like genre, interface, or art style).

- A disability database that stores "disability objects" and their "disability attributes" (like type, symptoms, or experts).

- A query interface (like an API or web server) that allows a user to submit a query to the system.

- A correlation engine that processes the query.

### 2. The Process of Correlation, Relationship, and Recommendation

The engine is configured to:

1. **Establish Correlations:** It first finds statistical or logical "correlations" between game attributes and disability attributes that match the user's query.

2. **Identify Relationships:** Based on these correlations, it identifies and quantifies "relationships" between the game objects and disability objects. **Figure 3** provides a visual example of this, showing a plotted relationship between the "Metric: Level Success Rate," the "Game Attribute: % Use of Red," and the "Disability Attribute: Degree of R/G Color blindness"999999999.
    
3. **Generate Recommendations:** Finally, the engine uses these quantified relationships to generate a "recommendation" 10101010and sends it to an output device11.
    

---

### 3. Dual-Purpose Recommendations (For Players and Developers)

The patent repeatedly claims the system's recommendations are valuable for two distinct audiences, a concept summarized in the abstract12.

- **For Disabled Players:** The engine can recommend games that are **"accessible"** to them based on their specific disability131313. Claim 20 explicitly mentions generating a "list of game features accessible by disabled individuals"14.
    
- **For Game Developers:** The engine can recommend game features to _add_ or _change_ to make a game more compatible with a disability15. Claim 18 specifies a "recommendation to change game attributes" 16, and Claim 5 mentions indicating a disability is **"compatible"** with game play17.
    

---

### 4. Quantified and Ranked "Compatibility Scores"

The recommendations generated are not just simple "yes" or "no" answers. The patent claims a system for providing a **ranked listing** of recommendations based on **"compatibility scores"**18.

- **Figure 4** shows a table of these compatibility scores, which are represented as scalar values (e.g., "Use of red" has a score of "-0.9" for "Protanopia," indicating strong incompatibility)19191919.
    
- The text describes these scores as a "quantification of accessibility" 20that allows recommendations (for features or disabilities) to be **ranked**21.
    

---

### 5. Advanced Applications: IDE Integration and Diagnostic Use

Beyond a simple search, the patent claims two more advanced, automated use cases for the engine:

- **Developer IDE Integration:** The system includes a "development environment interface"22. This allows a query to be **"received automatically from the development environment"** (IDE) as a developer is actively writing code23. The engine can then provide real-time recommendations for the game under development24242424.
    
- **Diagnostic Game Play Analysis:** The system can also work in reverse. A query can be a **"representation of game play of... a disabled individual"**25. By analyzing _how_ someone plays a game, the engine can generate recommendations that are a **"listing of disabilities"** potentially associated with that game play 26, which the patent describes as a "diagnosis of potential disabilities"27.