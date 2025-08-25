	2025-08-21 02:46

Status: [[t-child]]

Tags: [[t-academics]] [[t-FLAT]] 

---
# Introduction to Theory of Computation

## A pioneer to Automata Theory

### **ALAN TURING (1912-1954)** - "TURING M/C"

- Father of modern computer
    
- An English Mathematician
    
- Turing's machine is essentially an abstract model of modern-day computer **execution and storage**.

---

## Automata

- Automata are abstract models of machines.  
- They perform computations on an input by moving through a series of **states or configurations** ($q \in Q$).  
- As a result, once the computation reaches an **accepting configuration** ($q \in F$), it accepts that input.  
- The most general and powerful automata is the **Turing Machine**.  

### Objective  
To analyze the **dynamic behavior** of **discrete systems**.

### Characteristics  
Characteristics of such machines are based on:

$$ \text{Inputs, Outputs, and States} $$


---

# The Basic Concepts of Automata Theory  

## Alphabet  

- An **Alphabet** is a **finite, non-empty set of symbols that an automata can receive**.  
- Representation: $\Sigma$ (Sigma)  

### Examples  

- **Binary Symbols:**  
  $\Sigma = \{0, 1\}$  

- **All lowercase letters:**  
  $\Sigma = \{a, b, c, \dots, z\}$  

- **Digits:**  
  $\Sigma = \{0, 1, 2, \dots, 9\}$  

- **Alphanumeric:**  
  $\Sigma = \{a\!-\!z, A\!-\!Z, 0\!-\!9\}$  

---

## Flow of Concepts  

$$
\text{Alphabet} \;\;\;\longrightarrow\;\;\; \text{Strings} \;\;\;\longrightarrow\;\;\; \text{Language}
$$


---

## Strings  

- A **string** or **word** is a **finite collection of symbols** selected from the alphabets ($\Sigma$).  
- A string can also be **empty**, which is represented by $\varepsilon$ (Epsilon).  

---

### Length of String  

- The **length** of a string is denoted by $|w|$,  
  where $w$ is the string.  
- It represents the **number of positions (symbols)** in the string.  

#### Examples  

- If $w = 01101$, then length $= 5$  
  $$ |w| = 5 $$  

- If $w = ababaa$, then length $= 6$  
  $$ |w| = 6 $$

---

# Empty String  

- The **empty string** is the string with **zero occurrence of symbols**.  
- The empty string is represented by $\varepsilon$.  
 
---

## Kleene Star  

- $\Sigma^* = \{\varepsilon, 0, 1, 01, 10, 000, 010, 0000, \dots \}$  

Examples:  

- $\{0\}^* = \{\varepsilon, 0, 00, 000, 0000, \dots\}$  
- $\{1\}^* = \{\varepsilon, 1, 11, 111, 1111, \dots\}$  

---

## Important Note  

- $\varepsilon \in \Sigma^*$, regardless of what alphabet $\Sigma$ is.  
- i.e. $\varepsilon$ is the **only string whose length is 0**.  

---

## Example with Symbols  

If $\Sigma = \{a, b\}$:  

- $\Sigma^1 = \{a, b\}$  
- $\Sigma^2 = \{aa, ab, ba, bb\}$  

---

# The Basic Concepts…contd.

## Concatenation of Strings
- Let $x$ and $y$ be two strings.  
- Then $xy$ denotes the concatenation of $x$ and $y$, i.e., the string formed by making a copy of $x$ and followed by a copy of $y$.  

**Example**:  
If $x = ab$ and $y = cd$, then concatenation:  
$$xy = abcd$$  

---

## Reverse of the String
- Reverse of the string can be achieved by simply interchanging the order of symbols.  

**Example**:  
If $w = abcd$, then  
$$w^R = dcba$$  

Another example:  
If $w = abc$, then  
$$(w)^R = cba$$  ---
## Powers of Alphabet

Let $\Sigma$ be the alphabet. Then power of alphabet is given by:

- $\Sigma^k =$ the set of all strings of length $k$

- $\Sigma^* = \Sigma^0 \cup \Sigma^1 \cup \Sigma^2 \cup \dots$

- $\Sigma^+ = \Sigma^1 \cup \Sigma^2 \cup \Sigma^3 \cup \dots$

---

# Languages

$L$ is said to be the language over a given set of alphabets, if $L \subseteq \Sigma^*$.
A set that a finite automata accepts.

---

## Examples

1. $L$ is a language that comprises the set of even numbers over the alphabet  
   $$\Sigma = \{0, 1\}$$  

2. The language of all strings consisting of $n$ $0$’s followed by $n$ $1$’s, for some $n \geq 0$:  
   $$L = \{\varepsilon, 01, 0011, 000111, \dots\}$$



# Reference
