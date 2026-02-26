# Ellipse Drawing Algorithm (Midpoint Ellipse Algorithm)

The **Midpoint Ellipse Algorithm** is used in computer graphics to draw an ellipse efficiently using only integer calculations (like Bresenham’s line algorithm).

It is based on the **implicit equation of an ellipse** and decision parameters to determine the next pixel.

---

# 1️⃣ Mathematical Derivation of Ellipse

## Standard Equation of Ellipse

For an ellipse centered at origin (0,0):

[  
\frac{x^2}{a^2} + \frac{y^2}{b^2} = 1  
]

Where:

- ( a ) = semi-major axis (x-direction radius)
    
- ( b ) = semi-minor axis (y-direction radius)
    

---

## Convert to Implicit Form

Multiply both sides by ( a^2 b^2 ):

[  
b^2 x^2 + a^2 y^2 = a^2 b^2  
]

Define implicit function:

[  
f(x,y) = b^2 x^2 + a^2 y^2 - a^2 b^2  
]

- If ( f(x,y) < 0 ) → Point is inside ellipse
    
- If ( f(x,y) = 0 ) → On ellipse
    
- If ( f(x,y) > 0 ) → Outside ellipse
    

---

# 2️⃣ Why Two Regions?

Slope of ellipse:

[  
\frac{dy}{dx} = -\frac{b^2 x}{a^2 y}  
]

We divide into two regions based on slope:

### Region 1:

When ( |\frac{dy}{dx}| < 1 )

[  
b^2 x < a^2 y  
]

Increment x step-by-step.

---

### Region 2:

When ( |\frac{dy}{dx}| ≥ 1 )

[  
b^2 x ≥ a^2 y  
]

Decrement y step-by-step.

---

# 3️⃣ Algorithm Derivation

We start at:

[  
(x_0, y_0) = (0, b)  
]

---

# 🔹 REGION 1 DERIVATION

Decision parameter:

We test midpoint between:

- East pixel: (x+1, y)
    
- South-East pixel: (x+1, y-1)
    

Midpoint:

[  
(x+1, y-\frac{1}{2})  
]

Decision parameter:

[  
p_1 = f(x+1, y-\frac{1}{2})  
]

Substitute in f(x,y):

[  
p_1 = b^2(x+1)^2 + a^2(y-\frac{1}{2})^2 - a^2b^2  
]

Initial value at (0,b):

[  
p_{10} = b^2 - a^2 b + \frac{a^2}{4}  
]

---

## Region 1 Decision Rules

If:

### Case 1: ( p_1 < 0 )

Midpoint inside → choose East

[  
x = x+1  
]

Update:

[  
p_1 = p_1 + 2b^2x + b^2  
]

---

### Case 2: ( p_1 ≥ 0 )

Choose South-East

[  
x = x+1  
]  
[  
y = y-1  
]

Update:

[  
p_1 = p_1 + 2b^2x - 2a^2y + b^2  
]

Continue until:

[  
b^2x ≥ a^2y  
]

---

# 🔹 REGION 2 DERIVATION

Now we step in y-direction.

Midpoint between:

- South pixel: (x, y-1)
    
- South-East pixel: (x+1, y-1)
    

Midpoint:

[  
(x+\frac{1}{2}, y-1)  
]

Decision parameter:

[  
p_2 = f(x+\frac{1}{2}, y-1)  
]

Initial:

[  
p_{20} = b^2(x+\frac{1}{2})^2 + a^2(y-1)^2 - a^2b^2  
]

---

## Region 2 Decision Rules

### Case 1: ( p_2 > 0 )

Midpoint outside → choose South

[  
y = y-1  
]

Update:

[  
p_2 = p_2 - 2a^2y + a^2  
]

---

### Case 2: ( p_2 ≤ 0 )

Choose South-East

[  
x = x+1  
]  
[  
y = y-1  
]

Update:

[  
p_2 = p_2 + 2b^2x - 2a^2y + a^2  
]

Continue until:

[  
y = 0  
]

---

# 4️⃣ Complete Algorithm (Step-by-Step)

### Input:

- a (x-radius)
    
- b (y-radius)
    
- Center (xc, yc)
    

---

### Step 1: Initialize

[  
x = 0  
]  
[  
y = b  
]

[  
p_1 = b^2 - a^2 b + \frac{a^2}{4}  
]

---

### Step 2: Region 1

While:

[  
b^2x < a^2y  
]

1. Plot symmetric points:
    

[  
(xc ± x, yc ± y)  
]

2. If ( p_1 < 0 )
    

[  
x = x+1  
]  
[  
p_1 = p_1 + 2b^2x + b^2  
]

Else:

[  
x = x+1  
]  
[  
y = y-1  
]  
[  
p_1 = p_1 + 2b^2x - 2a^2y + b^2  
]

---

### Step 3: Initialize Region 2

[  
p_2 = b^2(x+\frac{1}{2})^2 + a^2(y-1)^2 - a^2b^2  
]

---

### Step 4: Region 2

While:

[  
y > 0  
]

1. Plot symmetric points
    
2. If ( p_2 > 0 )
    

[  
y = y-1  
]  
[  
p_2 = p_2 - 2a^2y + a^2  
]

Else:

[  
x = x+1  
]  
[  
y = y-1  
]  
[  
p_2 = p_2 + 2b^2x - 2a^2y + a^2  
]

---

# 5️⃣ Symmetry Used

Ellipse is symmetric in all 4 quadrants.

For every point (x,y), plot:

[  
(xc+x, yc+y)  
]  
[  
(xc-x, yc+y)  
]  
[  
(xc+x, yc-y)  
]  
[  
(xc-x, yc-y)  
]

This reduces computation to 1/4th.

---

# 6️⃣ Visual Understanding

## Region 1 (Slope < 1)

![Image](https://www.tutorialspoint.com/computer_graphics/images/midpoint_ellipse_drawing_algorithm.jpg)

![Image](https://www.anirdesh.com/math/algebra/ellipse-tangent-1.svg)

![Image](https://imgv2-2-f.scribdassets.com/img/document/63708061/original/ddc4928275/1?v=1)

![Image](https://i.imgur.com/r7relos.png)

---

## Region 2 (Slope ≥ 1)

![Image](https://www.tutorialspoint.com/computer_graphics/images/midpoint_ellipse_drawing_algorithm.jpg)

![Image](https://www.tutorialspoint.com/computer_graphics/images/midpoint_calculations.jpg)

![Image](https://imgv2-2-f.scribdassets.com/img/document/63708061/original/ddc4928275/1?v=1)

![Image](https://i.imgur.com/r7relos.png)

---

# 7️⃣ Why This Algorithm is Efficient?

- Uses only addition and subtraction
    
- No floating-point multiplication inside loop
    
- Faster than direct equation method
    
- Similar logic to Midpoint Circle Algorithm
    

---

# 🔥 Final Summary for Exams

✔ Based on ellipse implicit equation  
✔ Divided into two regions based on slope  
✔ Uses midpoint decision parameter  
✔ Uses 4-way symmetry  
✔ Incremental integer updates

---

If you want, I can also provide:

- ✔ Numerical example step-by-step
    
- ✔ Comparison with DDA ellipse
    
- ✔ C / C++ implementation
    
- ✔ Short 8-mark exam answer format
    
- ✔ Handwritten-style notes format
    

Just tell me what you need.