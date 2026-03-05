	2025-11-29 18:54

Status:

Tags:

---
# Explained

## 1. Singleton Pattern Explained
A Singleton is a design pattern that ensures a class has only one instance throughout the entire application and provides a global access point to that instance.

### The Problem It Solves
Imagine you need a manager that:
•	Should only exist once in the game
•	Needs to be accessible from anywhere in your code
•	Should survive across different parts of the game

**Without SIngleton**
```
// BAD: Multiple managers could exist!
CheckpointManager manager1 = FindObjectOfType<CheckpointManager>();
CheckpointManager manager2 = new CheckpointManager(); // Oops! Two managers!
```

**With Singleton**
```
// GOOD: Always references the same instance
CheckpointManager.Instance.SetCheckpoint(transform);
CheckpointManager.Instance.RespawnPlayer();
```

### How Your CheckpointManager Uses It
```
public class CheckpointManager : MonoBehaviour
{
    // 1️⃣ STATIC INSTANCE - Global access point
    public static CheckpointManager Instance { get; private set; }
    
    private void Awake()
    {
        // 2️⃣ SINGLETON LOGIC - Ensures only one exists
        if (Instance != null && Instance != this)
        {
            Destroy(this.gameObject);  // Kill duplicate
            return;
        }
        Instance = this;  // Set as THE instance
    }
}
```

### Singleton Pattern Breakdown
```
public static CheckpointManager Instance { get; private set; }
```

| Keyword               | Purpose                                             |     |
| --------------------- | --------------------------------------------------- | --- |
| public                | Any script can access it                            |     |
| static                | Belongs to the class itself, not individual objects |     |
| Instance              | The single shared reference                         |     |
| { get; private set; } | Anyone can read, only this class can write          |     |

**What this means:**
•	CheckpointManager.Instance is accessible from any script
•	There's only one Instance variable for the entire game
•	You can't accidentally overwrite it from outside

---
# Reference
