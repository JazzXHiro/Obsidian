2025-01-30 15:52

Status: [[Jazz/3 - Tags/t-child]]

Tags: [[Jazz/3 - Tags/t-godot]] [[Jazz/3 - Tags/t-engine]] [[Jazz/3 - Tags/t-gamedev]] [[Jazz/3 - Tags/t-gojo]]

# godotengine


nodes 

scenes

![[Pasted image 20250124020430.png]]

world boundary - extends infinitely

#### Nodes

AnimationPlayer

Area2D -- for object detection without any actual collision

mask decides which layer it the sprite collides with

queue_free() -- removes an entire scene from the game

![[Pasted image 20250124235631.png]]![[Pasted image 20250124235648.png]]

Ctrl + D -- Duplicate

.is_colliding
.flip_h
![[Pasted image 20250125005141.png]]

Engine.time_scale --- to manipulate speed

![[Pasted image 20250125005410.png]]
to free the collisionnode so player falls down

![[Pasted image 20250125005507.png]]

physics process runs at a fixed rate - 60fps (needs it to work properly)

TO change keybinds
![[Pasted image 20250125005627.png]] 


# Reference
