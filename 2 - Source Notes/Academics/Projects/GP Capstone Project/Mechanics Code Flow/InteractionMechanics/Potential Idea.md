	2025-11-29 21:01

Status:

Tags:

---
# Potential Idea

## How can I implement additional interactable objects that provide different types of clues in the game?

### 1. Extend the Clue System with Categories
#### ClueCatalyst.cs

```
using System.Collections;
using UnityEngine;

public enum ClueType
{
    Discovery,      // Found objects/evidence
    Document,       // Notes, letters, journals
    Environmental,  // Visual observations
    Audio,          // Sound-based clues
    Memory          // Flashback triggers
}

public class ClueCatalyst : MonoBehaviour
{
    [Header("Clue Settings")]
    [SerializeField] private string clue;
    [SerializeField] private ClueType clueType = ClueType.Discovery;
    
    [Header("UI Settings")]
    [SerializeField] private GameObject notification;
    [SerializeField] private float notificationDuration = 3f;
    
    [Header("Optional: Custom Behavior")]
    [SerializeField] private bool destroyAfterInteraction = false;
    [SerializeField] private bool canInteractMultipleTimes = false;
    
    private bool clueAdded = false;
    private Coroutine hideNotificationCoroutine;

    public void CreateClue()
    {
        Debug.Log($"CreateClue called. Clue: '{clue}', Type: {clueType}, ClueAdded: {clueAdded}");

        if (string.IsNullOrEmpty(clue))
        {
            Debug.LogWarning("Clue text is empty!");
            return;
        }

        if (!clueAdded || canInteractMultipleTimes)
        {
            if (!clueAdded)
            {
                clueAdded = true;
                AddClueToManager();
            }

            ShowNotification();

            if (destroyAfterInteraction)
            {
                Destroy(gameObject, notificationDuration);
            }
        }
        else
        {
            Debug.LogWarning($"Clue already added and cannot interact multiple times.");
        }
    }

    private void AddClueToManager()
    {
        // Add to main clue list
        MainManager.mainManager.clueNames.Add(clue);
        
        // Add to categorized list (you'll need to add this to MainManager)
        switch (clueType)
        {
            case ClueType.Discovery:
                MainManager.mainManager.discoveryClues.Add(clue);
                break;
            case ClueType.Document:
                MainManager.mainManager.documentClues.Add(clue);
                break;
            case ClueType.Environmental:
                MainManager.mainManager.environmentalClues.Add(clue);
                break;
            case ClueType.Audio:
                MainManager.mainManager.audioClues.Add(clue);
                break;
            case ClueType.Memory:
                MainManager.mainManager.memoryClues.Add(clue);
                break;
        }

        Debug.Log($"Clue '{clue}' added as {clueType}. Total clues: {MainManager.mainManager.clueNames.Count}");
    }

    private void ShowNotification()
    {
        if (notification != null)
        {
            notification.SetActive(true);

            if (hideNotificationCoroutine != null)
            {
                StopCoroutine(hideNotificationCoroutine);
            }

            hideNotificationCoroutine = StartCoroutine(HideNotificationAfterDelay());
        }
    }

    private IEnumerator HideNotificationAfterDelay()
    {
        yield return new WaitForSeconds(notificationDuration);

        if (notification != null)
        {
            notification.SetActive(false);
        }
    }

    public ClueType GetClueType() => clueType;
}

```

### 2. Update MainManager to Store Categorized Clues
#### MainManager.cs
```
using System.Collections.Generic;
using UnityEngine;

public class MainManager : MonoBehaviour
{
    public static MainManager mainManager;
    
    [Header("All Clues")]
    public List<string> clueNames = new List<string>();
    
    [Header("Categorized Clues")]
    public List<string> discoveryClues = new List<string>();
    public List<string> documentClues = new List<string>();
    public List<string> environmentalClues = new List<string>();
    public List<string> audioClues = new List<string>();
    public List<string> memoryClues = new List<string>();

    private void Awake()
    {
        if (mainManager == null)
        {
            mainManager = this;
            DontDestroyOnLoad(gameObject);
        }
        else
        {
            Destroy(gameObject);
        }
    }
}

```

### 3. Create Different Interactable Object Types
```
using UnityEngine;

public class DocumentInteractable : MonoBehaviour, IInteractable
{
    private ClueCatalyst clueCatalyst;
    
    [Header("Document Settings")]
    [SerializeField] private string documentTitle = "Mysterious Letter";
    [SerializeField] private AudioClip paperRustleSound;
    
    private AudioSource audioSource;

    private void Awake()
    {
        clueCatalyst = GetComponent<ClueCatalyst>();
        audioSource = GetComponent<AudioSource>();

        if (clueCatalyst == null)
        {
            Debug.LogError($"ClueCatalyst component NOT FOUND on {gameObject.name}!");
        }
    }

    public void Interact()
    {
        Debug.Log($"Reading document: {documentTitle}");
        
        // Play sound effect
        if (audioSource != null && paperRustleSound != null)
        {
            audioSource.PlayOneShot(paperRustleSound);
        }
        
        // Add the clue
        if (clueCatalyst != null)
        {
            clueCatalyst.CreateClue();
        }
    }
}
```



---
# Reference
