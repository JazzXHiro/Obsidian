	2025-11-30 17:57

Status:

Tags:

---
# Updated DialogueSys

## System Architecture Overview
```
┌─────────────────────────────────────────────────────────────────┐
│                     DIALOGUE SYSTEM FLOW                         │
└─────────────────────────────────────────────────────────────────┘

Trigger Sources:
├─ ClueCatalyst (clue collection)
├─ DialogueAreaTrigger (area entry/exit)
└─ DialogueTrigger (manual/button press)
           ↓
    DialogueEventManager (event broadcasting)
           ↓
    DialogueEventListener (event matching & routing)
           ↓
    DialogueManager (UI display & text animation)
```

## Complete Flow Diagram

```mermaid
sequenceDiagram
    participant Player
    participant Interactor
    participant ClueCatalyst
    participant DialogueEventManager
    participant DialogueEventListener
    participant CharacterDialogueConfig
    participant Dialogue
    participant DialogueManager
    participant UI

    Player->>Interactor: Press E key
    Interactor->>Interactor: Physics.Raycast()
    Interactor->>ClueCatalyst: TryGetComponent<IInteractable>()
    Interactor->>ClueCatalyst: Interact()
    
    ClueCatalyst->>ClueCatalyst: CreateClue()
    Note over ClueCatalyst: Check: clue != null && !clueAdded
    ClueCatalyst->>MainManager: clueNames.Add(clue)
    ClueCatalyst->>ClueCatalyst: StartCoroutine(TriggerDialogueWithDelay)
    
    Note over ClueCatalyst: Wait dialogueDelay seconds
    
    ClueCatalyst->>DialogueEventManager: TriggerEvent(OnClueFound, "Key")
    Note over DialogueEventManager: Create DialogueEventData
    DialogueEventManager->>DialogueEventManager: OnDialogueEventTriggered?.Invoke(eventData)
    
    DialogueEventManager-->>DialogueEventListener: Event Broadcast
    DialogueEventListener->>DialogueEventListener: HandleDialogueEvent(eventData)
    
    loop For each CharacterDialogueConfig
        DialogueEventListener->>CharacterDialogueConfig: Check eventDialogues list
        CharacterDialogueConfig-->>DialogueEventListener: EventDialogue entries
        
        loop For each EventDialogue
            DialogueEventListener->>DialogueEventListener: IsEventMatch(eventDialogue, eventData)
            Note over DialogueEventListener: Match: eventType && customEventName
            
            alt Match Found
                DialogueEventListener->>DialogueEventListener: Check triggeredOnceEvents HashSet
                alt Not Triggered Before
                    DialogueEventListener->>DialogueEventListener: matches.Add(eventDialogue)
                    DialogueEventListener->>DialogueEventListener: triggeredOnceEvents.Add(key)
                end
            end
        end
    end
    
    DialogueEventListener->>DialogueEventListener: matches.Sort(by priority)
    
    alt delay > 0
        DialogueEventListener->>DialogueEventListener: StartCoroutine(TriggerDialogueWithDelay)
        Note over DialogueEventListener: Wait delay seconds
    end
    
    DialogueEventListener->>DialogueEventListener: TriggerDialogue(dialogue)
    Note over DialogueEventListener: Check: isShowingDialogue?
    
    alt No Active Dialogue
        DialogueEventListener->>DialogueEventListener: isShowingDialogue = true
        DialogueEventListener->>DialogueManager: StartDialogue(dialogue)
        DialogueEventListener->>DialogueEventListener: StartCoroutine(WaitForDialogueEnd)
    else Dialogue Active & Queue Enabled
        DialogueEventListener->>DialogueEventListener: dialogueQueue.Enqueue(action)
    end
    
    DialogueManager->>DialogueManager: StartDialogue(dialogue)
    DialogueManager->>UI: animator.SetBool("IsOpen", true)
    DialogueManager->>UI: nameText.text = dialogue.name
    
    loop For each sentence in dialogue.sentences
        DialogueManager->>DialogueManager: sentences.Enqueue(sentence)
    end
    
    DialogueManager->>DialogueManager: dialogueActive = true
    DialogueManager->>DialogueManager: DisplayNextSentence()
    DialogueManager->>DialogueManager: sentences.Dequeue()
    DialogueManager->>DialogueManager: StartCoroutine(TypeSentence)
    
    loop For each character in sentence
        DialogueManager->>UI: dialogueText.text += letter
        Note over DialogueManager: Wait typingSpeed seconds
    end
    
    Player->>DialogueManager: Click Left Mouse Button
    DialogueManager->>DialogueManager: DisplayNextSentence()
    
    alt More Sentences
        Note over DialogueManager: Display next sentence
    else No More Sentences
        DialogueManager->>DialogueManager: EndDialogue()
        DialogueManager->>UI: animator.SetBool("IsOpen", false)
        DialogueManager->>DialogueManager: dialogueActive = false
        DialogueManager->>DialogueEventListener: OnDialogueEnded()
        
        DialogueEventListener->>DialogueEventListener: isShowingDialogue = false
        
        alt Queue Has Items
            DialogueEventListener->>DialogueEventListener: dialogueQueue.Dequeue()
            DialogueEventListener->>DialogueManager: StartDialogue(nextDialogue)
        end
    end
```

## Flow Breakdown

### Phase 1: Trigger Initiation

#### Option A: Clue Collection via ClueCatalyst

```
// 1. Player presses E near clue object
Input.GetKeyDown(KeyCode.E) // in Interactor.Update()

// 2. Interactor raycasts forward
Ray r = new Ray(InteractorSource.position, InteractorSource.forward);
Physics.Raycast(r, out RaycastHit hitInfo, InteractorRange)

// 3. Checks for IInteractable component
hitInfo.collider.gameObject.TryGetComponent(out IInteractable interactObj)

// 4. Calls Interact() method
interactObj.Interact() // → ClueCatalyst.Interact()
```

**Variables Passed:**
•	InteractorSource.position: Vector3 (camera position)
•	InteractorSource.forward: Vector3 (camera forward direction)
•	InteractorRange: float (raycast distance, e.g., 3.0f)
•	hitInfo: RaycastHit (collision data)
•	interactObj: IInteractable (the ClueCatalyst instance)

```
// 5. ClueCatalyst.Interact() → CreateClue()
public void Interact()
{
    CreateClue();
}

// 6. CreateClue() executes
public void CreateClue()
{
    // Validation
    if (clue != null && !clueAdded)
    {
        clueAdded = true;
        MainManager.mainManager.clueNames.Add(clue);
        
        // Determine event name
        string eventName = string.IsNullOrEmpty(customDialogueEventName) 
            ? clue 
            : customDialogueEventName;
        
        // Trigger with delay
        if (dialogueDelay > 0)
        {
            StartCoroutine(TriggerDialogueWithDelay(eventName));
        }
        else
        {
            DialogueEventManager.Instance.TriggerEvent(
                DialogueEventType.OnClueFound, 
                eventName
            );
        }
    }
}
```

**Variables at this point:**
•	clue: string (e.g., "Key")
•	clueAdded: bool (false → true)
•	customDialogueEventName: string (empty or custom name)
•	eventName: string (resolved to "Key")
•	dialogueDelay: float (e.g., 0.5f)

#### Option B: Area Trigger via DialogueAreaTrigger

```
// 1. Player enters trigger collider
void OnTriggerEnter(Collider other)
{
    if (!ShouldTrigger(other)) return;
    
    if (triggerMode == TriggerMode.OnEnter || triggerMode == TriggerMode.Both)
    {
        TriggerDialogueEvent();
    }
}

// 2. Validation check
private bool ShouldTrigger(Collider other)
{
    // Check player tag
    if (!other.CompareTag(playerTag)) // "Player"
        return false;
    
    // Check trigger-once logic
    if (triggerOnce && hasTriggered)
        return false;
    
    return true;
}

// 3. Trigger event
private void TriggerDialogueEvent()
{
    if (triggerOnce)
    {
        hasTriggered = true;
    }
    
    if (dialogueDelay > 0)
    {
        StartCoroutine(TriggerWithDelay());
    }
    else
    {
        TriggerEvent();
    }
}

// 4. Call event manager
private void TriggerEvent()
{
    DialogueEventManager.Instance.TriggerEvent(eventType, eventName);
}
```

**Variables Passed:**
•	other: Collider (player's collider)
•	playerTag: string ("Player")
•	eventType: DialogueEventType (e.g., Custom)
•	eventName: string (e.g., "EntranceArea")
•	dialogueDelay: float (e.g., 0.5f)
•	triggerOnce: bool
•	hasTriggered: bool (false → true)

### Phase 2: Event Broadcasting

```
// DialogueEventManager.TriggerEvent()
public void TriggerEvent(
    DialogueEventType eventType,  // OnClueFound or Custom
    string customName = "",        // "Key" or "EntranceArea"
    object data = null             // Optional additional data
)
{
    // 1. Create event data wrapper
    var eventData = new DialogueEventData(eventType, customName, data);
    
    // 2. Log if debug enabled
    if (enableDebugLogs)
    {
        Debug.Log($"[DialogueEventManager] Triggering event: {eventType} (Custom: {customName})");
    }
    
    // 3. Broadcast to all listeners
    OnDialogueEventTriggered?.Invoke(eventData);
}
```

#### DialogueEventData Structure:

```
public class DialogueEventData
{
    public DialogueEventType eventType;    // OnClueFound, Custom, etc.
    public string customEventName;         // "Key", "EntranceArea"
    public object additionalData;          // Optional extra data
}

```

##### Example Event Data:

```
// For clue collection:
eventData = {
    eventType: DialogueEventType.OnClueFound,
    customEventName: "Key",
    additionalData: null
}

// For area trigger:
eventData = {
    eventType: DialogueEventType.Custom,
    customEventName: "EntranceArea",
    additionalData: null
}
```

### Phase 3: Event Listening & Matching

```
// DialogueEventListener.HandleDialogueEvent()
private void HandleDialogueEvent(DialogueEventData eventData)
{
    Debug.Log($"[DialogueEventListener] Received event: {eventData.eventType} (Custom: '{eventData.customEventName}')");
    
    // 1. Initialize matches list
    List<CharacterDialogueConfig.EventDialogue> matches = new List<CharacterDialogueConfig.EventDialogue>();
    
    // 2. Search through all character configs
    foreach (var config in characterConfigs) // e.g., PlayerClueDialogues
    {
        if (config == null) continue;
        
        // 3. Check each event dialogue in the config
        foreach (var eventDialogue in config.eventDialogues)
        {
            // 4. Match check
            if (IsEventMatch(eventDialogue, eventData))
            {
                Debug.Log($"[DialogueEventListener] Found match in config '{config.characterName}'!");
                
                // 5. Check trigger-once logic
                string key = $"{config.characterName}_{eventData.eventType}_{eventDialogue.customEventName}";
                // Example key: "Player_OnClueFound_Key"
                
                if (eventDialogue.triggerOnce && triggeredOnceEvents.Contains(key))
                {
                    Debug.Log($"[DialogueEventListener] Skipping - already triggered once");
                    continue;
                }
                
                // 6. Add to matches
                matches.Add(eventDialogue);
                
                // 7. Mark as triggered
                if (eventDialogue.triggerOnce)
                {
                    triggeredOnceEvents.Add(key);
                }
            }
        }
    }
    
    Debug.Log($"[DialogueEventListener] Total matches found: {matches.Count}");
    
    // 8. Handle no matches
    if (matches.Count == 0)
    {
        Debug.LogWarning($"[DialogueEventListener] No matching dialogue found");
        return;
    }
    
    // 9. Sort by priority (highest first)
    matches.Sort((a, b) => b.priority.CompareTo(a.priority));
    
    // 10. Trigger all matches
    foreach (var match in matches)
    {
        if (match.dialogue == null)
        {
            Debug.LogError("[DialogueEventListener] Dialogue reference is null!");
            continue;
        }
        
        if (match.delay > 0)
        {
            StartCoroutine(TriggerDialogueWithDelay(match.dialogue, match.delay));
        }
        else
        {
            TriggerDialogue(match.dialogue);
        }
    }
}
```

#### Matching Logic:

```
private bool IsEventMatch(
    CharacterDialogueConfig.EventDialogue eventDialogue,
    DialogueEventData eventData
)
{
    // 1. Check event type
    if (eventDialogue.eventType != eventData.eventType)
    {
        Debug.Log($"Event type mismatch: {eventDialogue.eventType} != {eventData.eventType}");
        return false;
    }
    
    // 2. Check custom name (for Custom events or events with names)
    if (eventData.eventType == DialogueEventType.Custom || 
        !string.IsNullOrEmpty(eventData.customEventName))
    {
        bool match = eventDialogue.customEventName == eventData.customEventName;
        if (!match)
        {
            Debug.Log($"Custom name mismatch: '{eventDialogue.customEventName}' != '{eventData.customEventName}'");
        }
        return match;
    }
    
    // 3. Default match
    return true;
}
```

##### Example Matching:

```
Event Data:
  eventType: Custom
  customEventName: "EntranceArea"

Config Entry:
  eventType: Custom
  customEventName: "EntranceArea"
  dialogue: EntranceAreaDialogue

Result: MATCH ✅
```

###### Data Structures at this Point:

```
characterConfigs = List<CharacterDialogueConfig> {
    PlayerClueDialogues {
        characterName: "Player",
        eventDialogues: List<EventDialogue> {
            EventDialogue {
                eventType: OnClueFound,
                customEventName: "Key",
                dialogue: KeyDialogue,
                triggerOnce: true,
                delay: 0.5f,
                priority: 0
            },
            EventDialogue {
                eventType: Custom,
                customEventName: "EntranceArea",
                dialogue: EntranceDialogue,
                triggerOnce: true,
                delay: 0.5f,
                priority: 0
            }
        }
    }
}

matches = List<EventDialogue> {
    EventDialogue { /* matching dialogue */ }
}

triggeredOnceEvents = HashSet<string> {
    "Player_Custom_EntranceArea"
}
```

### Phase 4: Dialogue Triggering

```
// DialogueEventListener.TriggerDialogue()
private void TriggerDialogue(Dialogue dialogue)
{
    // 1. Validation
    if (dialogueManager == null)
    {
        Debug.LogError("[DialogueEventListener] DialogueManager reference is missing!");
        return;
    }
    
    if (dialogue == null)
    {
        Debug.LogError("[DialogueEventListener] Dialogue is null!");
        return;
    }
    
    Debug.Log($"[DialogueEventListener] Triggering dialogue: {dialogue.name}");
    
    // 2. Check if dialogue is already active
    if (queueDialogues && isShowingDialogue && !allowInterruption)
    {
        // Queue for later
        Debug.Log("[DialogueEventListener] Dialogue already active - queueing");
        dialogueQueue.Enqueue(() => dialogueManager.StartDialogue(dialogue));
    }
    else
    {
        // 3. Show immediately
        if (allowInterruption)
        {
            StopAllCoroutines();
        }
        
        isShowingDialogue = true;
        dialogueManager.StartDialogue(dialogue); // → DialogueManager
        StartCoroutine(WaitForDialogueEnd());
    }
}
```

**Variables:**
•	dialogue: Dialogue asset reference
```
Dialogue {
      name: "Player",
      sentences: string[] {
          "Found the key.",
          "I wonder what this unlocks...",
          "Better keep this safe."
      }
  }

```
```
•	queueDialogues: bool (true = queue if busy)
•	isShowingDialogue: bool (tracks active state)
•	allowInterruption: bool (false = don't interrupt)
•	dialogueQueue: Queue<Action> (pending dialogues)
```

### Phase 5: Dialogue Display

```
// DialogueManager.StartDialogue()
public void StartDialogue(Dialogue dialogue)
{
    // 1. Show dialogue box
    animator.SetBool("IsOpen", true);
    
    // 2. Set speaker name
    nameText.text = dialogue.name; // "Player"
    
    // 3. Clear previous sentences
    sentences.Clear();
    
    // 4. Validation
    if (dialogue.sentences == null || dialogue.sentences.Length == 0)
    {
        Debug.LogError("No sentences found in dialogue!");
        return;
    }
    
    Debug.Log("Number of sentences: " + dialogue.sentences.Length);
    
    // 5. Enqueue all sentences
    foreach (string sentence in dialogue.sentences)
    {
        sentences.Enqueue(sentence);
    }
    // sentences queue now contains: ["Found the key.", "I wonder...", "Better keep..."]
    
    // 6. Activate dialogue
    dialogueActive = true;
    
    // 7. Display first sentence
    DisplayNextSentence();
}
```

UI Components:
•	animator: Animator (controls dialogue box animation)
	•	Parameter: IsOpen (bool)
	•	Animation: DialogueBoxOpen/Close
•	nameText: TextMeshProUGUI (displays speaker name)
	•	Text: "Player"
•	dialogueText: TextMeshProUGUI (displays sentence)
	•	Text: Initially empty, fills with typing effect


---
# Reference
