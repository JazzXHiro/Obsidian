	2025-11-29 18:54

Status:

Tags:

---
# Explained

## Singleton Pattern Explained
A Singleton is a design pattern that ensures a class has only one instance throughout the entire application and provides a global access point to that instance.

## The Problem It Solves
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



---
# Reference
