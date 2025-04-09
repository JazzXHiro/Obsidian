Shift + A
![[Pasted image 20250409000804.png]]]

Ctrl + R - Loop Cut
(for number of cuts use number buttons)

Subdivision
In **Blender**, **Subdivision** (short for _Subdivision Surface_) is used to **smooth** and **add more geometry** to your model by dividing its faces into smaller ones. It's perfect for creating high-poly, smooth shapes from low-poly models.

---

## 🔍 What Subdivision Does:

- **Adds more geometry** to your mesh.
    
- **Smooths out** sharp edges and corners.
    
- Makes the model look **more organic and detailed**.
    

---

## 🧱 Example:

- A cube with subdivision becomes a **rounded shape**.
    
- A low-poly character becomes **smooth and high-res**.
    

---

## ✨ How to Use It:

### 📦 Add Subdivision Surface Modifier:

1. Select your object.
    
2. Go to the **Modifiers tab** (🔧 wrench icon).
    
3. Click **Add Modifier** > **Subdivision Surface**.
    

### ⚙️ Settings:

- **Levels Viewport** – How smooth it looks in the 3D view.
    
- **Render** – How smooth it will be when you render the image.
    
- Higher levels = smoother model, but also **more geometry** = heavier on performance.
    

---

### 🔧 Shortcut (Quick Preview):

- Press **Ctrl + 1, 2, 3...** to quickly apply Subdivision levels in the viewport.

---

- Can only apply modifiers outside of the edit mode(order of applying matters).


Holding **Alt** while selecting a vertex (or edge or face) in **Blender** does something super useful:

---

## 🧠 **Alt + Left Click** in Edit Mode:

🔹 **Selects an entire edge loop or face loop**!

---

### 📌 What That Means:

- If you're in **Vertex**, **Edge**, or **Face Select** mode:
    
    - **Alt + Left Click** on an edge or face = Blender selects the **looped path** that goes all the way around.
        

---

### ✅ Use Cases:

- Perfect for selecting loops around a cylinder, ring, or any circular structure.
    
- Great for modeling or cleaning up geometry.
    

---

### 🎯 Bonus:

- Hold **Shift + Alt + Left Click** to **add more loops** to your selection (multi-select).
    
- Works best on clean, quad-based topology.