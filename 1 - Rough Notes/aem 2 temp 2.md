Here is a complete solution as would be expected for a 20-mark examination question.

---

### **Objective**

To solve the one-dimensional wave equation for a tightly stretched string of length l with fixed endpoints, released from rest from the initial position y=y0​sin3(lπx​).

---

### **1. General Solution via Separation of Variables**

The one-dimensional wave equation is given by:

∂t2∂2y​=c2∂x2∂2y​⋯(1)

We seek a solution using the method of separation of variables, assuming the displacement y(x,t) can be written as a product of a function of x alone and a function of t alone:

y(x,t)=X(x)T(t)

Substituting this into the wave equation gives:

X(x)T′′(t)=c2X′′(x)T(t)

Separating the variables, we get:

c2T(t)T′′(t)​=X(x)X′′(x)​

Since the left side depends only on t and the right side depends only on x, both sides must be equal to a constant, which we'll call k. This leads to two ordinary differential equations:

X′′−kX=0⋯(2)

T′′−kc2T=0⋯(3)

For a physically realistic solution representing a vibrating string, the displacement must be periodic. This requires oscillatory (sinusoidal) solutions for X(x), which only occurs when k is a negative constant. Let k=−p2 for some real number p.

The equations become:

1. X′′+p2X=0, with general solution X(x)=C1​cos(px)+C2​sin(px).
    
2. T′′+p2c2T=0, with general solution T(t)=C3​cos(pct)+C4​sin(pct).
    

The general solution for the displacement is the product y(x,t)=X(x)T(t):

y(x,t)=(C1​cos(px)+C2​sin(px))(C3​cos(pct)+C4​sin(pct))⋯(4)

---

### **2. Applying Boundary and Initial Conditions**

The problem specifies the following conditions:

- **Boundary Conditions (BCs):** The string is fixed at x=0 and x=l.
    
    1. y(0,t)=0
        
    2. y(l,t)=0
        
- Initial Conditions (ICs): The string is released from rest from a given shape.
    
    3. y(x,0)=y0​sin3(lπx​)
    
    4. ∂t∂y​(x,0)=0 (released from rest)
    

**Applying the Boundary Conditions:**

- Using BC 1 (y(0,t)=0) in equation (4):
    
    0=(C1​cos(0)+C2​sin(0))T(t)=C1​T(t). For a non-trivial solution, T(t)=0, so we must have C1​=0.
    
    The solution becomes: y(x,t)=C2​sin(px)(C3​cos(pct)+C4​sin(pct)).
    
- Using BC 2 (y(l,t)=0):
    
    0=C2​sin(pl)T(t). Since C2​ cannot be zero (for a non-trivial solution), we must have sin(pl)=0.
    
    This implies pl=nπ for n=1,2,3,….
    
    This determines the eigenvalues: p=lnπ​.
    

By the Principle of Superposition, the most general solution satisfying the boundary conditions is an infinite sum of all possible solutions:

y(x,t)=n=1∑∞​sin(lnπx​)(An​cos(lnπct​)+Bn​sin(lnπct​))⋯(5)

(where An​ and Bn​ are new constants).

---

### **3. Determining the Coefficients from Initial Conditions**

**Applying the Initial Velocity Condition:**

First, we differentiate equation (5) with respect to t:

$$\frac{\partial y}{\partial t} = \sum_{n=1}^{\infty} \sin\left(\frac{n\pi x}{l}\right) \left[-A_n \frac{n\pi c}{l} \sin\left(\frac{n\pi ct}{l}\right) + B_n \frac{n\pi c}{l} \cos\left(\frac{n\pi ct}{l}\right)\right]$$Now, apply IC 4 (∂t∂y​(x,0)=0):

0=n=1∑∞​sin(lnπx​)(Bn​lnπc​)

For this Fourier series to be zero for all x, every coefficient must be zero. Thus, Bn​lnπc​=0, which implies Bn​=0 for all n.

The solution simplifies to:

y(x,t)=n=1∑∞​An​sin(lnπx​)cos(lnπct​)⋯(6)

**Applying the Initial Position Condition:**

Now, apply IC 3 (y(x,0)=y0​sin3(lπx​)) to equation (6):

$$y(x, 0) = \sum_{n=1}^{\infty} A_n \sin\left(\frac{n\pi x}{l}\right) = y_0\sin^3\left(\frac{\pi x}{l}\right)$$To find the coefficients $A_n$, we must express the initial shape as a Fourier sine series. We use the trigonometric identity:$$\sin(3\theta) = 3\sin\theta - 4\sin^3\theta$$

Rearranging for sin3θ:$$\sin^3\theta = \frac{3}{4}\sin\theta - \frac{1}{4}\sin(3\theta)$$Letting θ=lπx​, our initial condition becomes:$$y(x, 0) = y_0 \left[ \frac{3}{4}\sin\left(\frac{\pi x}{l}\right) - \frac{1}{4}\sin\left(\frac{3\pi x}{l}\right) \right]$$Now we compare this with the series expansion for y(x,0):

A1​sin(lπx​)+A2​sin(l2πx​)+A3​sin(l3πx​)+⋯=43y0​​sin(lπx​)−4y0​​sin(l3πx​)

By comparing the coefficients of the corresponding sine terms, we find:

- A1​=43y0​​
    
- A3​=−4y0​​
    
- An​=0 for all other values of n (i.e., for n=2,4,5,…)
    

---

### **4. Final Solution**

Finally, we substitute the non-zero coefficients back into our simplified solution (6). The infinite series reduces to just two terms (for n=1 and n=3):

y(x,t)=A1​sin(lπx​)cos(lπct​)+A3​sin(l3πx​)cos(l3πct​)

y(x,t)=43y0​​sin(lπx​)cos(lπct​)−4y0​​sin(l3πx​)cos(l3πct​)

Factoring out the common term 4y0​​ gives the final displacement.

Final Answer:

The displacement of the string at any point x and time t is given by:

y(x,t)=4y0​​[3sin(lπx​)cos(lπct​)−sin(l3πx​)cos(l3πct​)]