2025-04-24 16:25

Status:

Tags:

# Web Storage


In the web version of the Drop game, data is stored in two places:

## 1. Browser's localStorage
The primary storage mechanism uses the browser's built-in localStorage API:

```java
// In WebDatabaseManager.java
private native void setLocalStorageItem(String key, String value) /*-{
    try {
        $wnd.localStorage.setItem(key, value);
    } catch(e) {
        console.log("LocalStorage error: " + e);
    }
}-*/;
```

The data is serialized to JSON format before storage:
- High scores: `{"username1":100,"username2":200,...}`
- Usernames: `["username1","username2",...]`

Keys used in localStorage:
- `highScores`: JSON object mapping usernames to scores
- `usernames`: JSON array of all usernames
- `userList`: Comma-separated usernames (legacy format)
- `username_score`: Individual score entries

## 2. Remote Server Storage
The `WebSyncManager` handles synchronizing with a remote server:

```java
// In WebDatabaseManager constructor
syncManager.fetchHighScores(new WebSyncManager.FetchCallback() {
    @Override
    public void onComplete(boolean success, ObjectMap<String, Integer> remoteHighScores, 
                          Array<String> remoteUsernames) {
        if (success) {
            // Merge remote data with local data
            mergeData(remoteHighScores, remoteUsernames);
            saveToLocalStorage();
        }
    }
});
```

The game periodically syncs with this remote storage every 60 seconds:
```java
// In Main.java render method
syncTimer += Gdx.graphics.getDeltaTime();
if (syncTimer >= SYNC_INTERVAL) { // SYNC_INTERVAL = 60
    syncTimer = 0;
    dbManager.flush(); // Triggers sync in WebDatabaseManager
}
```

This dual-storage approach provides both offline functionality and cross-device synchronization for web players.


Let me check the LocalDatabaseManager implementation to see how local storage is handled:

Read file: core/src/main/java/com/badlogic/drop/LocalDatabaseManager.java
The Drop game doesn't use a traditional database file. Instead, it uses platform-specific storage mechanisms:

1. **For local/desktop platforms:**
   - Uses LibGDX's Preferences system (`LocalDatabaseManager.java`)
   - Data is stored in a platform-specific location:
     - **Windows**: Registry at `HKEY_CURRENT_USER\Software\JavaSoft\Prefs\dropGame`
     - **macOS**: `~/Library/Preferences/dropGame.plist`
     - **Linux**: `~/.java/.userPrefs/dropGame/prefs.xml`
     - **Android**: SharedPreferences in `/data/data/[package-name]/shared_prefs/dropGame.xml`

2. **For web platforms:**
   - Uses browser's localStorage (`WebDatabaseManager.java`)
   - Stored in the browser's internal storage area
   - No physical file location - managed by the browser

No traditional database files (like SQLite) are used. The game uses key-value storage native to each platform instead of a dedicated database system.

If you're looking for the saved data on your system, check the platform-specific locations mentioned above, but note they may be in binary format and not directly readable.


Yes, the web version of the game is designed to sync data across different devices, as implemented in the `WebSyncManager` class. Here's how the synchronization works:

1. **Initial Data Load**: When a user opens the web version on any device:
   ```java
   // In WebDatabaseManager constructor
   syncManager.fetchHighScores(new WebSyncManager.FetchCallback() {
       @Override
       public void onComplete(boolean success, ObjectMap<String, Integer> remoteHighScores, Array<String> remoteUsernames) {
           if (success) {
               // Merge remote data with local data
               mergeData(remoteHighScores, remoteUsernames);
               saveToLocalStorage();
           }
       }
   });
   ```

2. **Periodic Syncing**: The game automatically syncs every 60 seconds:
   ```java
   // In Main.java's render method
   syncTimer += Gdx.graphics.getDeltaTime();
   if (syncTimer >= SYNC_INTERVAL) { // SYNC_INTERVAL = 60 seconds
       syncTimer = 0;
       dbManager.flush(); // Triggers sync in WebDatabaseManager
   }
   ```

3. **Score Updates**: When a user achieves a new high score:
   ```java
   // In WebDatabaseManager's saveHighScore method
   if (initialSyncDone) {
       syncManager.syncHighScores(highScores, usernames);
   }
   ```

4. **Data Merging**: The system intelligently merges local and remote data:
   ```java
   // Keep the higher score between local and remote
   if (remoteScore > localScore) {
       highScores.put(username, remoteScore);
   }
   ```

This ensures that:
- A player can continue their game with their high scores on any device
- All players see a consistent global leaderboard
- The highest score for each player is preserved across all their devices
- Even if a player plays offline, their scores will sync when they reconnect

The sync system uses a "highest score wins" conflict resolution strategy, ensuring players don't lose their best performances regardless of which device they achieved them on.

# Reference
