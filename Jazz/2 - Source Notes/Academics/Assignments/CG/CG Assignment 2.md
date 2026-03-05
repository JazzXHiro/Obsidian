Keerti Vardhan
500119378
GG B-1

---

# Midpoint Ellipse Drawing Algorithm

---

## 1. Standard Equation of Ellipse

For an ellipse centered at origin:

$$  
\frac{x^2}{a^2} + \frac{y^2}{b^2} = 1  
$$

Where:

- $a$ = semi-major axis

- $b$ = semi-minor axis

---

## 2. Convert to Implicit Form

Multiply by $a^2 b^2$:

$$  
b^2 x^2 + a^2 y^2 = a^2 b^2  
$$

Define implicit function:

$$  
f(x,y) = b^2 x^2 + a^2 y^2 - a^2 b^2  
$$

Decision rule:

- $f(x,y) < 0$ → Point inside

- $f(x,y) = 0$ → On ellipse

- $f(x,y) > 0$ → Outside


---

## 3. Slope of Ellipse

Differentiate implicitly:

$$  
\frac{dy}{dx} = -\frac{b^2 x}{a^2 y}  
$$

We divide into two regions:

### Region 1

$$  
\left| \frac{dy}{dx} \right| < 1  
$$

$$  
b^2 x < a^2 y  
$$

Increment $x$.

---

### Region 2

$$  
\left| \frac{dy}{dx} \right| \ge 1  
$$

$$  
b^2 x \ge a^2 y  
$$

Decrement $y$.

---

# 4. Region 1 Derivation

Start point:

$$  
(x_0, y_0) = (0, b)  
$$

Midpoint between:

- East $(x+1, y)$

- South-East $(x+1, y-1)$


Midpoint:

$$  
(x+1, y-\frac{1}{2})  
$$

Decision parameter:

$$  
p_1 = f(x+1, y-\frac{1}{2})  
$$

Substitute in implicit equation:

$$  
p_1 = b^2(x+1)^2 + a^2\left(y-\frac{1}{2}\right)^2 - a^2 b^2  
$$

Initial decision parameter:

$$  
p_{10} = b^2 - a^2 b + \frac{a^2}{4}  
$$

---

## Region 1 Update Rules

If $p_1 < 0$:

$$  
x = x+1  
$$

$$  
p_1 = p_1 + 2b^2 x + b^2  
$$

---

If $p_1 \ge 0$:

$$  
x = x+1  
$$

$$  
y = y-1  
$$

$$  
p_1 = p_1 + 2b^2 x - 2a^2 y + b^2  
$$

Continue while:

$$  
b^2 x < a^2 y  
$$

---

# 5. Region 2 Derivation

Midpoint between:

- South $(x, y-1)$

- South-East $(x+1, y-1)$


Midpoint:

$$  
\left(x+\frac{1}{2}, y-1\right)  
$$

Decision parameter:

$$  
p_2 = f\left(x+\frac{1}{2}, y-1\right)  
$$

Initial value:

$$  
p_{20} = b^2\left(x+\frac{1}{2}\right)^2 + a^2(y-1)^2 - a^2 b^2  
$$

---

## Region 2 Update Rules

If $p_2 > 0$:

$$  
y = y-1  
$$

$$  
p_2 = p_2 - 2a^2 y + a^2  
$$

---

If $p_2 \le 0$:

$$  
x = x+1  
$$

$$  
y = y-1  
$$

$$  
p_2 = p_2 + 2b^2 x - 2a^2 y + a^2  
$$

Continue until:

$$  
y = 0  
$$

---

# 6. Symmetry Property

For every computed point $(x,y)$, plot:

$$  
(x_c + x, y_c + y)  
$$

$$  
(x_c - x, y_c + y)  
$$

$$  
(x_c + x, y_c - y)  
$$

$$  
(x_c - x, y_c - y)  
$$

---

# 7. Complete Algorithm (Structured Form)

**Input:** $a, b, (x_c, y_c)$

---

### Step 1: Initialize

$$  
x = 0  
$$

$$  
y = b  
$$

$$  
p_1 = b^2 - a^2 b + \frac{a^2}{4}  
$$

---

### Step 2: Region 1

While:

$$  
b^2 x < a^2 y  
$$

1. Plot symmetric points

2. If $p_1 < 0$:


$$  
x = x+1  
$$

$$  
p_1 = p_1 + 2b^2 x + b^2  
$$

Else:

$$  
x = x+1  
$$

$$  
y = y-1  
$$

$$  
p_1 = p_1 + 2b^2 x - 2a^2 y + b^2  
$$

---

### Step 3: Initialize Region 2

$$  
p_2 = b^2\left(x+\frac{1}{2}\right)^2 + a^2(y-1)^2 - a^2 b^2  
$$

---

### Step 4: Region 2

While:

$$  
y > 0  
$$

If $p_2 > 0$:

$$  
y = y-1  
$$

$$  
p_2 = p_2 - 2a^2 y + a^2  
$$

Else:

$$  
x = x+1  
$$

$$  
y = y-1  
$$

$$  
p_2 = p_2 + 2b^2 x - 2a^2 y + a^2  
$$

---
