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


---
# Reference
