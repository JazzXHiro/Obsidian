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



---
# Reference
