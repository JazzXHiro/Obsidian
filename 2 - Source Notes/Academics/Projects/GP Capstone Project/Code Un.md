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
    

---
# Reference
