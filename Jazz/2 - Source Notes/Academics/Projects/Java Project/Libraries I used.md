2025-04-24 16:36

Status:

Tags:

# Libraries


# LibGDX Libraries in the Drop Game

## Core Framework
- **`com.badlogic.gdx.ApplicationListener`**: Main interface implemented by the game. Defines the lifecycle methods (create, render, dispose, etc.).
- **`com.badlogic.gdx.Gdx`**: Central access point for device-specific features like input, files, and audio.

## Input Handling
- **`com.badlogic.gdx.Input.Keys`**: Constants for keyboard input, used for player movement and menu navigation.

## Audio System
- **`com.badlogic.gdx.audio.Music`**: For long-playing background audio tracks with streaming capability.
- **`com.badlogic.gdx.audio.Sound`**: For short sound effects (like droplet collection sounds) loaded entirely in memory.

## Graphics
- **`com.badlogic.gdx.graphics.Color`**: Color utilities for rendering text and tinting sprites.
- **`com.badlogic.gdx.graphics.Texture`**: Raw image data loaded from files (bucket, droplet, background).
- **`com.badlogic.gdx.graphics.g2d.BitmapFont`**: Text rendering for scores, menus, and UI elements.
- **`com.badlogic.gdx.graphics.g2d.Sprite`**: Enhanced texture objects with position, rotation, and scale properties.
- **`com.badlogic.gdx.graphics.g2d.SpriteBatch`**: Efficient renderer for drawing multiple 2D images in batches.

## Math & Collision
- **`com.badlogic.gdx.math.MathUtils`**: Math utilities including random number generation for droplet positioning.
- **`com.badlogic.gdx.math.Rectangle`**: Rectangle class for collision detection between bucket and droplets.
- **`com.badlogic.gdx.math.Vector2`**: 2D vector class for position and touch input handling.

## Data Structures
- **`com.badlogic.gdx.utils.Array`**: LibGDX's optimized array implementation for managing collections of droplets.
- **`com.badlogic.gdx.utils.ObjectMap`**: Key-value mapping for high score data storage.

## Screen Management
- **`com.badlogic.gdx.utils.ScreenUtils`**: Utilities for screen clearing and management.
- **`com.badlogic.gdx.utils.viewport.FitViewport`**: Viewport implementation that scales the game while maintaining aspect ratio, ensuring consistent appearance across different screen sizes.



# Reference
