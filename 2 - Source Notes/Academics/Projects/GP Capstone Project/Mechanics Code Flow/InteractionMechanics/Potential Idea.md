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

#### Document Interactable
##### DocumentInteractable.cs
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

#### Environmental Clue (Inspectable Object)

##### InspectableObject.cs
```
using UnityEngine;

public class InspectableObject : MonoBehaviour, IInteractable
{
    private ClueCatalyst clueCatalyst;
    
    [Header("Inspection Settings")]
    [SerializeField] private string objectName = "Strange Markings";
    [SerializeField] private bool highlightOnLookAt = true;
    [SerializeField] private Material highlightMaterial;
    
    private Material originalMaterial;
    private Renderer objectRenderer;

    private void Awake()
    {
        clueCatalyst = GetComponent<ClueCatalyst>();
        objectRenderer = GetComponent<Renderer>();

        if (objectRenderer != null)
        {
            originalMaterial = objectRenderer.material;
        }

        if (clueCatalyst == null)
        {
            Debug.LogError($"ClueCatalyst component NOT FOUND on {gameObject.name}!");
        }
    }

    public void Interact()
    {
        Debug.Log($"Inspecting: {objectName}");
        
        if (clueCatalyst != null)
        {
            clueCatalyst.CreateClue();
        }
    }

    // Optional: Add highlight effect when player looks at it
    private void OnMouseEnter()
    {
        if (highlightOnLookAt && highlightMaterial != null && objectRenderer != null)
        {
            objectRenderer.material = highlightMaterial;
        }
    }

    private void OnMouseExit()
    {
        if (highlightOnLookAt && originalMaterial != null && objectRenderer != null)
        {
            objectRenderer.material = originalMaterial;
        }
    }
}
```

#### Audio Clue Trigger

##### AudioClueInteractable.cs
```
using UnityEngine;

public class AudioClueInteractable : MonoBehaviour, IInteractable
{
    private ClueCatalyst clueCatalyst;
    
    [Header("Audio Settings")]
    [SerializeField] private AudioClip clueAudio;
    [SerializeField] private string audioDescription = "Distant whispers...";
    [SerializeField] private bool autoPlayOnInteract = true;
    
    private AudioSource audioSource;

    private void Awake()
    {
        clueCatalyst = GetComponent<ClueCatalyst>();
        audioSource = GetComponent<AudioSource>();

        if (audioSource == null)
        {
            audioSource = gameObject.AddComponent<AudioSource>();
        }

        if (clueCatalyst == null)
        {
            Debug.LogError($"ClueCatalyst component NOT FOUND on {gameObject.name}!");
        }
    }

    public void Interact()
    {
        Debug.Log($"Listening to: {audioDescription}");
        
        // Play audio clue
        if (autoPlayOnInteract && clueAudio != null && audioSource != null)
        {
            audioSource.clip = clueAudio;
            audioSource.Play();
        }
        
        // Add the clue
        if (clueCatalyst != null)
        {
            clueCatalyst.CreateClue();
        }
    }
}
```

#### Memory/Flashback Trigger

##### MemoryTrigger.cs
```
using System.Collections;
using UnityEngine;

public class MemoryTrigger : MonoBehaviour, IInteractable
{
    private ClueCatalyst clueCatalyst;
    
    [Header("Memory Settings")]
    [SerializeField] private string memoryDescription = "A faded memory surfaces...";
    [SerializeField] private GameObject visionOverlay;
    [SerializeField] private float visionDuration = 3f;
    [SerializeField] private AudioClip memorySound;
    
    private AudioSource audioSource;
    private bool hasTriggered = false;

    private void Awake()
    {
        clueCatalyst = GetComponent<ClueCatalyst>();
        audioSource = GetComponent<AudioSource>();

        if (visionOverlay != null)
        {
            visionOverlay.SetActive(false);
        }

        if (clueCatalyst == null)
        {
            Debug.LogError($"ClueCatalyst component NOT FOUND on {gameObject.name}!");
        }
    }

    public void Interact()
    {
        if (hasTriggered) return;
        
        hasTriggered = true;
        Debug.Log($"Memory triggered: {memoryDescription}");
        
        StartCoroutine(PlayMemorySequence());
        
        // Add the clue
        if (clueCatalyst != null)
        {
            clueCatalyst.CreateClue();
        }
    }

    private IEnumerator PlayMemorySequence()
    {
        // Show vision overlay
        if (visionOverlay != null)
        {
            visionOverlay.SetActive(true);
        }

        // Play sound
        if (audioSource != null && memorySound != null)
        {
            audioSource.PlayOneShot(memorySound);
        }

        // Optional: Reduce sanity during memory
        if (SanityManager.Instance != null)
        {
            // Memories could drain sanity temporarily
        }

        yield return new WaitForSeconds(visionDuration);

        // Hide overlay
        if (visionOverlay != null)
        {
            visionOverlay.SetActive(false);
        }
    }
}
```

### 4. Enhanced Journal Manager with Categories

#### JournalManager.cs
```
using System.Collections.Generic;
using System.Text;
using UnityEngine;
using TMPro;

public class JournalManager : MonoBehaviour
{
    [SerializeField] private GameObject journalPage;
    [SerializeField] private TMP_Text clueTextBox;
    [SerializeField] private string[] noClueText;
    
    [Header("Category Toggles")]
    [SerializeField] private bool showDiscoveries = true;
    [SerializeField] private bool showDocuments = true;
    [SerializeField] private bool showEnvironmental = true;
    [SerializeField] private bool showAudio = true;
    [SerializeField] private bool showMemories = true;
    
    private bool openBook;

    private void Update()
    {
        if (Input.GetKeyDown(KeyCode.J))
        {
            OpenJournalBook();
        }
    }

    public void OpenJournalBook()
    {
        openBook = !openBook;
        Debug.Log($"Journal opened: {openBook}");
        CreatePage();
        WriteQuests();
    }

    private void CreatePage()
    {
        if (journalPage != null)
        {
            journalPage.SetActive(openBook);
        }
    }

    private void WriteQuests()
    {
        Debug.Log($"WriteQuests called. Clues in MainManager: {MainManager.mainManager.clueNames.Count}");
        
        if (clueTextBox != null)
        {
            if (MainManager.mainManager.clueNames.Count == 0)
            {
                Debug.Log("No clues found, showing placeholder text");
                if (noClueText != null && noClueText.Length > 0)
                {
                    int randomNumber = Random.Range(0, noClueText.Length);
                    clueTextBox.text = noClueText[randomNumber];
                }
            }
            else
            {
                StringBuilder stringBuilder = new StringBuilder();
                
                // Add categorized clues
                if (showDiscoveries && MainManager.mainManager.discoveryClues.Count > 0)
                {
                    stringBuilder.AppendLine("=== DISCOVERIES ===");
                    AppendClues(stringBuilder, MainManager.mainManager.discoveryClues);
                    stringBuilder.AppendLine();
                }
                
                if (showDocuments && MainManager.mainManager.documentClues.Count > 0)
                {
                    stringBuilder.AppendLine("=== DOCUMENTS ===");
                    AppendClues(stringBuilder, MainManager.mainManager.documentClues);
                    stringBuilder.AppendLine();
                }
                
                if (showEnvironmental && MainManager.mainManager.environmentalClues.Count > 0)
                {
                    stringBuilder.AppendLine("=== OBSERVATIONS ===");
                    AppendClues(stringBuilder, MainManager.mainManager.environmentalClues);
                    stringBuilder.AppendLine();
                }
                
                if (showAudio && MainManager.mainManager.audioClues.Count > 0)
                {
                    stringBuilder.AppendLine("=== AUDIO CLUES ===");
                    AppendClues(stringBuilder, MainManager.mainManager.audioClues);
                    stringBuilder.AppendLine();
                }
                
                if (showMemories && MainManager.mainManager.memoryClues.Count > 0)
                {
                    stringBuilder.AppendLine("=== MEMORIES ===");
                    AppendClues(stringBuilder, MainManager.mainManager.memoryClues);
                }

                clueTextBox.text = stringBuilder.ToString();
                Debug.Log($"Journal text set with {MainManager.mainManager.clueNames.Count} total clues");
            }

            clueTextBox.rectTransform.sizeDelta = new Vector2(
                clueTextBox.rectTransform.sizeDelta.x, 
                clueTextBox.preferredHeight
            );
        }
        else
        {
            Debug.LogError("ClueTextBox is NULL!");
        }
    }

    private void AppendClues(StringBuilder sb, List<string> clues)
    {
        foreach (string clue in clues)
        {
            sb.AppendLine($"• {clue}");
        }
    }

    // Public methods to toggle categories
    public void ToggleDiscoveries() => showDiscoveries = !showDiscoveries;
    public void ToggleDocuments() => showDocuments = !showDocuments;
    public void ToggleEnvironmental() => showEnvironmental = !showEnvironmental;
    public void ToggleAudio() => showAudio = !showAudio;
    public void ToggleMemories() => showMemories = !showMemories;
}
```

### Setup Instructions



---
# Reference
