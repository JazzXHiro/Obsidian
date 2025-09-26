Here is a complete solution as would be expected for a 20-mark examination question.

---

### **Objective**

To solve the one-dimensional wave equation for a vibrating string of length l with given initial conditions, using the method of separation of variables, and show that the displacement y(x,t) is given by y(x,t)=asin(lπx​)cos(lπct​).

---

### **1. The Wave Equation and Separation of Variables**

The partial differential equation governing the motion of the vibrating string (the wave equation) is:

∂t2∂2y​=c2∂x2∂2y​⋯(1)

We assume a solution of the form y(x,t)=X(x)T(t), where X is a function of x only and T is a function of t only.

Differentiating our assumed solution partially with respect to x and t:

$$\frac{\partial^2 y}{\partial x^2} = X''(x)T(t) \quad \text{and} \quad \frac{\partial^2 y}{\partial t^2} = X(x)T''(t)$$Substituting these into equation (1):

$$X(x)T''(t) = c^2 X''(x)T(t)$$To separate the variables, we divide by $c^2X(x)T(t)$:$$\frac{T''(t)}{c^2 T(t)} = \frac{X''(x)}{X(x)}$$Since the left side is a function of $t$ only and the right side is a function of $x$ only, they must both be equal to a common constant, say $k$.$$\frac{X''}{X} = k \quad \text{and} \quad \frac{T''}{c^2 T} = k$$

This gives us two ordinary differential equations:

X′′−kX=0⋯(2)

T′′−kc2T=0⋯(3)

For a vibrating string, the solution must be periodic (oscillatory). This requires sinusoidal solutions, which only occurs if the constant k is negative. Let k=−p2, where p is a real number.

Equation (2) becomes: X′′+p2X=0. The general solution is:

$$X(x) = C_1 \cos(px) + C_2 \sin(px)$$Equation (3) becomes: T′′+p2c2T=0. The general solution is:$$T(t) = C_3 \cos(pct) + C_4 \sin(pct)$$Thus, the general solution for the displacement is:

y(x,t)=X(x)T(t)=(C1​cos(px)+C2​sin(px))(C3​cos(pct)+C4​sin(pct))⋯(4)

---

### **2. Boundary and Initial Conditions**

From the problem statement, we can establish the following conditions:

Boundary Conditions (BCs):

The string is fastened at two points l apart (at x=0 and x=l). Therefore, the displacement at the ends is always zero.

1. y(0,t)=0 for all t≥0
    
2. y(l,t)=0 for all t≥0
    

Initial Conditions (ICs):

The string is released from rest at t=0 from an initial shape.

3. Initial displacement: y(x,0)=asin(lπx​)

4. Initial velocity: ∂t∂y​(x,0)=0 (since it is "released from rest")

---

### **3. Applying the Boundary Conditions**

We apply the BCs to our general solution (4).

Applying BC 1: y(0,t)=0

0=(C1​cos(0)+C2​sin(0))T(t)=(C1​⋅1+0)T(t)=C1​T(t)

For a non-trivial solution, T(t)=0, which implies C1​=0.

The solution simplifies to:

y(x,t)=C2​sin(px)(C3​cos(pct)+C4​sin(pct))

Applying BC 2: y(l,t)=0

$$0 = C_2 \sin(pl) T(t)$$For a non-trivial solution, $C_2 \neq 0$ and $T(t) \neq 0$. This forces the condition:$$\sin(pl) = 0$$

This is true if pl=nπ for n=1,2,3,…

This determines the possible values for p, known as eigenvalues:

$$p = \frac{n\pi}{l}$$The solution for each integer n is of the form:

yn​(x,t)=sin(lnπx​)(An​cos(lnπct​)+Bn​sin(lnπct​))

where An​ and Bn​ are new arbitrary constants.

By the Principle of Superposition, the most general solution is the sum of all possible solutions:

y(x,t)=n=1∑∞​sin(lnπx​)(An​cos(lnπct​)+Bn​sin(lnπct​))⋯(5)

---

### **4. Applying the Initial Conditions**

We now use the ICs to find the specific values of An​ and Bn​.

Applying IC 3: y(x,0)=asin(lπx​)

Setting t=0 in equation (5):

y(x,0)=n=1∑∞​sin(lnπx​)(An​cos(0)+Bn​sin(0))

$$y(x, 0) = \sum_{n=1}^{\infty} A_n \sin\left(\frac{n\pi x}{l}\right)$$Equating this to the given initial displacement:

asin(lπx​)=A1​sin(lπx​)+A2​sin(l2πx​)+A3​sin(l3πx​)+…

By comparing the coefficients of this Fourier sine series, we deduce that:

A1​=a,andAn​=0 for n>1

Applying IC 4: ∂t∂y​(x,0)=0

First, differentiate equation (5) with respect to t:

$$\frac{\partial y}{\partial t} = \sum_{n=1}^{\infty} \sin\left(\frac{n\pi x}{l}\right) \left[-A_n \frac{n\pi c}{l} \sin\left(\frac{n\pi ct}{l}\right) + B_n \frac{n\pi c}{l} \cos\left(\frac{n\pi ct}{l}\right)\right]

$$Now, set $t=0$:$$

\frac{\partial y}{\partial t}(x, 0) = \sum_{n=1}^{\infty} \sin\left(\frac{n\pi x}{l}\right) \left( B_n \frac{n\pi c}{l} \right)$$Since the initial velocity is zero, we have:$$0 = \sum_{n=1}^{\infty} \left( B_n \frac{n\pi c}{l} \right) \sin\left(\frac{n\pi x}{l}\right)$$For this equality to hold for all x, every coefficient must be zero. Thus, for every n:

Bn​lnπc​=0⟹Bn​=0

---

### **5. Final Solution**

Substituting the determined coefficients (A1​=a, An>1​=0, and Bn​=0 for all n) back into the general solution (5), the infinite series collapses to a single term where n=1:

y(x,t)=sin(l1⋅πx​)(A1​cos(l1⋅πct​)+B1​sin(l1⋅πct​))y(x,t)=sin(lπx​)(acos(lπct​)+0)y(x,t)=asin(lπx​)cos(lπct​)

This is the required expression for the displacement of the string.

**Hence Shown.**