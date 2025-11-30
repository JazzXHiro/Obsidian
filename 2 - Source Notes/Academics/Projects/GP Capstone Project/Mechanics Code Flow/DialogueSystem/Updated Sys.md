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

---
# Reference
