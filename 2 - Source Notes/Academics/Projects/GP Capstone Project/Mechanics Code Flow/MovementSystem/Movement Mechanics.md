	2025-11-29 21:47

Status:

Tags:

---
# Movement Mechanics 

## Movement Mechanics Flow Diagram

```mermaid
sequenceDiagram
    participant Input as Unity Input System
    participant PIH as PlayerInputHandler
    participant FPC as FirstPersonController
    participant CC as CharacterController
    participant Camera as Main Camera

    Note over Input,Camera: Input Phase
    Input->>PIH: Input detected (WASD, Mouse, Space, Shift)
    PIH->>PIH: SubscribeActionValueToInputEvents()
    
    alt Movement Input (WASD)
        PIH->>PIH: movementAction.performed
        PIH->>PIH: MovementInput = Vector2(x, y)
    end
    
    alt Sprint Input (Shift)
        PIH->>PIH: sprintAction.performed
        PIH->>PIH: SprintTriggered = true
    end
    
    alt Jump Input (Space)
        PIH->>PIH: jumpAction.performed
        PIH->>PIH: JumpTriggered = true
    end
    
    alt Rotation Input (Mouse)
        PIH->>PIH: rotationAction.performed
        PIH->>PIH: RotationInput = Vector2(x, y)
    end

    Note over FPC: Update Loop - Every Frame
    FPC->>FPC: Update()
    FPC->>FPC: HandleMovement()
    FPC->>FPC: HandleRotation()

    Note over FPC,CC: Movement Calculation
    FPC->>FPC: CalculateWorldDirection()
    FPC->>PIH: Get MovementInput (Vector2)
    PIH-->>FPC: Return Vector2(x: horizontal, y: forward)
    FPC->>FPC: Create inputDirection Vector3(x, 0, y)
    FPC->>FPC: transform.TransformDirection(inputDirection)
    FPC->>FPC: Return normalized worldDirection

    FPC->>FPC: Calculate CurrentSpeed
    FPC->>PIH: Get SprintTriggered (bool)
    PIH-->>FPC: Return true/false
    Note over FPC: speed = walkSpeed * (sprint ? 2.0 : 1.0)
    
    FPC->>FPC: currentMovement.x = worldDirection.x * CurrentSpeed
    FPC->>FPC: currentMovement.z = worldDirection.z * CurrentSpeed

    Note over FPC,CC: Jumping & Gravity
    FPC->>FPC: HandleJumping()
    FPC->>CC: Check isGrounded
    CC-->>FPC: Return bool
    
    alt If Grounded
        FPC->>FPC: currentMovement.y = -0.5f
        FPC->>PIH: Get JumpTriggered
        PIH-->>FPC: Return bool
        alt If Jump Pressed
            FPC->>FPC: currentMovement.y = jumpForce (5.0)
        end
    else If Airborne
        FPC->>FPC: currentMovement.y += gravity * multiplier * deltaTime
    end

    FPC->>CC: Move(currentMovement * Time.deltaTime)
    CC->>CC: Apply movement to character position

    Note over FPC,Camera: Rotation Handling
    FPC->>FPC: HandleRotation()
    FPC->>PIH: Get RotationInput (Vector2)
    PIH-->>FPC: Return Vector2(mouseX, mouseY)
    
    FPC->>FPC: mouseXRotation = x * mouseSensitivity (0.1)
    FPC->>FPC: mouseYRotation = y * mouseSensitivity (0.1)
    
    FPC->>FPC: ApplyHorizontalRotation(mouseXRotation)
    FPC->>FPC: transform.Rotate(0, rotationAmount, 0)
    Note over FPC: Player body rotates left/right
    
    FPC->>FPC: ApplyVerticalRotation(mouseYRotation)
    FPC->>FPC: verticalRotation = Clamp(vertical - amount, -80, 80)
    FPC->>Camera: Set localRotation = Quaternion.Euler(vertical, 0, 0)
    Note over Camera: Camera tilts up/down
    FPC->>FPC: hand.localRotation = same as camera
    Note over FPC: Flashlight syncs with camera

```

## Key Variables and Their Flow

### Input Variables (PlayerInputHandler → FirstPersonController)

| Variable        | Type    | Source      | Purpose                                  |
| --------------- | ------- | ----------- | ---------------------------------------- |
| MovementInput   | Vector2 | WASD keys   | x = strafe (A/D), y = forward/back (W/S) |
| RotationInput   | Vector2 | Mouse delta | x = horizontal look, y = vertical look   |
| JumpTriggered   | bool    | Spacebar    | Triggers jump when grounded              |
| SprintTriggered | bool    | Shift key   | Multiplies movement speed by 2.0         |

### Movement Calculation Variables
```
// Step 1: Get input direction in local space
Vector3 inputDirection = new Vector3(
    playerInputHandler.MovementInput.x,  // Left/Right (-1 to 1)
    0f,                                   // No vertical component
    playerInputHandler.MovementInput.y    // Forward/Back (-1 to 1)
);

// Step 2: Convert to world space relative to player rotation
Vector3 worldDirection = transform.TransformDirection(inputDirection).normalized;

// Step 3: Calculate speed with sprint multiplier
float CurrentSpeed = walkSpeed * (SprintTriggered ? sprintMultiplier : 1);
// Result: 3.0f (walk) or 6.0f (sprint)

// Step 4: Apply to movement vector
currentMovement.x = worldDirection.x * CurrentSpeed;
currentMovement.z = worldDirection.z * CurrentSpeed;
```

### Jumping & Gravity Variables
```
if (characterController.isGrounded)
{
    currentMovement.y = -0.5f;  // Small downward force to maintain ground contact
    
    if (JumpTriggered)
    {
        currentMovement.y = jumpForce;  // 5.0f upward velocity
    }
}
else
{
    // Gravity accumulation: -9.81 * 1.0 * Time.deltaTime
    currentMovement.y += Physics.gravity.y * gravityMultiplier * Time.deltaTime;
}
```

### Rotation Variables
```
// Horizontal (Y-axis) rotation - rotates entire player body
float mouseXRotation = RotationInput.x * mouseSensitivity;  // e.g., 10 * 0.1 = 1.0°
transform.Rotate(0, mouseXRotation, 0);

// Vertical (X-axis) rotation - only camera/hand
float mouseYRotation = RotationInput.y * mouseSensitivity;
verticalRotation = Mathf.Clamp(
    verticalRotation - mouseYRotation,  // Accumulated pitch
    -upDownLookRange,                    // -80°
    upDownLookRange                      // +80°
);
mainCamera.transform.localRotation = Quaternion.Euler(verticalRotation, 0, 0);
hand.localRotation = Quaternion.Euler(verticalRotation, 0, 0);
```

### Execution Order Summary
	1.	Input System → Captures raw input (WASD, Mouse, Space, Shift)
	2.	PlayerInputHandler → Converts to properties (MovementInput, RotationInput, etc.)
	3.	FirstPersonController.Update() → Called every frame
	4.	HandleMovement() → Calculates and applies character movement
	•	CalculateWorldDirection() → Converts input to world space
	•	HandleJumping() → Manages vertical movement and gravity
	•	characterController.Move() → Applies final movement
	5.	HandleRotation() → Rotates player body and camera
	•	ApplyHorizontalRotation() → Player body Y-axis rotation
	•	ApplyVerticalRotation() → Camera/hand X-axis rotation (clamped)

The system uses Unity's CharacterController component for collision detection and movement, ensuring the player can't walk through walls and properly handles ground detection for jumping.

---
# Reference
