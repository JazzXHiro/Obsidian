Here are the solutions to both parts of the question.

---

### **(i) Solve the Differential Equation using Laplace Transform**

**Given:** The differential equation dt2d2y​−4dtdy​+4y=64sin(2t), with initial conditions y(0)=0 and y′(0)=1.

---

**Step 1: Apply the Laplace Transform**

We take the Laplace transform of each term in the equation. Let Y(s)=L{y(t)}. We use the standard formulas for the transforms of derivatives:

- L{y′′(t)}=s2Y(s)−sy(0)−y′(0)
    
- L{y′(t)}=sY(s)−y(0)
    
- L{sin(at)}=s2+a2a​
    

Applying these to the equation:

L{y′′}−4L{y′}+4L{y}=64L{sin(2t)}[s2Y(s)−sy(0)−y′(0)]−4[sY(s)−y(0)]+4Y(s)=64⋅s2+222​

---

**Step 2: Substitute Initial Conditions**

Now, we substitute the given initial conditions y(0)=0 and y′(0)=1:

[s2Y(s)−s(0)−1]−4[sY(s)−0]+4Y(s)=s2+4128​

s2Y(s)−1−4sY(s)+4Y(s)=s2+4128​

---

**Step 3: Solve for Y(s)**

We rearrange the equation to solve for Y(s):

Y(s)(s2−4s+4)−1=s2+4128​Y(s)(s−2)2=1+s2+4128​=s2+4(s2+4)+128​=s2+4s2+132​Y(s)=(s−2)2(s2+4)s2+132​

---

**Step 4: Partial Fraction Decomposition**

We decompose Y(s) into partial fractions:

$$\frac{s^2 + 132}{(s-2)^2(s^2 + 4)} = \frac{A}{s-2} + \frac{B}{(s-2)^2} + \frac{Cs+D}{s^2+4}$$Multiplying by the denominator gives:

s2+132=A(s−2)(s2+4)+B(s2+4)+(Cs+D)(s−2)2

- To find B, let s=2:
    
    22+132=B(22+4)⟹136=8B⟹B=17
    
- To find A, C, D, we expand and equate coefficients:
    
    s2+132=A(s3−2s2+4s−8)+17(s2+4)+(Cs+D)(s2−4s+4)
    
    s2+132=(A+C)s3+(−2A+17−4C+D)s2+(4A+4C−4D)s+(−8A+68+4D)
    
    Comparing coefficients:
    
    - s3:A+C=0⟹C=−A
        
    - s:4A+4C−4D=0⟹4A−4A−4D=0⟹D=0
        
    - s2:−2A+17−4C+D=1⟹−2A+17−4(−A)+0=1⟹2A+17=1⟹2A=−16⟹A=−8
        
    - From C=−A⟹C=8
        

So, the decomposition is:

Y(s)=−s−28​+(s−2)217​+s2+48s​

---

**Step 5: Inverse Laplace Transform**

Finally, we find the solution y(t) by taking the inverse Laplace transform of each term:

$$y(t) = L^{-1}{Y(s)} = -8L^{-1}\left{\frac{1}{s-2}\right} + 17L^{-1}\left{\frac{1}{(s-2)^2}\right} + 8L^{-1}\left{\frac{s}{s^2+2^2}\right}$$Using standard inverse transforms:

y(t)=−8e2t+17te2t+8cos(2t)

Final Answer:

The solution to the differential equation is:

y(t)=(17t−8)e2t+8cos(2t)

---

---

### **(ii) Find the Fourier Series**

**Given:** The function f(x)=x2 for the interval −π≤x≤π.

---

**Step 1: Check for Symmetry**

We check if the function is even or odd.

f(−x)=(−x)2=x2=f(x)

Since f(−x)=f(x), the function is even. For an even function, the Fourier series contains only cosine terms, and the coefficient for the sine terms, bn​, is zero for all n.

The Fourier series is given by:

f(x)=2a0​​+n=1∑∞​an​cos(nx)

---

**Step 2: Calculate the Coefficient a0​**

The formula for a0​ for an even function over [−π,π] is:

a0​=π2​∫0π​f(x)dx=π2​∫0π​x2dx

a0​=π2​[3x3​]0π​=π2​(3π3​−0)=32π2​

---

**Step 3: Calculate the Coefficients an​**

The formula for an​ for an even function over [−π,π] is:

an​=π2​∫0π​f(x)cos(nx)dx=π2​∫0π​x2cos(nx)dx

We use integration by parts (tabular method):

| Sign | Differentiate | Integrate |

| :---: | :---: | :---: |

| + | x2 | cos(nx) |

| - | 2x | n1​sin(nx) |

| + | 2 | −n21​cos(nx) |

| - | 0 | −n31​sin(nx) |

an​=π2​[nx2sin(nx)​+n22xcos(nx)​−n32sin(nx)​]0π​

Evaluating at the limits:

- The terms with sin(nx) are zero at both x=0 and x=π (since sin(0)=0 and sin(nπ)=0).
    
- We only need to evaluate the middle term:
    
    $$a_n = \frac{2}{\pi} \left[ \frac{2x\cos(nx)}{n^2} \right]_0^{\pi} = \frac{2}{\pi} \left( \frac{2\pi\cos(n\pi)}{n^2} - 0 \right)$$Since cos(nπ)=(−1)n:
    
    an​=π2​(n22π(−1)n​)=n24(−1)n​for n≥1
    

---

**Step 4: Assemble the Fourier Series**

Substituting the coefficients back into the series formula:

f(x)=2a0​​+n=1∑∞​an​cos(nx)

f(x)=21​(32π2​)+n=1∑∞​n24(−1)n​cos(nx)

Final Answer:

The Fourier series for f(x)=x2 on the interval [−π,π] is:

$$\bf{x^2 = \frac{\pi^2}{3} + 4\sum_{n=1}^{\infty} \frac{(-1)^n}{n^2} \cos(nx)}$$or, written out:$$\bf{x^2 = \frac{\pi^2}{3} - 4\left(\cos(x) - \frac{\cos(2x)}{4} + \frac{\cos(3x)}{9} - \cdots \right)}$$