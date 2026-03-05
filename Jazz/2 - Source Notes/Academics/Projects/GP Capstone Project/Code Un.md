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
2. Press E to intiate dialogue and Left mouse click to cycle through the dialogues.
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

### 🔍 Example of the new recommended approach

```csharp
DialogueManager manager = FindFirstObjectByType<DialogueManager>();
```

This is:

- Faster
    
- More consistent
    
- The supported method going forward
    

---

### 🧠 Should you worry?

No — it’s just a **warning**, not an error.  
Your game will still work.

Unity just wants you to stop using the old method before they remove it in future updates.

## 7. public bool IsOn => isOn;

`public bool IsOn => isOn;` is just a **short-hand way of writing a getter property** in C#.

### Long explanation (simple):

Normally you would write this:

```csharp
public bool IsOn
{
    get { return isOn; }
}
```

But C# allows a shorter syntax:

```csharp
public bool IsOn => isOn;
```

This means:

- **IsOn** is a public _read-only property_
    
- It returns the value of the private variable **isOn**
    
- You cannot set it from outside, but you can _read_ it
    

### Why use this?

So other scripts (like your `SanityManager`) can check:

```csharp
if (flashlightController.IsOn)
{
    // Flashlight is turned on
}
```

But they **cannot change** `isOn` directly — good for safety.

## 8. IEnumerator

`IEnumerator` in Unity is used for **coroutines** — one of the most important systems in Unity scripting.

# ✅ What `IEnumerator` Does in Unity (Simple Explanation)

### **`IEnumerator` lets you write a function that can PAUSE and RESUME execution.**

Unity uses this to run **coroutines**, which let you:

- wait for seconds
    
- wait for frames
    
- run something over time
    
- perform gradual changes (animations, sanity drain, stamina regen)
    
- avoid freezing the game while doing long operations
    

A coroutine **does not block the game** like a normal `Update()`.

---

# 🧠 With `IEnumerator`

You can **pause** execution using `yield return`.

```csharp
IEnumerator DoSomething()
{
    Debug.Log("Start");

    yield return new WaitForSeconds(2f); // ⏳ pause for 2 seconds

    Debug.Log("End");
}
```

---

# 🚀 How to start a coroutine

```csharp
StartCoroutine(DoSomething());
```

Unity will run the function, stop at `yield return`, wait for the condition to finish, then resume.

---

# 🟦 Common `yield return` options

### ✔ `yield return null;`

Wait 1 frame.

### ✔ `yield return new WaitForSeconds(1f);`

Wait for 1 second.

### ✔ `yield return new WaitUntil(() => condition);`

Wait until some condition becomes true.

### ✔ `yield return new WaitForEndOfFrame();`

Wait until frame finishes rendering.

---

# 🎮 Why Unity Uses `IEnumerator`

Because Unity is **single-threaded** (main game thread). A coroutine lets you break an operation into steps without blocking the game loop.

Unity calls your coroutine a little bit every frame, which is perfect for:

- damage over time
    
- recharging stamina
    
- smooth UI animations
    
- cooldown timers
    
- sanity drain systems (like your game!)
    
- fade in/out screens
    
- loading sequences
    

---

# ✔ Example from your own sanity system

In your file’s `SanityLoop()` (you uploaded this file):  
Your code uses `IEnumerator` so it can:

- continuously decrease/replenish sanity
    
- run once per frame
    
- pause each frame using `yield return null`
    

Your uploaded script essentially does:

```csharp
IEnumerator SanityLoop()
{
    while (true)
    {
        // compute sanity
        yield return null; // pause until next frame
    }
}
```

Without `IEnumerator`, this would freeze Unity instantly.

## 9. Invoke("EndOverheatCooldown", overheatCooldownDuration);

This is Unity's delayed method invocation system. It schedules a method to be called after a specified delay.

---
# Reference
