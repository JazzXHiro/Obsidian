---
creation_date: 2025-01-07 11:51
modification_date: Tuesday 7th January 2025 13:27:22
current_time: Sunday, 12th January 2025, 11:43:57 PM
tags:
  - maths-sem-4
  - maths
---
```ad-info
collapse: open 
**Created**::`=dateformat(this.file.ctime, "DDDD, HH:mm")` 
**Modified**::`=dateformat(this.file.mtime, "DDDD, HH:mm")` 
**Location**::`=this.file.path`
```
[[t-adult]]
# Maths Lecture 1

Links: [[college_MOC#Linear Algebra]]
## Why do we use Matrix?
- array relevance
- ease of calculations
- to solve a system of linear equations
- Used in these fields:
	- **Mathematics**: Solve systems of linear equations, transformations, and calculus operations.
	- **Computer Graphics**: Represent and perform geometric transformations like rotation, scaling, and translation.

---
## Equations and Polynomials
### Equations
- An **equation** is a mathematical statement that asserts the ==equality of two expressions==, connected by an **equals sign** ($=$)
- The goal is often to ==solve the equation== by finding the value(s) of the variable(s) that make the ==equality true==
- **Example**:
	- $2x + y = 5$; solution: $x = 5$

### Polynomials
- A **polynomial** is a specific type of mathematical expression consisting of ==variables raised to non-negative integer powers==, combined with ==coefficients==
- Polynomials are typically written as a ==sum of terms==, where ==each term== includes a **co-efficient** and a variable raised to an **exponent**.
- **Example**:
	- $P(x) = 3x^{2} + 2x + 1$
#### General Form:
$$
P(x) = a_{n}x^{n} + a_{n-1}x^{n-1} + \dots + a_{1}x + a_{0}
$$
$$
\text{where } a_{n}, a_{n-1}, \dots, a_{0} \text{ are coefficients, } n \text{ is a non-negative integer, and } x \text{ is the variable.}
$$
---
### Differences between Equations and Polynomials

| Criteria        | Equation                                                                                                                | Polynomials                                                                                                       |
| --------------- | ----------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------- |
| **Definition**  | asserts equality between two expressions                                                                                | an expression without any assertion of equality                                                                   |
| **Objective**   | focus is on finding solutions that satisfy the equality                                                                 | focus is often on their properties, such as degree, roots, or behavio                                             |
| **Structure**   | can include any type of terms (not necessarily polynomials), including trigonometric, logarithmic, or exponential terms | strictly sums of terms with variables raised to non-negative integer powers                                       |
| **Solvability** | may or may not be solvable, depending on their type                                                                     | can be solved by finding their roots, but they are not inherently "problems" to solve unless equated to something |

---
### Connecting the Two
- When a polynomial is equated to a value (typically zero), it becomes a **polynomial equation**.
- **Example**:
	- Polynomial: $P(x) = 3x^{2} + 2x + 1$
	- Equation: $3x^{2} + 2x + 1 = 0$
- Here, ==solving the equation== involves ==finding the roots== of the polynomial.

---
## System of Linear Equations
### Lecture Notes
- $2e^{x} + 5\log(y) = \sin(1)$ => Non-Linear
- $2x + 3y = 5$ => Linear
- $2xy = 10$ => Non-Linear
---
#### Note
1. $ax + by = p \text{ where } a, b, p \in \mathbb{R}$
2. $\mathbb{R}^{2} = \mathbb{R} \times \mathbb{R} \equiv \{ (x,y) : x, y \in \mathbb{R} \}$
	- where $\mathbb{R^{2}}$:
	- 2D Euclidean Plane OR
	- 2D Plane OR
	- 2D Cartesian Plane
3. $\mathbb{R}^{3} = \{ (x_{1}, x_{2}, x_{3}) \text{ each } x_{i} \in \mathbb{R} \}$
4. $\mathbb{R}^{n} = \{ (x_{i}, x_{2}, x_{3}, \dots, x_{n}): x_{1}, x_{2}, x_{3}, \dots, x_{n} \in \mathbb{R}\}$
	- OR => $\mathbb{R}^{n} = \{ (x_{1}, x_{2}, x_{3}, \dots, x_{n}): \text{ each } x_{i} \in \mathbb{R}$
	- OR => $\mathbb{R}^{n} = \{ (x_{2}, x_{2}, x_{3}, \dots, x_{n}): x_{i} \in \mathbb{R}, \, \forall \, i = 1, 2, 3, \dots, n$
	- OR => $\mathbb{R}^{n} = \{ (x_{1}, x_{2}, x_{3}, \dots, x_{n}): x_{i} \in \mathbb{R}, \, \forall \, 1 \leq i \leq n \cap i \in n$

#### Fill in the Blanks
1. $ax + by = p \text{ where } a, b, p \in \mathbb{R}$ represents a ==line== in $\mathbb{R}^{2}$
2. $ax + by +cz = d \text{ where } a, b, c, d \in \mathbb{R}$ represents a ==plane== in $\mathbb{R}^{3}$
3. $a_{1}x_{1} + a_{2}x_{2} + \dots + a_{n}x_{n} = b \text{ where each } a_{i}, b \in R$ represents a ==hyperplane==