	2025-11-29 19:29

Status:

Tags:

---
# CheckpointManager.cs

## 1.

```
    private void Awake()
    {
        if (Instance != null && Instance != this)
        {
            Destroy(this.gameObject);
            return;
        }
        Instance = this;
    }
```



---
# Reference
