2025-03-31 02:43

Status:

Tags:

# High Score


I'll add a high score counter to your game that works with libGDX HTML. We'll use browser localStorage for persistence:

I've added a high score system to your game that will work with libGDX HTML:

1. Added variables:

- currentScore - Tracks the player's current score

- highScore - Tracks the highest score achieved

- font - For displaying the scores on screen

- prefs - Uses libGDX's Preferences system (works with HTML5's localStorage)

1. Score tracking:

- Score increases each time a drop is caught

- High score is updated when the current score exceeds it

- High score is saved using Preferences

1. Visual display:

- Current score and high score are displayed in the top-left corner

- Using BitmapFont for rendering text

1. Persistence:

- The Preferences system automatically uses the appropriate storage mechanism for each platform

- For HTML5, it uses localStorage

- Data is saved whenever a high score is achieved

- High score is loaded when the game starts and when resuming

This implementation ensures the high score will persist across game sessions even in the browser environment.


I made the following changes to implement the high score feature:

1. **Added new imports**:
   - `import com.badlogic.gdx.Preferences` - For storing high scores
   - `import com.badlogic.gdx.graphics.g2d.BitmapFont` - For displaying text

2. **Added new class variables**:
   ```java
   // Score variables
   private int currentScore = 0;
   private int highScore = 0;
   private BitmapFont font;
   private Preferences prefs;
   ```

3. **Initialized the new components in create()**:
   ```java
   // Initialize font
   font = new BitmapFont();
   font.setColor(Color.WHITE);
   
   // Load high score
   prefs = Gdx.app.getPreferences("dropGame");
   highScore = prefs.getInteger("highScore", 0);
   ```

4. **Updated score logic in the collision detection**:
   ```java
   // Increment score when drop is caught
   currentScore++;
   
   // Update high score if needed
   if (currentScore > highScore) {
       highScore = currentScore;
       // Save high score
       prefs.putInteger("highScore", highScore);
       prefs.flush();
   }
   ```

5. **Added score display in the draw() method**:
   ```java
   // Draw score and high score
   font.draw(spriteBatch, "Score: " + currentScore, 10, worldHeight - 10);
   font.draw(spriteBatch, "High Score: " + highScore, 10, worldHeight - 30);
   ```

6. **Added high score reload in resume()**:
   ```java
   // Reload high score in case it was changed
   highScore = prefs.getInteger("highScore", 0);
   ```

7. **Added font cleanup in dispose()**:
   ```java
   font.dispose();
   ```

These changes create a complete scoring system that tracks the current game score, saves and displays the high score, and persists between sessions using the Preferences API (which uses localStorage in HTML5).

#### What is prefs?

In this context, `prefs` is an instance of libGDX's `Preferences` interface, which provides cross-platform persistent storage for simple data.

`Preferences` in libGDX:
- Acts as a key-value store for saving game data
- Works across all platforms libGDX supports
- Automatically uses the appropriate storage mechanism for each platform:
  - Desktop: saves to local files
  - Android: uses SharedPreferences
  - HTML5/Web: uses browser's localStorage

In our code, we use it to save and load the high score:
```java
// Initialize
prefs = Gdx.app.getPreferences("dropGame");

// Load a value
highScore = prefs.getInteger("highScore", 0);

// Save a value
prefs.putInteger("highScore", highScore);
prefs.flush();  // Ensures data is written to storage
```

The `"dropGame"` string is a unique identifier that distinguishes these preferences from any other data that might be saved by other applications.


# Reference
