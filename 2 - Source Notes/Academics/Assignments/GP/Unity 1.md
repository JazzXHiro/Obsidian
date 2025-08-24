	2025-08-25 02:54

Status:

Tags:

---
# Unity 1

- You can achieve this with the Is Trigger property of the Collider component. When you tell a collider component to act as a trigger instead of a physical collider, it will no longer have a solid barrier, but it can still detect entry by the player or other GameObjects. A trigger collider makes an object act more like a cloud. Even though it looks solid, an airplane can still pass right through it, and the pilot knows when they’ve gone through it.

- It's important to note that OnTriggerEnter is only called if at least one of the objects involved has a Rigidbody component attached to it. The player object already has a Rigidbody component, so you’re all set!

---
# Reference
