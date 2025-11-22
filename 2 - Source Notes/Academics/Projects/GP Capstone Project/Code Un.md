	2025-11-21 13:40

Status:

Tags:

---
# Code Un

## 1. Mathf.Clamp()

`Mathf.Clamp()` in Unity takes **three parameters**:

### **Mathf.Clamp(value, min, max)**

1. **value** → the number you want to limit
    
2. **min** → the minimum allowed value
    
3. **max** → the maximum allowed value
    

---

### In your example:

```csharp
Mathf.Clamp(verticalRotation - rotationAmount, -upDownLookRange, upDownLookRange);
```

- **value** = `verticalRotation - rotationAmount`  
    This is the new rotation you want to apply.
    
- **min** = `-upDownLookRange`  
    This is how far up you can look.
    
- **max** = `upDownLookRange`  
    This is how far down you can look.


## 2. SerializedField

`[SerializeField]` is a Unity attribute that you put **before a private field** to make it **visible and editable in the Inspector**.

### ✔ Without SerializeField

Normally, **private** variables do **not** show up in the Inspector:

```csharp
private float speed;   // won't show in Inspector
```

### ✔ With SerializeField

Adding `[SerializeField]` tells Unity:

> “Even though this field is private, expose it in the Inspector.”

```csharp
[SerializeField] 
private float speed;   // will show in Inspector
```

### 📌 Why use it?

- **Keep variables private** (good encapsulation)
    
- **Still adjust values in Inspector**
    
- **Better control over what designers/team members can tweak**
    

## 3. Awake()
`Awake()` is one of Unity’s **lifecycle methods** — special functions Unity calls automatically at specific times.  
You don’t call `Awake()` yourself; Unity calls it for you.

Here’s exactly what it does:

---

# ✅ **What `Awake()` does**

`Awake()` is called **as soon as the script instance is loaded**, _before the game starts running_.

That means:

- It’s called **before Start()**
    
- It’s called even if the object is **disabled** (unlike Start())
    
- It is the **first function Unity calls** in your script’s lifetime
    
- All `Awake()` functions in all scripts run **before** any `Start()` runs
    

---

# 🧠 **When does Unity run it?**

Unity calls `Awake()` when:

- The GameObject containing the script is created
    
- A scene loads
    
- A prefab is instantiated
    
- Domain reload happens in Play mode
    

This happens **before** gameplay logic begins.

---

# 🔍 **`Awake()` vs `Start()`**

|Feature|Awake()|Start()|
|---|---|---|
|Called when?|As soon as script loads|Right before the first frame|
|Order|All Awakes → then all Starts|After all Awakes|
|Object must be enabled?|**No**, Awake is called even if disabled|**Yes**, Start is only called if enabled|
|Good for|Setup, component getting|Logic that depends on other objects being initialized|

## 4. if (current && !lastInputState)

```csharp
private void Update()
{
    if (inputHandler != null)
    {
        bool current = inputHandler.FlashlightTriggered;
        if (current && !lastInputState)
        {
            ToggleFlashlight();
        }
        lastInputState = current;
        return;
    }
}
```

# 🔍 **What are `current` and `lastInputState`?**

### `current`

- This is the **current frame's flashlight button state**.
    
- `true` if the F key (or your input action) **is being pressed right now**.
    
- `false` if it is not.
    

### `lastInputState`

- This is the **previous frame's button state**.
    
- It lets us detect changes from one frame to the next.
    

---

# 🎉 **In simple words:**

### 👉 It means **"Did the player just press the button this frame?"**

Not holding…  
Not releasing…  
JUST **the moment they press it**.

---

# 🎮 Why do we need this?

Because if you use:

```csharp
if(current)
    ToggleFlashlight();
```

Then while you hold the F key:

- The flashlight would toggle **EVERY FRAME**
    
- At 60 FPS it would flicker like crazy
    

To avoid that, we detect only the **moment the key is first pressed**.

This is called **edge detection** (detecting the rising edge of the signal).

---

# 📌 Example timeline (frames)

| Frame | Key Held? (`current`) | Previous (`lastInputState`) | Condition | Result    |
| ----- | --------------------- | --------------------------- | --------- | --------- |
| 1     | false                 | false                       | false     | nothing   |
| 2     | **true**              | false                       | **true**  | toggle!   |
| 3     | true                  | true                        | false     | no toggle |
| 4     | true                  | true                        | false     | no toggle |
| 5     | false                 | true                        | false     | no toggle |

This is exactly why the flashlight toggles cleanly ON/OFF **once per key press**.

## 5. Dialogue System

1. Using Queue for dialogue storage and handling (cus FIFO).

## 6. FindFirstObjectByType

Unity is giving you that warning **because Unity changed how object-finding works in newer engine versions**.

---

## ✅ **Why is `FindObjectOfType()` deprecated?**

Unity deprecated it because:

### **1. It is SLOW**

`FindObjectOfType()` scans the entire scene every time it runs.  
If you call it often, it becomes expensive—especially in big scenes.

Unity introduced faster and safer versions like:

- `FindFirstObjectByType<T>()` → reliable & safer
    
- `FindAnyObjectByType<T>()` → fastest but may return any instance
    

---

### **2. It can behave unpredictably**

If you have **multiple objects** of the same type, `FindObjectOfType()` might return a random one depending on load order.

The new API makes the intent clearer:

- _First_ = deterministic
    
- _Any_ = performance-focused
    

---

### **3. Unity is cleaning up old API**

They are slowly removing older methods to modernize the engine.

---

## 🔍 Example of the new recommended approach

```csharp
DialogueManager manager = FindFirstObjectByType<DialogueManager>();
```

This is:

- Faster
    
- More consistent
    
- The supported method going forward
    

---

## 🧠 Should you worry?

No — it’s just a **warning**, not an error.  
Your game will still work.

Unity just wants you to stop using the old method before they remove it in future updates.

---
# Reference
