---
creation_date: Tuesday, 14th January 2025, 11:10:17 AM
modification_date:  Tuesday, 14th January 2025, 11:10:17 AM
current_time: Tuesday, 14th January 2025, 11:10:24 AM
tags: maths-sem-4, maths
---
```ad-info
collapse: open 
**Created**::`=dateformat(this.file.ctime, "DDDD, HH:mm")` 
**Modified**::`=dateformat(this.file.mtime, "DDDD, HH:mm")` 
**Location**::`=this.file.path`
```

# Maths Lecture 4
Links: [[college_MOC#Linear Algebra | Linear Algebra]]
Lecture Date::2025-01-14

[[t-adult]]

---
## Lecture Notes

### To compute Rank of a Matrix
- Given a matrix $A_{m\times n}$, first reduce the given matrix $A$ to its equivalent row echelon form by applying a series of elementary row operations.
- Then, rank of $A$ is given by the number of non-zero rows in row echelon form of $A$ or number of pivot elements in row echelon form of $A$.

---
### Note
1. Pivot element is the first non-zero entry in a row after conversion to the row echelon form.
2. Rank of a matrix also determines the number of linearly independent rows/columns of a matrix.
- Example:
$$
\begin{pmatrix}
1 & 0 & 1 \\
-2 & 0 & -2 \\
3 & 0 & 3
\end{pmatrix}, 
\begin{pmatrix}
1 & -1 & 2 \\
-2 & 1 & 3 \\
-1 & 0 & 5
\end{pmatrix},
\begin{pmatrix}
1 & 0 & 0 \\
0 & 1 & 0 \\
0 & 0 & 1
\end{pmatrix}
$$

---
### Questions
#### Question 1
- Find the rank of the matrix:
$$
\begin{pmatrix}
1 & 2 & 3 & 0 \\
2 & 4 & 3 & 2 \\
3 & 2 & 1 & 3 \\
6 & 8 & 7 & 5
\end{pmatrix}
$$
##### Solution:
Given matrix:
$$
A =
\begin{pmatrix}
1 & 2 & 3 & 0 \\
2 & 4 & 3 & 2 \\
3 & 2 & 1 & 3 \\
6 & 8 & 7 & 5
\end{pmatrix}
$$
Applying $R_{2} \to R_{2} - 2\cdot R_{1}$, $R_{3} \to R_{3} - 3\cdot R_{1}$, $R_{4} \to R_{4} - 6\cdot R_{1}$, we get:
$$
A \sim 
\begin{pmatrix}
1 & 2 & 3 & 0 \\
0 & 0 & -3 & 2 \\
0 & -4 & -8 & 3 \\
0 & -4 & -11 & 5
\end{pmatrix}
$$
Applying $R_{2} \leftrightarrow R_{3}$, we get:
$$
A \sim 
\begin{pmatrix}
1 & 2 & 3 & 0 \\
0 & -4 & -8 & 3 \\
0 & 0 & -3 & 2 \\
0 & -4 & -11 & 5
\end{pmatrix}
$$
Applying $R_{4} \to R_{4} - R_{2}$, we get:
$$
A \sim
\begin{pmatrix}
1 & 2 & 3 & 0 \\
0 & -4 & -8 & 3 \\
0 & 0 & -3 & 2 \\
0 & 0 & -3 & 2
\end{pmatrix}
$$
Applying $R_{4} \to R_{4} - R_{3}$, we get:
$$
A \sim
\begin{pmatrix}
1 & 2 & 3 & 0 \\
0 & -4 & -8 & 3 \\
0 & 0 & -3 & 2 \\
0 & 0 & 0 & 0
\end{pmatrix}
$$
which is the row echelon form of Matrix $A$.
$$
\begin{align}
\text{Rank of A} = \rho(A) & = \text{Number of non-zero rows in row echelon form of A} \\ & = \text{Number of pivot elements in row echelon form of A} \\ & = 3
\end{align}
$$

---
#### Question 2
- Find the value of $k \in \mathbb{R}$, such that the rank of the given matrix is 3
$$
\begin{pmatrix}
6 & 3 & 5 & 9 \\
5 & 2 & 3 & 6 \\
3 & 1 & 2 & 3 \\
2 & 1 & 1 & k
\end{pmatrix}
$$
##### Solution I:
$$
\begin{vmatrix}
2 & 3 & 6 \\
1 & 2 & 3 \\
1 & 1 & k
\end{vmatrix}
\begin{align}
& = 2\cdot(2k - 3) - 3\cdot(k - 3) + 6(1-2) \\
& = 4\cdot k - 6 - 3\cdot k +9 - 6 \\
& = k - 3
\end{align}
$$
$$
\begin{vmatrix}
5 & 3 & 6 \\
3 & 2 & 3 \\
2 & 1 & k
\end{vmatrix}
\begin{align}
& = 5\cdot(2\cdot k - 3) - 3\cdot(3\cdot k - 6) + 6\cdot(3-4) \\
& = 10\cdot k - 15 - 9\cdot k + 18 - 6 \\
& = k - 3
\end{align}
$$
$$
\begin{vmatrix}
5 & 2 & 6 \\
3 & 1 & 3 \\
2 & 1 & k
\end{vmatrix}
\begin{align}
& = 5\cdot(k - 3) - 2\cdot(3\cdot k - 6) + 6\cdot(3-2) \\
& = 5\cdot k - 15 - 6\cdot k +12 + 6 \\
& = 3 - k
\end{align}
$$
$$
\begin{vmatrix}
5 & 2 & 3 \\
3 & 1 & 2 \\
2 & 1 & 1
\end{vmatrix}
\begin{align}
& = 5\cdot(1-2) - 2\cdot(3-4) + 3\cdot(3-2)  \\
& = 2 + 3 - 5 \\
& = 0
\end{align}
$$
Finally:
$$
\begin{pmatrix}
6 & 3 & 5 & 9 \\
5 & 2 & 3 & 6 \\
3 & 1 & 2 & 3 \\
2 & 1 & 1 & k
\end{pmatrix}
\begin{align}
& = 6\cdot(k-3) - 3\cdot(k-3) + 5\cdot(3-k) \\
& = (6\cdot k - 3\cdot k - 5\cdot k) - 18 + 9 + 15 \\
& = 6 - 2\cdot k  \\
\end{align}
$$
$$
\begin{align}
& \implies 6 - 2\cdot k = 0 \\
& \implies k = 3
\end{align}
$$
---
##### Solution II:
Given matrix:
$$
A = 
\begin{pmatrix}
6 & 3 & 5 & 9 \\
5 & 2 & 3 & 6 \\
3 & 1 & 2 & 3 \\
2 & 1 & 1 & k
\end{pmatrix}
$$
Applying $R_{1} \to R_{1} - R_{2}$, we get:
$$
A \sim
\begin{pmatrix}
1 & 1 & 2 & 3 \\
5 & 2 & 3 & 6 \\
3 & 1 & 2 & 3 \\
2 & 1 & 1 & k
\end{pmatrix}
$$
Applying $R_{2} \to R_{2} - 5\cdot R_{1}$, $R_{3} \to R_{3} - 3\cdot R_{1}$, $R_{4} \to R_{4} - 2\cdot R_{1}$, we get:
$$
A \sim
\begin{pmatrix}
1 & 1 & 2 & 3 \\
0 & -3 & -7 & -9 \\
0 & -2 & -4 & -6 \\
0 & -1 & -3 & (k-6)
\end{pmatrix}
$$
Applying $R_{2} \leftrightarrow R_{3}$, we get:
$$
A \sim
\begin{pmatrix}
1 & 1 & 2 & 3 \\
0 & -2 & -4 & -6 \\
0 & -3 & -7 & -9 \\
0 & -1 & -3 & (k - 6)
\end{pmatrix}
$$
Applying $R_{2} \to -\frac{1}{2}\cdot R_{2}$, we get:
$$
A \sim
\begin{pmatrix}
1 & 1 & 2 & 3 \\
0 & 1 & 2 & 3 \\
0 & -3 & -7 & -9 \\
0 & -1 & -3 & (k - 6)
\end{pmatrix}
$$
Applying $R_{3} + 3\cdot R_{2}$,$R_{4} \to R_{4} + R_{2}$, we get:
$$
A \sim
\begin{pmatrix}
1  & 1 & 2 & 3  \\
0 & 1 & 2 & 3 \\
0 & 0 & -1 & 0 \\
0 & 0 & -1 & (k - 3)
\end{pmatrix}
$$
Applying $R_{4} \to R_{4} - R_{3}$, we get:
$$
A \sim
\begin{pmatrix}
1 & 1 & 2 & 3 \\
0 & 1 & 2 & 3 \\
0 & 0 & -1 & 0 \\
0 & 0 & 0 & (k - 3)
\end{pmatrix}
$$
which is the row echelon form of Matrix $A$.

$\because \rho(A) = 3$ (Given)
$\therefore$ Number of non-zero rows in row echelon form of $A = 3$ 
$$
\begin{align}
& \implies (k - 3) = 0 \\
& \implies k  = 3
\end{align}
$$
