	2025-11-29 20:40

Status:

Tags:

---
# Raycast Interactor Flow with Clues

## Complete Interaction Chain
```mermaid
sequenceDiagram
    participant Player
    participant Interactor
    participant Physics
    participant Sphere
    participant ClueCatalyst
    participant MainManager
    participant JournalManager
    participant UI
    
    Player->>Interactor: Press E key
    Interactor->>Interactor: Create Ray(position, forward)
    Interactor->>Physics: Physics.Raycast(ray, out hitInfo, range)
    
    alt Hit something within range
        Physics-->>Interactor: Returns true + RaycastHit data
        Interactor->>Interactor: TryGetComponent<IInteractable>()
        
        alt Has IInteractable component
            Interactor->>Sphere: Interact()
            Sphere->>Sphere: Check if clueCatalyst != null
            Sphere->>ClueCatalyst: CreateClue()
            
            ClueCatalyst->>ClueCatalyst: Check if !clueAdded
            ClueCatalyst->>MainManager: clueNames.Add(clue)
            ClueCatalyst->>ClueCatalyst: clueAdded = true
            ClueCatalyst->>UI: notification.SetActive(true)
            ClueCatalyst->>ClueCatalyst: StartCoroutine(HideNotification)
            
            Note over ClueCatalyst,UI: Wait notificationDuration (3s)
            ClueCatalyst->>UI: notification.SetActive(false)
        end
    else Miss or no IInteractable
        Physics-->>Interactor: Returns false / null component
        Note over Interactor: Nothing happens
    end
    
    Player->>JournalManager: Press J key
    JournalManager->>JournalManager: OpenJournalBook()
    JournalManager->>UI: journalPage.SetActive(!openBook)
    JournalManager->>MainManager: Read clueNames list
    JournalManager->>JournalManager: Build clue text
    JournalManager->>UI: clueTextBox.text = clues
```

## Detailed Step-by-Step Flow

### 1. Input Detection (Interactor.cs)
```
// Every frame in Update()
if (Input.GetKeyDown(KeyCode.E))
{
    // Create a ray from camera/player forward
    Ray r = new Ray(InteractorSource.position, InteractorSource.forward);
    
    // Cast the ray
    if (Physics.Raycast(r, out RaycastHit hitInfo, InteractorRange))
    {
        // Try to get IInteractable component
        if (hitInfo.collider.gameObject.TryGetComponent(out IInteractable interactObj))
        {
            interactObj.Interact(); // Polymorphic call
        }
    }
}

```
**Variables:**
•	InteractorSource (Transform) - Usually the camera transform
•	InteractorRange (float) - Max distance to interact (e.g., 3-5 units)
•	r (Ray) - Direction from player forward
•	hitInfo (RaycastHit) - Contains collision data (collider, point, normal, etc.)
•	interactObj (IInteractable) - Interface reference to interactable object

### 2. Interface Implementation (Sphere.cs)
```
public class Sphere : MonoBehaviour, IInteractable
{
    private ClueCatalyst clueCatalyst; // Reference set in Awake()
    
    public void Interact()
    {
        // Called by Interactor when player presses E while looking at sphere
        if (clueCatalyst != null)
        {
            clueCatalyst.CreateClue();
        }
    }
}
```
**Key Points:**
•	Any GameObject with Sphere component can be interacted with
•	The sphere delegates clue creation to ClueCatalyst
•	This follows Single Responsibility Principle (separation of concerns)

### 3. Clue Creation (ClueCatalyst.cs)
```
public void CreateClue()
{
    // Prevent duplicate clues
    if (clue != null && !clueAdded)
    {
        clueAdded = true; // Mark as added
        
        // Add to global clue list
        MainManager.mainManager.clueNames.Add(clue);
        
        // Show notification UI
        if (notification != null)
        {
            notification.SetActive(true);
            StartCoroutine(HideNotificationAfterDelay());
        }
    }
}

```
**Variables:**
•	clue (string) - Serialized in Inspector (e.g., "Strange markings on the wall")
•	clueAdded (bool) - Prevents duplicate additions
•	notification (GameObject) - UI popup shown when clue collected
•	notificationDuration (float) - How long notification shows (default: 3s)

### 4. Global Storage (MainManager.cs)
```
// MainManager stores all collected clues
public List<string> clueNames = new List<string>();
```
This list is accessed by:
•	ClueCatalyst (adds clues)
•	JournalManager (reads clues for display)

### 5. Journal Display (JournalManager.cs)
```
private void Update()
{
    if (Input.GetKeyDown(KeyCode.J))
    {
        OpenJournalBook();
    }
}

public void OpenJournalBook()
{
    openBook = !openBook; // Toggle state
    CreatePage();         // Show/hide UI
    WriteQuests();        // Populate with clues
}

private void WriteQuests()
{
    if (MainManager.mainManager.clueNames.Count == 0)
    {
        // Show random placeholder text
        clueTextBox.text = noClueText[Random.Range(0, noClueText.Length)];
    }
    else
    {
        // Build clue list
        StringBuilder stringBuilder = new();
        foreach (string clue in MainManager.mainManager.clueNames)
        {
            stringBuilder.AppendLine(clue);
        }
        clueTextBox.text = stringBuilder.ToString();
    }
}

```

## Visual Raycast Diagram
```mermaid
flowchart TB
    A["Player presses E"] --> B["Create Ray from InteractorSource"]
    B --> C["Physics.Raycast(ray, hitInfo, range)"]
    C --> D{Hit detected?}
    D -->|No| Z[Nothing happens]
    D -->|Yes| E["Get hitInfo.collider.gameObject"]
    E --> F["TryGetComponent<IInteractable>()"]
    F --> G{Component exists?}
    G -->|No| Z
    G -->|Yes - Sphere found| H["Sphere.Interact()"]
    H --> I["clueCatalyst.CreateClue()"]
    I --> J{Already added?}
    J -->|Yes| K[Debug warning]
    J -->|No| L["MainManager.clueNames.Add(clue)"]
    L --> M["notification.SetActive(true)"]
    M --> N["Wait 3 seconds"]
    N --> O["notification.SetActive(false)"]
    
    style H fill:#4CAF50
    style L fill:#2196F3
    style M fill:#FF9800
```

## Key Variables Passed through the Chain
| Variable                    | Type          | Source → Destination         | Purpose                                |
| --------------------------- | ------------- | ---------------------------- | -------------------------------------- |
| InteractorSource.position   | Vector3       | Interactor → Ray             | Raycast origin point                   |
| InteractorSource.forward    | Vector3       | Interactor → Ray             | Raycast direction                      |
| InteractorRange             | float         | Interactor → Raycast         | Max interaction distance               |
| hitInfo                     | RaycastHit    | Physics → Interactor         | Collision data (collider, point, etc.) |
| hitInfo.collider.gameObject | GameObject    | Interactor → TryGetComponent | Object to check for IInteractable      |
| interactObj                 | IInteractable | TryGetComponent → Sphere     | Interface reference                    |
| clue                        | string        | ClueCatalyst → MainManager   | Clue text to add                       |
| clueAdded                   | bool          | ClueCatalyst internal        | Prevents duplicate additions           |
| MainManager.clueNames       | List<string>  | Global storage               | All collected clues                    |

## Example GameObject Setup
```
PlayerCamera (InteractorSource)
├── Interactor (script)
│   ├── InteractorSource = PlayerCamera transform
│   ├── InteractorRange = 3.0f
│   └── interactCanvas = (optional UI)

ClueObject_01
├── Sphere Collider
├── Sphere (script) → implements IInteractable
└── ClueCatalyst (script)
    ├── clue = "The door was left ajar..."
    ├── notification = NotificationUI GameObject
    └── notificationDuration = 3.0f
```

## Design Patterns Used
1.	Interface Segregation: IInteractable allows any object to be interactable
2.	Component-Based: Each responsibility is a separate component
3.	Raycast Pattern: Standard Unity interaction technique
4.	Singleton/Static: MainManager.mainManager provides global access
5.	State Management: clueAdded prevents duplicate additions
6.	Coroutine for Timing: Auto-hide notification after delay

## How to Add New Interactable Objects
```
// Create a new interactable item
public class Door : MonoBehaviour, IInteractable
{
    public void Interact()
    {
        Debug.Log("Door opened!");
        // Your door logic here
    }
}
```

The Interactor will automatically detect and call Interact() on any GameObject with an IInteractable component!

---
# Reference
