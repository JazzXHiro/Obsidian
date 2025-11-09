# Death Valley
Team Members:
1. Keerti
2. Ayushmaan 
3. Aarav

# Game Overview

An Ambient mystery Exploration first person game set in Norway's Isladen Valley about uncovering who was the unfortunate victim of a horrific death and what caused that!

Genre: Exploration, Survival, Puzzle, Mystery
Perspective: First Person 3D
Target Playtime: 10ish minutes
Platform: Windows
Engine: Unity
Project duration: 1 month

# Core Concept

Explore -> Complete Puzzles -> Complete Objective 

Main Objective:- Identify the victim 

1. Prologue: Player finds itself at Point A 
2. Objective 1: locate destination
3. Objective 2: Look for Clues
4. Objective 3: Note down in journal
5. Explore and Find more clues at different places
	1. Direct Clues
	2. Scattered Clues
6. Then markdown, first one to get 3 clues is the real victim
7. Finale

Permanent Mechanic:-
1. Flashlight life = 0% -> Sanity meters starts to drop
2. Sanity meter = 0% -> Faint and restart from checkpoint
3. If player goes too far, They enter The FOG and faint

# Story and setting

premise: A different take on the incident of Isladen valley incident

Backstory: 
	On the morning of 29 November 1970, a man and his two young daughters see a body in Isdalen Valley.
	The corpse is sprawled across some rocks - with its arms extended in a "boxer" position, typical of bodies that have been burnt.

Isdalen is known to some locals as "Death Valley" -It is a beautiful but dangerous trek in Norway, in the 1960s, some hikers had fallen to their deaths while trekking in the fog.

Player role:
	A journalist came to document the case but it turns out to be something else...
	
Characters: 
1. Main character - A journalist 
2. Victims -
	1. A rich Lady in her mid early 30s
	2. An not so rich Old man
		`A young maid in her 20s.`
	3. And an enthusiastic local boy
		`An enthusiastic college girl on vacation in her hometown`
	`Reason for Change suggestion
	`A basic examination of the skeleton structure can reveal the gender of the corpse. Just to make the plot seem more solid.`
3. Young Maid's desperate younger brother who came to find his sister and left an entry in the trail log and a letter inside the cabin.

Narrative flow:
1. Act 1 :- Introduction
	1. starts with text on black screen giving the context and backstory.
	2. Arrival of player at the foothills bus stop
	3. Starts trekking towards the safe house, when reaches, gets a call from friend who then introduces the main character to player, He then mentions that mentions that the key was lost somewhere around the investigation scene and that he has go and find it.
	4. Finds two clues
		1. Boy clue #1 (near foothills)
		2. Old man clue #1 (near safe house cabin)

2. Act 2 :- Finding more clues
	1. Goes to the scene of investigation to look for keys
	2. Reaches the site, find keys after looking
	3. Goes back to Safe house -> Unlocks the Journal
	4. Fills gathered clues
	5. Reads a letter, goes in other direction, towards the peak
	6. Returns from peak to safe house
	7. Finds three clues
		1. boy clue #2 (near the site)
		2. lady clue #1 (Inside the cabin)
		3. Old man clue #2 (At the peak)

3. Act 3 :- Piecing everything together and Finale
	1. Goes towards a cave
	2. Finds more clue
	3. puts everything together
	4. Victim's Identity is discovered
	5. Finds tow clues
		1. Lady clue #2 (on the way to the cave)
		2. Lady clue #3 (In the cave, Not that deep tho)

4. Epilogue :- It is revealed that the old man and boy were found a day later by the rescue team and our deduction was correct. 

## Details on Clues

1. Direct Clues (For the real victim)

	1. Clue #1 - Suitcase (lady)
		1. States: Locked/Unlocked
		2. Type: Inspectable Object -> Puzzle? (3-digit lock)
		3. location: Inside Cabin
		4. Flavour: Clothes, A train ticket (boarding date gone) and a hotel key
			1. Train ticket: Hints that the lady never left the town 
				1. Flavour text: "Single ticket: Oslo to Bergen. Dated 27/11/1970"
				2. Deduction: She never left
			2. Hotel key: Hints the lady is well-off
				1. Flavour text: "Grand Hotel, the kind of place only the well-to-do could afford"
				2. Deduction: She is rich

	2. Clue #2 - Group of two Bottles (lady)
		1. Type: World Item
		2. Location: On the way to cave
		3. Flavour text: "The bottles smell faintly of benzine, someone bought fuel up here"
		4. Deduction: These maybe the same bottles used for the deed
		5. Visual layer: black marks along the path from bottles to cave

	3. Clue #3 - Broken wrist watch (Lady)
		1. Type: Multi part World Item (4 scattered pieces)
		2. Location: last one is inside cave with some more fuel bottles
		3. Flavour text (final assemble): "The Watch is a really expensive one, The watch is stopped at 2:13 — the moment everything stopped"
		4. Deduction: The lady is the victim

2. Ambiguous Clues (TO throw off players)

	1. Clue #1 - Letter in safe house (Old man)
		1. Type: Inspectable Object 
		2. location: near safe house
		3. Flavour text: "Dad left home before dawn. He said he’d fix it all himself this time. I think he owed money to someone dangerous"
		4. Deduction: He might be the victim

	2. Clue #2 - Threat note (Boy)
		1. Type: Inspectable Item
		2. location: near foothills
		3. Flavour text: "How dare you say those things! You think you’re untouchable? I’ll make you pay for it, bastard!"
		4. Deduction: He might be the victim

	3. Clue #3 - A climbing stick (Old man)
		1. Type: World Item
		2. location: at the peak
		3. Flavour text: "A splintered wooden stick. One end is cleanly cut, the other chipped from a fall. Someone struggled to stay upright here"
		4. Deduction: He lost his stick which suggests he might be in trouble

	4. Clue #4 - Half burnt pocket knife (Boy)
		1. Type: World Item
		2. location: around the site but not exactly near
		3. flavour text: "A small pocket knife, handle charred. The blade’s edge is darkened, was it burned?"
		4. deduction: He was involved with fire somehow
## Not So true story for false victims - 

1. A letter in house written by old man's son which mention the old man being in debt and trying to hide.

2. Some sort of note from some teenager who seems to threaten the local boy

## True cause for lady's death 

1. "killed by bunch of local thugs to rob money", this is the real case in our game and is revealed at the end after confusing the players


## Game-play mechanics

| mechanic          | Desc               | Action |
| ----------------- | ------------------ | ------ |
| walk              | movement           | WASD   |
| look              | camera             | mouse  |
| Interact          | raycast            | E      |
| Rotate item       | 3D object rotation | WASD   |
| Open Journal      |                    | tab    |
| Toggle flashlight |                    | F      |
|                   |                    |        |

## puzzles

1. brief case code -

## level and environment design

- Continuous Map 
- Trail head -> Cabin -> Scene -> Cabin -> Peak -> Cave

Props and assets:
1. Terrain - Rock, Trees, Small plants, Fencing
2. Cabin Exterior and Interior
3. Evidence props - briefcase, ticket, key, Clothes, bottles, watch, cane, letter, knife, note, journal.

## Visuals and Audio design

1. Low poly retro PS1 era graphics
2. Color Palette: 
3. Lighting: Low, moody, moon light
4. Sound design:
	1. Ambient noises, foot steps, Dynamic Ambient wind, forest sounds
	2. Eerie background score
	3. Creepy hisses and rumbles
5. UI/UX: minimal

## References

1. Firewatch
2. Fears to fathom: Ironbark lookout
3. The vanishing of Ethan carter
4. What remains of Edith finch

# All mechanics, systems and Artefacts

## Core player and input (high - programmer)

1. Player controller 
	- Input system
	- Camera smoothing
2. Input system
	1. Toggle flashlight
	2. Open journal
	3. Rotate Item while Inspection

## Interaction and Item system (high - programmer + designer)

1. Ray cast based Interact system: Single ray cast from camera; use of layer mask for intractable items
2. Inspectable view: separate camera view to inspect item
3. Pickup logic: Collect items and add them to journal; Use simple pickup that disables world model and registers item ID in inventory
4. Multi part Item Assembly: Store part IDs and when all collected replace them with the full model ID
5. Intractable prefabs: Create base intractable script with states: IDLE, Locked, Inspectable and collected
## UI/UX (high - programmer + designer)

1. Journal / Evidence board UI: shows suspects, allows marking (first to three mechanic); Implement as Canvas UI with thumbnails
2. Inventory: shows collected items; item link to journal entries; A list with icons and Inspect button
3. Interaction prompts and cross-hair
4. Pause menu (?)
5. Subtitles

## World and level triggers (high - programmer + designer)

1. Trigger volumes (on enter/exits ): Trigger audio, particles, events and player passes a certain point; Use empty game objects with trigger collider and an area trigger script configurable in inspector
2. Map Border/ Fog boundary
3. checkpoint/re-spawn system: single safe-house check point to keep it simple. save minimal state (collected items persists)
4. Event sequencer (?)

## sanity and flashlight (high - programmer + audio/art)

1. Flashlight system (battery): toggles light, battery drain =  affect sanity; Time intervals for battery drains;  UI battery indicator; charge under street lights
2. Sanity meter: Visual/audio distortion as tension mechanic; Vignette, chromatic aberration, slight camera shake, whisper SFX
3. Sanity recovery mechanic: Restores sanity at safe-house

## puzzles (high - programmer + designer)

1. Code Lock UI (suitcase): simple numeric lock puzzle; correct code triggers unlock state, inside it is two intractable.  
2. ?
3. ?

## World construction and assets (high - artist + designer)

1. Terrain: Using Unity Terrain or custom mesh
2. Navmesh for anything that needs to follow the player (particles, sfx, etc.)
3. Prefab library: Reusable models - rock, trees, cabin, lights, fences, intractable, etc.  
4. Lighting and post processing: Mood (fog, volumetric light, bloom, colour grading); Using URP + post processing stack; keeping settings cheap for performance
5. Particle Effects: smoke at site, fog; using simple particle system or prefabs from store
6. VFX for Sanity: hallucination overlay; screen space shader or UI overlays toggles by sanity value. 

## Audio (high - audio + programmer)

1. Ambient layers: winds, forest loop
2. SFX for interactions
3. footstep variation on different surfaces
4. One off event sounds: rustle noises, faint voice in distances

## UI/UX polish ( medium - designer + programmer)

1. HUD elements: Flashlight battery, sanity bar, simple cross-hair
2. Journal pop ups (?)
3. On screen hints and tutorials
4. Final END reveal + epilogue text

## Systems and architecture (high - programmer)

1. Scriptableobject data for clues: stores clue names, description, suspect tag
2. GameManager/ stateManager: track collected clues, current suspect counts, game state; Using a singleton with a save/load line functionality
3. EventBus/Unity Events: decouple systems (pickup triggers journal updates)
4. savesystem: persist progress across sessions: store collected IDs and states

## Build / Optimisation / QA (Medium — All)

1. Performance Checks: Frame timing, draw calls, occlusion.
2. Light-map baking & LOD: Good performance & visuals.
3. Test Cases / Play-test Plan: Check puzzle flow, impossible states, missing clues, sanity edge cases.
4. Profiler & Debug Tools: Rapidly find bottlenecks.
5. Final build & packaging: Player build settings, icon, README.

## Editor & Workflow (Medium — All)

1. Folder & Naming Conventions: `Assets/Art`, `Assets/Scripts`, `Assets/Prefabs`, `Assets/Audio`, `Assets/Scenes`, `Assets/UI`
2. Scene Setup: Main scene + a separate test scene for interactions/puzzle testing.
3. Version Control (Git) (?)

## Optional / Nice-to-have (Low)

1. Simple AI (non-hostile NPC) — e.g., rescue team seen from distance
2. 
-------------------"CAN ADD MORE HERE"----------------------


# High priority minimal list

- Player controller & input.
    
- Ray-cast interact & inspect view.
    
- Journal/inventory & first-to-three marking UI.
    
- Intractable prefabs for 7–9 clues (suitcase, bottles, watch pieces, letter, knife, stick).
    
- Suitcase lock puzzle.
    
- Trigger volumes to sequence act progression (cabin → site → peak → cave).
    
- Flashlight + battery + battery UI.
    
- Sanity effects basic (vignette + whisper SFX).
    
- Checkpoint at safe-house and map boundary.
    
- Audio logs + subtitles.
    
- Level blockout (terrain + cabin + cave) and basic lighting.

# Who should own what (3-person split)

- **Programmer (1):** Player controller, interact system, puzzles, inventory, GameManager, journal UI hooks.
    
- **Designer / Scripter (1):** Place clues, design trigger events, write flavour text, wire puzzles in-scene, QA.
    
- **Artist / Audio (1):** Terrain, props, lighting, particle effects, SFX, voice/tape editing, UI icons.

# Quick implementation tips & patterns (practical)

- **Use ScriptableObjects** for clue data (title, description, suspect tag, weight, audio clip). Easy to tweak without code changes.
    
- **Single Intractable base class** with overridable `OnInteract()` and states (Locked, Inspectable, Collected).
    
- **Event-driven design:** when a clue is collected fire `OnClueCollected(clueID)` event to update journal and check “first-to-three” logic in GameManager.
    
- **Inspect view**: instantiate object in front of a dedicated `InspectCamera`, freeze player movement, show rotate/close controls.
    
- **Sanity VFX**: use Post-processing stack properties (chromatic aberration, grain) driven by sanity value.
    
- **Boundary**: soft warn HUD + audio then teleport to safe-house after 5s in fog. This is better UX than instant death.

# # Testing checklist (use every build)

- Can player collect clues in any order and still finish?
    
- Does first-to-three mechanic correctly identify victim every run?
    
- Are puzzles solvable (and not ambiguous)?
    
- Are any clues unobtainable due to collision/physics?
    
- Are checkpoint/respawn states correct?
    
- Sanity/flashlight interaction tested at edge cases (battery drain while in puzzles)?
    
- All audio logs have subtitles and can be replayed once collected.

