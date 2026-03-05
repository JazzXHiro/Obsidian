	2025-11-29 21:18

Status:

Tags:

---
# Flashlight Mechanics Flow

## 1. Input Detection Flow

```mermaid
sequenceDiagram
    participant Input as PlayerInputHandler
    participant FC as FlashlightController
    participant Light as flashlightLight (Unity Light)
    participant SM as SanityManager
    participant UI as overheatSlider (UI)

    Input->>Input: Player presses F key
    Input->>Input: Set FlashlightTriggered = true
    FC->>Input: Read FlashlightTriggered in Update()
    FC->>FC: Check: current && !lastInputState<br/>(edge detection)
    FC->>FC: ToggleFlashlight()
    FC->>FC: Check if isOverheated
    alt Not Overheated
        FC->>FC: SetState(!isOn)
        FC->>SM: Check SanityManager.Instance.isUnderLamp
        alt Under Lamppost
            FC->>FC: Block turn ON, return early
        else Not Under Lamppost
            FC->>FC: isOn = on
            FC->>FC: ApplyState()
            FC->>Light: flashlightLight.enabled = isOn
        end
    else Overheated
        FC->>FC: Log warning, return early
    end
    FC->>FC: lastInputState = current
```

## 2. Overheat System Flow

```mermaid
graph TD
    A["Update() called"] --> B["UpdateHeat()"]
    B --> C{isOverheated?}
    C -->|Yes| D["Skip heat update<br/>(forced cooldown)"]
    C -->|No| E{isOn?}
    E -->|Yes| F["currentHeat += Time.deltaTime"]
    F --> G{currentHeat >= overheatThreshold?}
    G -->|Yes| H["currentHeat = overheatThreshold"]
    H --> I["OverheatFlashlight()"]
    G -->|No| J["UpdateSlider()"]
    E -->|No| K["currentHeat -= cooldownRate * Time.deltaTime"]
    K --> L["currentHeat = Max(0, currentHeat)"]
    L --> J
    I --> M["Set isOverheated = true"]
    M --> N["TurnOff()"]
    N --> O["StartCoroutine(GradualCooldownCoroutine())"]
    J --> P["Update UI slider value"]
    P --> Q{currentHeat <= 0.001f?}
    Q -->|Yes| R["Hide fill image"]
    Q -->|No| S["Show fill image"]
```

## Key Variables in Heat System:
| Variable | Type | Purpose | Default | 
|----------|------|---------|---------| 
| currentHeat | float | Current heat accumulation | 0f | 
| overheatThreshold | float | Max heat before overheat | 10f | 
| cooldownRate | float | Heat decrease per second (when OFF) | 2f | 
| overheatCooldownDuration | float | Forced cooldown duration | 5f | 
| isOverheated | bool | Blocks flashlight usage | false |

## 3. Overheat Coroutine Flow
```
GradualCooldownCoroutine() Flow:
├─ Calculate cooldownSpeed = overheatThreshold / overheatCooldownDuration
│  └─ Example: 10f / 5f = 2f per second
├─ While (currentHeat > 0f):
│  ├─ currentHeat -= cooldownSpeed * Time.deltaTime
│  ├─ currentHeat = Max(0f, currentHeat)
│  └─ yield return null (wait 1 frame)
├─ Ensure currentHeat = 0f
└─ Set isOverheated = false
```
**Variables Passed:**
•	Uses class fields: currentHeat, overheatThreshold, overheatCooldownDuration
•	Updates UI through UpdateSlider() in Update() loop

## 4. Lamppost Interaction Flow
```mermaid
sequenceDiagram
    participant Player
    participant LT as LamppostTrigger
    participant FC as FlashlightController
    participant SM as SanityManager

    Player->>LT: OnTriggerEnter(Collider other)
    LT->>LT: Check other.CompareTag("Player")
    LT->>SM: SetUnderLamp(true)
    LT->>FC: Check flashlight.IsOn
    LT->>LT: wasFlashlightOnBeforeEntering = IsOn
    LT->>FC: TurnOff()
    Note over FC: Flashlight forced OFF

    Player->>LT: OnTriggerExit(Collider other)
    LT->>SM: SetUnderLamp(false)
    LT->>LT: Check wasFlashlightOnBeforeEntering
    alt Was ON before
        LT->>FC: TurnOn()
        FC->>FC: SetState(true)
        FC->>SM: Check isUnderLamp (now false)
        FC->>FC: isOn = true
        FC->>FC: ApplyState()
    end
```

**Key Variables:**
•	wasFlashlightOnBeforeEntering (bool): Stores flashlight state before entering lamppost area
•	playerTag (string): Tag to identify player ("Player")

## 5. Sanity System Integration
```
// In SanityManager.UpdateSanityCoroutine()

bool flashlightOn = flashlightController.IsOn;  // ← Read from FlashlightController
bool underLamp = isUnderLamp;

float change = 0f;
if (flashlightOn)
{
    change = 0f;  // Sanity PAUSED (no drain/gain)
}
else if (underLamp)
{
    change = replenishRatePerSecond * delta;  // Sanity GAINS
}
else
{
    change = -drainRatePerSecond * difficulty * delta;  // Sanity DRAINS
}

sanitySlider.value += change;
```

## 6. Complete Function Call Chain

### Turning Flashlight ON:
```
User Input → PlayerInputHandler.FlashlightTriggered = true
          ↓
FlashlightController.Update()
          ↓
Check: current && !lastInputState (edge detection)
          ↓
ToggleFlashlight()
          ↓
Check: !isOverheated
          ↓
SetState(true)
          ↓
Check: !SanityManager.Instance.isUnderLamp
          ↓
isOn = true
          ↓
ApplyState()
          ↓
flashlightLight.enabled = true
```

### Overheat Trigger:
```
Update() → UpdateHeat()
       ↓
currentHeat += Time.deltaTime (while isOn)
       ↓
currentHeat >= overheatThreshold
       ↓
OverheatFlashlight()
       ↓
isOverheated = true
       ↓
TurnOff() → SetState(false)
       ↓
StartCoroutine(GradualCooldownCoroutine())
       ↓
Gradual cooldown over overheatCooldownDuration seconds
       ↓
isOverheated = false
```

## 7. Public API Methods
| Method            | Parameters        | Returns | Checks Performed                                        |
| ----------------- | ----------------- | ------- | ------------------------------------------------------- |
| SetState(bool on) | on: desired state | void    | 1. Overheat check<br/>2. Lamppost check (if turning ON) |
| TurnOn()          | None              | void    | Calls SetState(true)                                    |
| TurnOff()         | None              | void    | Calls SetState(false)                                   |
| IsOn              | N/A               | bool    | Getter for isOn                                         |
| IsOverheated      | N/A               | bool    | Getter for isOverheated                                 |
| HeatPercentage    | N/A               | float   | Returns currentHeat / overheatThreshold (clamped 0-1)   |

## 8. State Diagram
```mermaid
stateDiagram-v2
    [*] --> OFF
    OFF --> ON: User presses F<br/>(not overheated, not under lamp)
    ON --> OFF: User presses F
    ON --> OVERHEATED: currentHeat >= threshold
    OVERHEATED --> OFF: Forced OFF
    OFF --> COOLDOWN: Gradual heat decrease
    COOLDOWN --> OFF: currentHeat reaches 0<br/>isOverheated = false
    OFF --> [*]
    
    note right of ON
        currentHeat increases
        by Time.deltaTime
    end note
    
    note right of OFF
        currentHeat decreases
        by cooldownRate * Time.deltaTime
    end note
    
    note right of OVERHEATED
        5 second forced cooldown
        Cannot toggle flashlight
    end note
```

This system creates a balanced mechanic where:
•	Flashlight ON = Sanity paused, heat builds up
•	Flashlight OFF = Sanity drains (unless under lamppost), heat cools down
•	Overheated = Forced cooldown, sanity drains
•	Under Lamppost = Flashlight forced OFF, sanity replenishes

## 9. Integration with Flashlight Overheat

```mermaid
graph LR
    A["Player turns ON flashlight"] --> B["Sanity stops draining"]
    B --> C["Flashlight heats up<br/>(10 seconds)"]
    C --> D["Flashlight OVERHEATS"]
    D --> E["Flashlight forced OFF"]
    E --> F["Sanity starts draining again!"]
    F --> G["Flashlight cools down<br/>(5 seconds)"]
    G --> H["Player can use flashlight again"]
    
    style D fill:#f66
    style F fill:#f66
```

**The Trade-off:**
•	Use flashlight = Sanity safe BUT overheat risk
•	Overheat happens = Forced sanity drain for 5 seconds
•	Must balance flashlight usage vs. finding lampposts
This creates a survival resource management system where players must strategically:
1.	Use flashlight to pause sanity drain
2.	Find lampposts to restore sanity
3.	Manage overheat to avoid forced drain periods

---
# Reference
