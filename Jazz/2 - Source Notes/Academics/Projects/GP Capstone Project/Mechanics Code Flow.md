	2025-11-25 09:50

Status:

Tags:

---
# Mechanics Code Flow

## 1. Gradual Heat Decrease During Overheat Cooldown

### 1. Removed Invoke() Approach
REMOVED - Instant cooldown
```cpp
Invoke("EndOverheatCooldown", overheatCooldownDuration);

private void EndOverheatCooldown()
{
    isOverheated = false;
    Debug.Log("...");
}
```

### 2. Added Coroutine with Gradual Cooldown
NEW - Gradual heat decrease

```cpp
private IEnumerator GradualCooldownCoroutine()
{
    // Calculate how fast to cool down (units per second)
    float cooldownSpeed = overheatThreshold / overheatCooldownDuration;
    // Example: 10 / 5 = 2 units per second
    
    while (currentHeat > 0f)
    {
        // Decrease heat each frame
        currentHeat -= cooldownSpeed * Time.deltaTime;
        currentHeat = Mathf.Max(0f, currentHeat);
        
        // Update slider in real-time
        if (overheatSlider != null)
        {
            overheatSlider.value = currentHeat;
        }
        
        yield return null; // Next frame
    }
    
    // Fully cooled
    currentHeat = 0f;
    isOverheated = false;
}
```

### How it works

#### Timeline Example:
```
[00:00] Flashlight ON, heat starts building
        currentHeat: 0 → 1 → 2 → 3 → ... → 9 → 10
        Slider:      ░░░░░░░░░░░░░░░░░░████████

[00:10] OVERHEAT! currentHeat = 10
        ├─ isOverheated = true (blocks activation)
        ├─ Flashlight forced OFF
        └─ Start GradualCooldownCoroutine()

[00:10 - 00:15] Cooldown phase (5 seconds)
        currentHeat gradually decreases:
        
        Time    | currentHeat | Slider Fill | Can Activate?
        --------|-------------|-------------|---------------
        00:10   | 10.0        | ████████████| ❌ No
        00:11   | 8.0         | ██████████  | ❌ No
        00:12   | 6.0         | ████████    | ❌ No
        00:13   | 4.0         | ██████      | ❌ No
        00:14   | 2.0         | ████        | ❌ No
        00:15   | 0.0         |             | ✅ YES!

[00:15] currentHeat reaches 0
        ├─ isOverheated = false
        └─ Player can now turn flashlight ON
```



---
# Reference
