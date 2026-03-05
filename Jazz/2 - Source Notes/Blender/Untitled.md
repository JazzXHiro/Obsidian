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

In **Blender**, to **extrude faces along their normals** (so each face moves outward/inward like inflating or shrinking), you can do it easily with this shortcut:

---

## 🔨 **Extrude Faces Along Normals**

### ✅ Steps:

1. **Go into Edit Mode** (`Tab`).
    
2. **Select the faces** you want to extrude.
    
3. Press **Alt + E** to open the special **Extrude menu**.
    
4. Choose **"Extrude Faces Along Normals"** from the list.
    
5. Move your mouse to adjust the extrusion, or type a value.
    
6. **Left-click** to confirm.
    

---

### 🧠 Why Use This?

- Regular **E** extrusion uses the average direction — good for single faces or connected surfaces.
    
- **Alt + E → Extrude Along Normals** is perfect when you want:
    
    - Walls extending outward.
        
    - Spikes or panels sticking out evenly.
        
    - Clean uniform thickness.
        

---

The **Multiresolution Modifier** (aka **Multires**) in **Blender** is a powerful tool mainly used in **sculpting** workflows. It lets you **subdivide your model** while keeping the ability to **edit it at multiple levels of detail**.

---

## 🧠 What the **Multires Modifier** Does:

- Adds multiple **levels of subdivision** to your mesh.
    
- Lets you **sculpt fine details** (like pores or wrinkles) at high resolution...
    
- ...while still being able to work on **big shapes** at lower resolution.
    
- You can go **up and down between levels** non-destructively.
    

---

## 📌 Main Difference vs Subdivision Surface:

|Feature|**Multires**|**Subdivision Surface**|
|---|---|---|
|Editable at each level|✅ Yes|❌ No|
|Sculpting support|✅ Excellent|⚠️ Not meant for sculpting|
|Animation-ready|⚠️ Usually not|✅ Yes|

---

## 🔧 How to Use Multires:

1. Select your mesh.
    
2. Go to the **Modifiers tab**.
    
3. Click **Add Modifier > Multiresolution**.
    
4. Click **Subdivide** to add more geometry.
    
5. Use **Sculpt Mode** to sculpt at different levels.
    
6. Use the **Preview / Sculpt / Render** sliders to control resolution.
    

---

### 🔁 Bonus:

- You can **bake details** from a high-res multires model onto a low-poly one (for game assets, etc.).
    

---
In **Blender**, pressing **Shift + C** does two useful things at once:

---

## 🎯 **Shift + C = Reset 3D View & Center Cursor**

### Specifically, it:

1. **Centers the 3D Cursor** to the World Origin (0, 0, 0).
    
2. **Frames All Objects** in the 3D View (zooms out to show everything).
    

---

### 🧠 Why It’s Useful:

- If you’ve lost your object in the scene or the 3D cursor is way off, **Shift + C** brings everything back into focus.
    
- Great for resetting your workspace quickly!
    

---
In **Blender**, **Face Sets** are super helpful when you're working in **Sculpt Mode**. They let you **mark parts of your mesh with color-coded regions**, so you can sculpt more precisely and organize your model better.

---

## 🧩 What Are Face Sets?

- **Face Sets** are groups of faces that you can **visually separate and isolate** in Sculpt Mode.
    
- They don’t change your geometry — they’re like **temporary masks or zones** for sculpting.
    

---

## 🎯 What You Can Do With Face Sets:

- **Hide/reveal** parts of the mesh quickly.
    
- **Protect** areas from accidental sculpting.
    
- **Smooth or deform** only specific zones.
    
- Great for detailed work (e.g. keeping the eyes untouched while sculpting the nose).
    

---

## 🔧 How to Create Face Sets:

1. **Go to Sculpt Mode**.
    
2. Use the **Face Set tools** from the left toolbar:
    
    - **Draw Face Sets**: Manually paint new face sets.
        
    - **Face Set from Visible**: Create a new set from what's visible.
        
    - **Face Set Edit**: Modify them.
        
3. Or press **Shift + W** to bring up the **Face Sets pie menu**.
    

---

## ✨ Face Set Colors:

- Each face set is colored differently.
    
- They don’t show up in Object Mode — only in **Sculpt Mode** (unless you enable them in overlays).
    

---

### 🔄 Bonus: Clear All Face Sets

- In Sculpt Mode: **Face Sets > Clear Face Sets** (in the top menu).
    

---

Render Box - Ctrl + B

Remove Render Box - Ctrl + Alt + B

Join Meshes - Ctrl + J

Recalculate normals - Shift + N

To camera - Ctrl + Alt + 0

Ctrl + b - Bevel (can be used for making steps)

