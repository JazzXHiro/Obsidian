2025-03-27 01:00

Status:

Tags:

# Drop

#### Render Method in LibGDX

The render() method in libGDX is the core of your game loop. It's called automatically every frame (typically 60 times per second) and is responsible for updating your game state and drawing everything on screen.

```
@Override
public void render() {
    input();   // Process player input
    logic();   // Update game state
    draw();    // Render graphics
}
```

#### Unproject Method in LibGDX

In libGDX, unproject is a method that converts screen coordinates (like from mouse or touch input) into game world coordinates.

When a player touches the screen, Gdx.input.getX() and Gdx.input.getY() give you the position in screen/window pixels. However, your game objects typically use a different coordinate system (your game world coordinates).

The unproject method:

- Takes screen coordinates (usually in pixels, with 0,0 at top-left)

- Converts them to your game world coordinates based on your viewport/camera setup

- Handles any scaling, rotation, or other transformations of your camera



# Reference
