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

# Detailed Variable Flow

## Checkpoint.cs Variables

| Variable         | Type       | Purpose                 | Flow                                                  |
| ---------------- | ---------- | ----------------------- | ----------------------------------------------------- |
| playerTag        | string     | Tag to identify player  | Set in Inspector → Used in OnTriggerEnter()           |
| activatedEffect  | GameObject | Visual feedback object  | Disabled in Start() → Enabled in ActivateCheckpoint() |
| oneTimeUse       | bool       | Prevent reactivation    | Set in Inspector → Checked in OnTriggerEnter()        |
| hasBeenActivated | bool       | Tracks activation state | false → true when activated                           |

## CheckpointManager.cs Variables

| Variable          | Type                     | Purpose              | Flow                                                        |
| ----------------- | ------------------------ | -------------------- | ----------------------------------------------------------- |
| Instance          | static CheckpointManager | Singleton reference  | Set in Awake() → Accessed by Checkpoint.cs                  |
| initialSpawnPoint | Transform                | First spawn location | Set in Inspector → Assigned to currentCheckpoint in Start() |
| currentCheckpoint | Transform                | Active checkpoint    | Updated by SetCheckpoint() → Used in RespawnPlayer()        |
| playerController  | CharacterController      | Player reference     | Found in Start() → Used to move player in RespawnPlayer()   |

# Key Function Call Chain

## 1. Checkpoint Activation

```
Player enters trigger
    ↓
OnTriggerEnter(Collider other)
    ↓
CompareTag("Player") [checks if collider is player]
    ↓
ActivateCheckpoint()
    ↓
CheckpointManager.Instance.SetCheckpoint(transform) [passes checkpoint's Transform]
    ↓
currentCheckpoint = checkpointTransform [stored in manager]
```

## 2. Player Respawn
```
RespawnPlayer() [called by death system/other script]
    ↓
playerController.enabled = false [required for position change]
    ↓
playerController.transform.position = currentCheckpoint.position
playerController.transform.rotation = currentCheckpoint.rotation
    ↓
playerController.enabled = true [re-enable physics]

```

# Important Design Patterns

1.	Singleton Pattern: Only one CheckpointManager exists, accessible via CheckpointManager.Instance
2.	Observer Pattern: Checkpoints notify the manager when activated
3.	One-time Trigger: hasBeenActivated flag prevents repeated activation (if oneTimeUse = true)

# The Complete Game Loop
```mermaid
flowchart TD
    Start["Game Starts"] --> Init["Initialization Phase"]
    Init --> CPMInit["CheckpointManager.Awake()<br/>- Creates Singleton<br/>- Finds Player"]
    Init --> CPMStart["CheckpointManager.Start()<br/>- Sets currentCheckpoint = initialSpawnPoint"]
    Init --> CPInit["Checkpoint.Start()<br/>- Sets collider.isTrigger = true<br/>- Hides activatedEffect"]
    
    CPMStart --> Gameplay["Player Exploring"]
    CPInit --> Gameplay
    
    Gameplay --> SanityDrain["SanityManager.Update()<br/>Coroutine Running"]
    
    SanityDrain --> CheckConditions{"Check Conditions"}
    CheckConditions -->|"Flashlight ON"| NoChange["change = 0<br/>(sanity paused)"]
    CheckConditions -->|"Under Lamp"| Regen["change = +replenishRate * delta"]
    CheckConditions -->|"In Darkness"| Drain["change = -drainRate * difficulty * delta"]
    
    NoChange --> ApplySanity["sanitySlider.value += change"]
    Regen --> ApplySanity
    Drain --> ApplySanity
    
    ApplySanity --> CheckDeath{"sanity <= 0?"}
    CheckDeath -->|"No"| Gameplay
    CheckDeath -->|"Yes"| Death["HandleDeath() Coroutine"]
    
    Death --> SetDead["isDead = true"]
    SetDead --> Wait["Wait respawnDelay seconds"]
    Wait --> Respawn["CheckpointManager.Instance.RespawnPlayer()"]
    
    Respawn --> DisableCC["playerController.enabled = false"]
    DisableCC --> MovePlayer["transform.position = currentCheckpoint.position<br/>transform.rotation = currentCheckpoint.rotation"]
    MovePlayer --> EnableCC["playerController.enabled = true"]
    EnableCC --> ResetSanity["sanitySlider.value = fullSanity"]
    ResetSanity --> ResetFlag["isDead = false"]
    ResetFlag --> Gameplay
    
    Gameplay --> PlayerMove["Player Moves Through World"]
    PlayerMove --> HitCP{"Enters Checkpoint<br/>Trigger?"}
    HitCP -->|"No"| Gameplay
    HitCP -->|"Yes"| CPTrigger["Checkpoint.OnTriggerEnter()"]
    
    CPTrigger --> CheckActivated{"oneTimeUse &&<br/>hasBeenActivated?"}
    CheckActivated -->|"Yes"| Gameplay
    CheckActivated -->|"No"| CheckTag{"other.CompareTag<br/>('Player')?"}
    CheckTag -->|"No"| Gameplay
    CheckTag -->|"Yes"| Activate["ActivateCheckpoint()"]
    
    Activate --> SaveCP["CheckpointManager.Instance.SetCheckpoint(transform)"]
    SaveCP --> StoreTransform["currentCheckpoint = checkpointTransform"]
    StoreTransform --> MarkActivated["hasBeenActivated = true"]
    MarkActivated --> ShowEffect["activatedEffect.SetActive(true)"]
    ShowEffect --> Gameplay
    
    style Death fill:#ff6b6b
    style Respawn fill:#4ecdc4
    style Activate fill:#95e1d3
    style SanityDrain fill:#ffe66d
```

#

---
# Reference
