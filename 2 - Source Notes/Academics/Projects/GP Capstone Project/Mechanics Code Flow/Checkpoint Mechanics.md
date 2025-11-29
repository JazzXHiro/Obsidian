	2025-11-29 17:55

Status:

Tags:

---
# Checkpoint Mechanics

How the Checkpoint System Works
The checkpoint system uses a Singleton pattern with two main components working together:
Components Overview
1.	Checkpoint (attached to checkpoint objects in scene)
•	Detects when the player enters the checkpoint zone
•	Notifies the CheckpointManager
•	Provides visual feedback
2.	CheckpointManager (singleton, one instance in scene)
•	Stores the current active checkpoint
•	Handles player respawning
•	Manages initial spawn point

---

```mermaid
sequenceDiagram
    participant Scene as Game Scene
    participant CP as Checkpoint GameObject
    participant Player as Player (CharacterController)
    participant CPM as CheckpointManager (Singleton)
    
    Note over Scene,CPM: #35;#35; Game Initialization
    Scene->>CPM: Awake() - Create Singleton Instance
    CPM->>CPM: Set Instance reference
    CPM->>Player: Start() - Find player by tag "Player"
    CPM->>CPM: Store CharacterController reference
    CPM->>CPM: Set currentCheckpoint = initialSpawnPoint
    
    Scene->>CP: Start() - Initialize checkpoint
    CP->>CP: Set collider.isTrigger = true
    CP->>CP: Hide activatedEffect
    CP->>CP: Set hasBeenActivated = false
    
    Note over Scene,CPM: #35;#35; Player Reaches Checkpoint
    Player->>CP: OnTriggerEnter(Collider other)
    CP->>CP: Check if oneTimeUse && hasBeenActivated
    alt Already activated and one-time use
        CP-->>Player: Return (do nothing)
    else Not yet activated
        CP->>CP: Check if other.CompareTag("Player")
        alt Is Player
            CP->>CP: ActivateCheckpoint()
            CP->>CPM: Check if Instance != null
            alt CheckpointManager exists
                CP->>CPM: SetCheckpoint(transform)
                CPM->>CPM: Store currentCheckpoint = checkpointTransform
                CPM-->>CP: Checkpoint updated
                CP->>CP: Set hasBeenActivated = true
                CP->>CP: activatedEffect.SetActive(true)
                CP->>CP: Debug.Log("Checkpoint activated")
            else CheckpointManager missing
                CP->>CP: Debug.LogError("CheckpointManager not found")
            end
        end
    end
    
    Note over Scene,CPM: #35;#35; Player Dies / Respawn Triggered
    Scene->>CPM: RespawnPlayer()
    CPM->>CPM: Check if playerController && currentCheckpoint exist
    alt Can respawn
        CPM->>Player: playerController.enabled = false
        CPM->>Player: Set transform.position = currentCheckpoint.position
        CPM->>Player: Set transform.rotation = currentCheckpoint.rotation
        CPM->>Player: playerController.enabled = true
        CPM->>CPM: Debug.Log("Player respawned")
    else Cannot respawn
        CPM->>CPM: Debug.LogError("Cannot respawn")
    end
```

---
# Reference
