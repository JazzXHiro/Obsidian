	2025-11-10 03:36

Status:

Tags:

---
# Navmesh + raycast

1. Set Plane to Navmesh Static with Default area being walkable and then bake
2. set the police car to Navmesh Agent
3. Create  a new ground layer and assign it to plane.
	   This is done for optimization. So that Unity doesn't detect needless ray cast collisions below the plane.
	   
	   unity layers are defined using bitmasks.
1. 

---
# Reference
