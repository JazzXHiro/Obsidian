2025-03-31 20:41

Status:

Tags:

# Button Hover


# Changes for Adding Button Hover Effects

1. **Added Hover State Variables**
   ```java
   // Button hover states
   private boolean adminButtonHovered = false;
   private boolean userButtonHovered = false;
   ```

2. **Updated Input Handling to Track Hover States**
   ```java
   // Update button hover states
   touchPos.set(Gdx.input.getX(), Gdx.input.getY());
   viewport.unproject(touchPos);
   
   adminButtonHovered = adminButton.contains(touchPos.x, touchPos.y);
   userButtonHovered = userButton.contains(touchPos.x, touchPos.y);
   ```

3. **Simplified Click Detection**
   ```java
   // Changed from:
   if (adminButton.contains(touchPos.x, touchPos.y)) {
   
   // To:
   if (adminButtonHovered) {
   ```

4. **Added Admin Button Border Drawing**
   ```java
   // Draw white border if button is hovered
   if (adminButtonHovered) {
       Color prevColor = spriteBatch.getColor();
       spriteBatch.setColor(Color.WHITE);
       
       // Draw border lines (2 pixels wide)
       float borderWidth = 2;
       // Top border
       spriteBatch.draw(backgroundTexture, adminButton.x, adminButton.y + adminButton.height - borderWidth, 
                       adminButton.width, borderWidth);
       // Bottom border
       spriteBatch.draw(backgroundTexture, adminButton.x, adminButton.y, 
                       adminButton.width, borderWidth);
       // Left border
       spriteBatch.draw(backgroundTexture, adminButton.x, adminButton.y, 
                       borderWidth, adminButton.height);
       // Right border
       spriteBatch.draw(backgroundTexture, adminButton.x + adminButton.width - borderWidth, adminButton.y, 
                       borderWidth, adminButton.height);
       
       spriteBatch.setColor(prevColor);
   }
   ```

5. **Added User Button Border Drawing**
   ```java
   // Draw white border if button is hovered
   if (userButtonHovered) {
       Color prevColor = spriteBatch.getColor();
       spriteBatch.setColor(Color.WHITE);
       
       // Draw border lines (2 pixels wide)
       float borderWidth = 2;
       // Top border
       spriteBatch.draw(backgroundTexture, userButton.x, userButton.y + userButton.height - borderWidth, 
                       userButton.width, borderWidth);
       // Bottom border
       spriteBatch.draw(backgroundTexture, userButton.x, userButton.y, 
                       userButton.width, borderWidth);
       // Left border
       spriteBatch.draw(backgroundTexture, userButton.x, userButton.y, 
                       borderWidth, userButton.height);
       // Right border
       spriteBatch.draw(backgroundTexture, userButton.x + userButton.width - borderWidth, userButton.y, 
                       borderWidth, userButton.height);
       
       spriteBatch.setColor(prevColor);
   }
   ```

These changes work together to create a visual hover effect where white borders appear around buttons when the mouse cursor hovers over them, providing better visual feedback to the user.


# Reference
