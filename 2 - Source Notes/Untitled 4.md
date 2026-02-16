Got you. I’ll convert your handwritten reference into clean, structured **Obsidian-compatible notes** (Markdown format with headings, math blocks, and clean structure). You can directly paste this into your vault.

---

# 📌 Digital Differential Analyzer (DDA) Algorithm

## 📖 Overview

The **Digital Differential Analyzer (DDA)** algorithm is used to draw a straight line between two given points in computer graphics.  
It works by calculating intermediate points using the slope of the line.

---

## 📐 Given



---

## 🧠 Algorithm Logic

### Case 1: |m| < 1 (Line is less steep)

Increment **x** by 1 and compute corresponding **y**.

[  
x_{i+1} = x_i + 1  
]  
[  
y_{i+1} = y_i + m  
]

---

### Case 2: |m| ≥ 1 (Line is steep)

Increment **y** by 1 and compute corresponding **x**.

[  
y_{i+1} = y_i + 1  
]  
[  
x_{i+1} = x_i + \frac{1}{m}  
]

---

## 📝 Steps of DDA Algorithm

1. Input (x_1, y_1, x_2, y_2)
    
2. Compute:
    
    - ( \Delta x = x_2 - x_1 )
        
    - ( \Delta y = y_2 - y_1 )
        
3. Calculate number of steps:
    
    [  
    steps = \max(|\Delta x|, |\Delta y|)  
    ]
    
4. Compute increments:
    
    [  
    x_{inc} = \frac{\Delta x}{steps}  
    ]  
    [  
    y_{inc} = \frac{\Delta y}{steps}  
    ]
    
5. Start from ((x_1, y_1))
    
6. Plot next point using:
    
    [  
    x = x + x_{inc}  
    ]  
    [  
    y = y + y_{inc}  
    ]
    

---

## ⚠️ Limitations of DDA

- Uses floating point arithmetic.
    
- Slower compared to Bresenham’s algorithm.
    
- Rounding errors may occur.
    

---

---

# 📌 Bresenham’s Line Drawing Algorithm

## 📖 Overview

Bresenham’s algorithm is an efficient line drawing algorithm that uses **integer arithmetic only**, making it faster than DDA.

---

## 📐 Given

Endpoints:

[  
(x_1, y_1), (x_2, y_2)  
]

[  
\Delta x = x_2 - x_1  
]  
[  
\Delta y = y_2 - y_1  
]

Slope:

[  
m = \frac{\Delta y}{\Delta x}  
]

---

## 🎯 Decision Parameter

Initial decision parameter:

[  
P_0 = 2\Delta y - \Delta x  
]

---

# 🔹 Case 1: m < 1

### If (P_k < 0)

[  
x_{k+1} = x_k + 1  
]  
[  
y_{k+1} = y_k  
]  
[  
P_{k+1} = P_k + 2\Delta y  
]

---

### If (P_k \ge 0)

[  
x_{k+1} = x_k + 1  
]  
[  
y_{k+1} = y_k + 1  
]  
[  
P_{k+1} = P_k + 2\Delta y - 2\Delta x  
]

---

# 🔹 Case 2: m > 1

### If (P_k < 0)

[  
x_{k+1} = x_k  
]  
[  
y_{k+1} = y_k + 1  
]  
[  
P_{k+1} = P_k + 2\Delta x  
]

---

### If (P_k \ge 0)

[  
x_{k+1} = x_k + 1  
]  
[  
y_{k+1} = y_k + 1  
]  
[  
P_{k+1} = P_k + 2\Delta x - 2\Delta y  
]

---

## 📝 Steps of Bresenham’s Algorithm (for m < 1)

1. Input endpoints.
    
2. Compute ( \Delta x ) and ( \Delta y ).
    
3. Initialize:  
    [  
    P_0 = 2\Delta y - \Delta x  
    ]
    
4. Repeat until (x = x_2):
    
    - If (P_k < 0) → choose East pixel
        
    - Else → choose North-East pixel
        
5. Update decision parameter accordingly.
    

---

## ✅ Advantages

- Uses integer calculations only.
    
- Faster than DDA.
    
- More accurate.
    
- No floating-point rounding errors.
    

---

## 🔎 DDA vs Bresenham (Quick Comparison)

|Feature|DDA|Bresenham|
|---|---|---|
|Arithmetic|Floating point|Integer only|
|Speed|Slower|Faster|
|Accuracy|Less|More|
|Efficiency|Moderate|High|

---

If you want, I can also:

- Convert this into exam-ready short notes
    
- Add example numerical problem
    
- Add algorithm pseudocode format for viva
    
- Create a comparison flowchart (Mermaid for Obsidian)
    

Just tell me what you need for your CG prep.