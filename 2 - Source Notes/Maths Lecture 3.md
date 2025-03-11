---
creation_date: Sunday, 12th January 2025, 8:05:53 PM
modification_date:  Sunday, 12th January 2025, 8:19:23 PM
current_time: Sunday, 12th January 2025, 8:21:06 PM
tags: maths-sem-4, maths
---
```ad-info
collapse: open 
**Created**::`=dateformat(this.file.ctime, "DDDD, HH:mm")` 
**Modified**::`=dateformat(this.file.mtime, "DDDD, HH:mm")` 
**Location**::`=this.file.path`
```
[[t-adult]]
# Maths Lecture 3
Links: [[college_MOC#Linear Algebra]]
Lecture Date:: 2025-01-10

---
## Lecture Notes

### Rank of a Matrix
- It is the ==highest order== of a ==non-zero minor==.
- Denoted by $rank(A)$ or $\rho(A)$ or $R(A)$
- In other words:
	- For a given matrix $A_{n \times n}$, if $\rho(A) = r$ where $r < n$, then:
		1. All minors of $A$ of order higher than $r$ (i.e., orders $r+1, r+2, ..., n$) will be zero
		2. There exists at least one non-zero minor of order $r$

---
### Note
- **Null** or **Zero Matrix**: 
	- all the ==entries are zero==
- **Non-Zero Matrix**:
	- at least ==one element is non-zero==
1. $A_{m\times n}: \rho(A_{m\times n}) \leq \min(m,n)$ where $m \neq n$
2. **Rank** of a **Null** or **Zero Matrix** is ==defined to be zero==
3. Let $A_{m\times n}$ be a **non-zero matrix**, then: $\rho(A) \geq 1$
4. **Zero Matrix** is the ==only matrix== which has ==rank zero==
5. $A_{m\times m}$, $\rho(A) = r$, $r < m$ $\implies |A| = \det(A) = 0$

---
### To determine the Rank of a Matrix

#### Row Echelon Form of a Matrix
- A matrix $A_{m\times n}$ is said to be in row echelon form if:
	1. the ==number of zeroes== preceding the ==first non-zero entry== in any row is ==lesser than== that in the ==subsequent row(s)==
	2. Zero Rows (that is, a row with all the entries as 0), if any, must be at the ==bottom of the matrix==
	3. the first non-zero entry in any row is ==unity== (that is, 1)
- (1) and (2) are mandatory, but (3) is optional
- Examples:
- $A$ is in Row Echelon Form
$$
A = 
\begin{pmatrix}
1 & 2 & 5 & -1 & 4 \\
0 & 3 & 0 & 0 & 0 \\
0 & 0 & 4 & 0 & 0 \\
0 & 0 & 0 & 0 & 0
\end{pmatrix}
$$
- $B$ is not in Row Echelon Form
$$
B = 
\begin{pmatrix}
3 & 4 & 5 & -1 & 2 \\
0 & 0 & 0 & 4 & 0 \\
0 & 2 & 0 & 0 & 0 \\
0 & 0 & -1 & 0 & 0 \\
0 & 0 & 0 & 0 & 0
\end{pmatrix}
$$
- $C$ is not in Row Echelon Form
$$
C =
\begin{pmatrix}
0 & 0 & 0 & 0 & 0 \\
0 & 0 & 0 & 0 & -1 \\
0 & 5 & 2 & 0 & 3 \\
0 & 0 & 1 & -1 & 0
\end{pmatrix}
$$

---
#### Elementary Row Operations
1. $R_{i} \leftrightarrow R_{j}$ (interchange)
2. $R_{i} \to k\cdot R_{i}$; where $k$ is constant, $k \in \mathbb{R} \ \& \ k \neq 0$
3. $R_{i} \to R_{i} + k\cdot R_{j}$; where $k \neq 0 \ \& \ k \in \mathbb{R}$

---
#### Column Operations
1. $C_{i} \leftarrow C_{j}$
2. $C_{i} \to k\cdot C_{i}$; where $k$ is constant, $k \in \mathbb{R} \ \& \ k \neq 0$
3. $C_{i} \to C_{i} + k\cdot C_{j}$; where $k \neq 0 \ \& \ k \in \mathbb{R}$