	2025-11-20 13:39

Status:

Tags:

---
# Game Mechanics

# Needed
## 1. Movement Mechanics
	1. Basic WASD movement along with mouse camera movement.
	2. Jump using SPACEBAR
	3. Sprint using Shift
	4. Interaction - E/Mouse LClick

## 2. Dialogue Mechanics
	1. Where and when to trigger certain dialogues.

## 3. Survival Mechanics
  
  ### i) Sanity Meter
	  1. Sanity Meter Depletion & Replenishment mechanics
		  1. Sanity Meter keeps deplenishing (if player flashlight isn't active and player isn't under any lampost)
		  2. Sanity meter only replenishes
			  1. When under a lampost(Gradually)
			  2. Sanity meter resets to full when a new checkpoint is unlocked.
	  2. Once Sanity Meter depletes to zero - Player dies and respawn at the last checkpoint
	  3. Lamposts
		  1. Scattered throughout the game world.
		  2. If player is under the lampost, their sanity replenishes.
		  3. Soon as the player enters the lampost, the torch is turned OFF if ON.
		  4. While the player is in the lampost radius, the player can't activate the torch until he leaves the radius.
	  Additional
		  Bleed effect/warning visuals on the screen when sanity is low.

## 4. Journaling Mechanics
### Clue Management
	1. The Player brings up the Journal -- On pressing "J"
	2. On every clue encounter in dialogues/in game objects player notes them down in the Journal
	3. Note down clues pertaining to all three victims in their own categories.
		1. Player theorizes the scenarios based on these gathered clues.
	4. Once the three clues of the real victim has been journalized.
		1. The real scenario is uncovered, and the real identity of the body is declared.

### Player Navigation
	1. The journal reminds the player of the next objective.

## 5. Respawn Mechanics
	Automated respawn to last checkpoint after player dies.

## 6. Door lock mechanism
	Cabin door only unlocks when the key is inserted.

## 7. Scene Transition
	Loading Screen Mechanics.

## 8. Flashlight Mechanics
	1. Press "F" to activate/deactivate flash light
	2. When Flashlight is active Sanity meter doesn't drop
	3. Has a overheat mechanics
		1. if the overheat meter fills up - torch deactivates
			1. Gets a cooldown timer - user can't use the torch until timer hits zero
		2. when overheat meter goes down to zero - torch can be turned back on by pressing "F" again

# Additional

  ### ii) Fog Mechanics 
	  3. Acts as a world boundary
	  4. Player Walks into the fog -
		  1. After 2-4 seconds player is respawned at the last checkpoint

---
# Reference

[^1]: 
