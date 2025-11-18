
## Gist

The patent claims a game recommendation engine designed to map video games to disabilities. This computer system works by storing games and disabilities as "objects" in separate databases, each with detailed attributes.

The core of the invention is a correlation engine. When a user submits a query, this engine finds statistical correlations between game attributes (like "use of red color" or "controller" interface) and disability attributes (like "color blindness" or "shaking").

Based on these correlations, the engine identifies quantified relationships.

Finally, the engine uses these relationships to generate recommendations, such as a "ranked listing" of games that are accessible to a player or a list of "compatibility scores" that tell a developer which features to change to make their game more compatible with a specific disability.

## Chosen Claims

1. **A Core System Architecture:** The patent claims a game recommendation engine built from a computer system, a **Game Database** (storing game objects), a **Disability Database** (storing disability objects), a **Query Interface**, and a **Correlation Engine**.

2. **A Specific Multi-Step Process:** The correlation engine is configured to **establish correlations** between game and disability attributes, **identify relationships** from those correlations, and **generate a recommendation** based on the relationships.

3. **Dual-Purpose Recommendations:** The recommendations serve two primary functions:
    - Indicating if a game attribute is **"accessible"** or **"inaccessible"** to individuals with a specific disability (for players).
    
    - Indicating if a disability is **"compatible"** or **"incompatible"** with a game (for developers).

4. **Quantified & Ranked Outputs:** The engine generates a **"ranked listing of recommendations"** that are sorted according to **"compatibility scores"** derived from the correlations.

5. **Advanced Applications (IDE & Diagnostics):** The system is claimed to support advanced uses, such as coupling with a **development environment (IDE)** for automatic queries and using a **"representation of game play"** as a query to generate a list of associated disabilities.