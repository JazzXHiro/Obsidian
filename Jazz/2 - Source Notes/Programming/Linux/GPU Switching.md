	2025-11-07 10:26

Status: [[Jazz/3 - Tags/t-child]]

Tags: [[Jazz/3 - Tags/t-linux]] 

---
# GPU Switching

We use envycontrol to switch between gpus

To check mode:

```bash
envycontrol -q
```

or:

```bash
envycontrol --cache-query
```

You should get output similar to:

```
Current mode: integrated
```

or

```
Current mode: hybrid
```

or

```
Current mode: nvidia
```

---

## ✅ Switching Still Works the Same

| Mode      | Command                          | Meaning                                                   |
| --------- | -------------------------------- | --------------------------------------------------------- |
| iGPU only | `sudo envycontrol -s integrated` | Low power, NVIDIA fully off                               |
| Hybrid    | `sudo envycontrol -s hybrid`     | Desktop runs on AMD, apps can use NVIDIA with `prime-run` |
| dGPU only | `sudo envycontrol -s nvidia`     | Max performance, battery drain                            |

Reboot after switching:

```bash
reboot
```

---

## 🎮 Using NVIDIA in Hybrid Mode

Launch heavy apps with NVIDIA:

```bash
prime-run steam
prime-run blender
prime-run <game>
```

### **A Hyprland GPU Switch Menu**

Press one key → pick GPU mode → auto reboot.

Just tell me which launcher you use:

**wofi** / **rofi** / **fuzzel**

---

Both **wofi** and **rofi** are **application launchers** — basically little search/selection menus that pop up when you press a key.  
You type something → it filters → you choose → it runs.

They are often used in **tiling window managers** like **Hyprland, i3, Sway, bspwm**.

---

## **Rofi**

- Classic, very popular launcher
    
- Originally made for **X11**
    
- Can be themed heavily
    
- Often used in i3/bspwm setups
    
- There is a special Wayland version: `rofi-wayland`
    

**Example:**  
Press a key → a searchable menu appears to launch apps.

---

## **Wofi**

- A **Wayland-native** launcher
    
- Works best with **Hyprland** and **Sway**
    
- Simpler and smoother on Wayland
    
- Matches the look of Wayland-based environments more naturally
    

**So if you're on Hyprland → wofi is usually the best choice.**

---

## Quick Visual Difference:

|Feature|Wofi|Rofi|
|---|---|---|
|Designed for|**Wayland**|**X11 (with Wayland fork)**|
|Look|Clean & minimal|Highly customizable|
|Performance in Hyprland|**Excellent**|Good (if using rofi-wayland)|
|Setup|Simple|More config options|

---

## What You're Using Them For

Right now, you're using the launcher to display a **GPU mode selection menu**:

```
integrated
hybrid
nvidia
status
cancel
```

So instead of typing commands, you can just press **SUPER + G** → choose GPU mode → reboot → done.

---

## Why You Don’t Need All Three

You already have:

```
/usr/bin/wofi   ✅
/usr/bin/rofi   ✅
(no fuzzel)     ❌
```

### Best for Hyprland → **Wofi**

So our GPU menu script uses **wofi**.

---

If you ever want a **rofi** style with themes (Nord, Catppuccin, Gruvbox, etc.), I can make your menus look like this 👇

```text
╭───────────────╮
│ GPU: Select…   │
├───────────────┤
│ integrated     │
│ hybrid         │
│ nvidia         │
│ status         │
╰───────────────╯
```

Just tell me which vibes you like:

**1)** cyberpunk neon  
**2)** clean mac-style  
**3)** catppuccin latte/mocha  
**4)** gruvbox rust

Reply with a number → I’ll theme your menu 🔥

## To check current active GPU OpenGL Renderer

`glxinfo | grep "renderer" -i`  



---
# Reference
