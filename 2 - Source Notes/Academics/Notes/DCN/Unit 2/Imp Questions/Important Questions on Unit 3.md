2025-03-06 08:37

Status:

Tags:

# Important Questions on Unit 3

# 1. Differentiate between **FDMA, TDMA, and CDMA**.

FDMA, TDMA, and CDMA are three different multiple access techniques used to allow multiple users to share the same communication medium. Here’s a detailed comparison:

---

### FDMA (Frequency Division Multiple Access)

- **Principle:**  
    Divides the available frequency band into multiple channels. Each user is assigned a unique frequency band for the duration of the connection.
    
- **Key Features:**
    
    - **Simultaneous Transmissions:** Users transmit concurrently on different frequencies.
    - **Hardware Filtering:** Requires filters to isolate channels.
    - **Interference:** Limited by frequency separation; adjacent channels need guard bands to prevent overlap.
- **Advantages:**
    
    - Simple and continuous transmission.
    - No need for complex synchronization between users.
- **Disadvantages:**
    
    - Inefficient spectrum utilization if the allocated channels are not fully used.
    - Fixed allocation can lead to wasted resources during low traffic.

---

### TDMA (Time Division Multiple Access)

- **Principle:**  
    Divides time into slots and allocates these slots to different users on the same frequency channel. Each user transmits in rapid succession, one after the other, within their assigned time slot.
    
- **Key Features:**
    
    - **Time Sharing:** Multiple users share the same frequency channel by transmitting in different time slots.
    - **Synchronization:** Requires tight synchronization to ensure users transmit in their correct time slot.
    - **Burst Transmission:** Data is sent in bursts during the assigned time slot.
- **Advantages:**
    
    - Efficient use of the available frequency since the same channel is shared.
    - Can adjust the time slot allocation based on traffic load.
- **Disadvantages:**
    
    - Requires precise timing synchronization.
    - Delay may occur if users have to wait for their time slot.
    - In burst transmissions, power amplifiers must handle higher peak powers.

---

### CDMA (Code Division Multiple Access)

- **Principle:**  
    Allows all users to transmit simultaneously over the same frequency band by assigning unique spreading codes. Each user's signal is spread over a wide frequency band and can be separated at the receiver using the same unique code.
    
- **Key Features:**
    
    - **Spread Spectrum:** Uses unique codes to distinguish between users.
    - **Simultaneous Access:** All users share the same frequency spectrum at the same time.
    - **Interference Management:** The receiver correlates the incoming signal with the expected code, which helps reduce the impact of interference from other users.
- **Advantages:**
    
    - High capacity and flexibility in resource allocation.
    - Improved privacy and resistance to interference and eavesdropping.
    - More robust in multipath environments.
- **Disadvantages:**
    
    - Complex signal processing and decoding at the receiver.
    - Requires careful power control to minimize the near-far problem (where a strong signal may overpower a weaker one).

---

### Summary Comparison

|Aspect|FDMA|TDMA|CDMA|
|---|---|---|---|
|**Resource Division**|Frequency|Time|Code|
|**Simultaneous Users**|Yes, on different frequency bands|Yes, via time slots|Yes, by using different spreading codes|
|**Synchronization**|Minimal|High (time slot alignment required)|Moderate to high (code synchronization)|
|**Spectrum Efficiency**|Can be less efficient if channels are underutilized|More efficient if time slots are well managed|High efficiency with proper power control|
|**Implementation Complexity**|Lower|Moderate|Higher|

# 2. Compare **Slotted ALOHA and Pure ALOHA** with throughput analysis.

Both Pure ALOHA and Slotted ALOHA are random access protocols that allow users to transmit data packets without prior coordination. However, they differ in their timing structure and resulting throughput. Here’s a detailed comparison along with their throughput analysis.

---

## Pure ALOHA

- **Operation:**
    
    - In Pure ALOHA, stations transmit whenever they have data to send without waiting for a specific time slot.
    - Because transmissions occur asynchronously, a packet is vulnerable to collisions with any other packet sent during a time window that spans the entire packet duration before and after its transmission.
- **Vulnerable Period:**
    
    - The vulnerable period is **2T**, where TT is the time to transmit one packet.
- **Throughput Analysis:**
    
    - Let GG be the average number of transmission attempts per packet time (including new transmissions and retransmissions).
    - The probability that a transmitted packet avoids collision is given by the probability that no other packet is transmitted during the vulnerable period, which is: Psuccess=e−2GP_\text{success} = e^{-2G}
    - The throughput SS (successful transmissions per packet time) is: S=G⋅e−2GS = G \cdot e^{-2G}
    - **Maximum Throughput:**
        - The maximum throughput occurs when G=0.5G = 0.5: S_\text{max} = 0.5 \cdot e^{-1} \approx 0.184 \quad \text{(or 18.4% of the channel capacity)}

---

## Slotted ALOHA

- **Operation:**
    
    - In Slotted ALOHA, time is divided into discrete slots of equal duration, each equal to the packet transmission time.
    - A station is allowed to transmit only at the beginning of a time slot, which synchronizes all transmissions.
- **Vulnerable Period:**
    
    - The vulnerable period is reduced to **T** (just one time slot) because transmissions are aligned with the slot boundaries.
- **Throughput Analysis:**
    
    - Using the same definition of GG (average number of transmission attempts per slot), the probability that no other transmission occurs in the same slot is: Psuccess=e−GP_\text{success} = e^{-G}
    - The throughput SS becomes: S=G⋅e−GS = G \cdot e^{-G}
    - **Maximum Throughput:**
        - The maximum throughput occurs when G=1G = 1: S_\text{max} = 1 \cdot e^{-1} \approx 0.368 \quad \text{(or 36.8% of the channel capacity)}

---

## Summary Comparison

|**Aspect**|**Pure ALOHA**|**Slotted ALOHA**|
|---|---|---|
|**Transmission Timing**|Asynchronous – transmit at any time.|Synchronous – transmit only at slot boundaries.|
|**Vulnerable Period**|2T2T|TT|
|**Throughput Formula**|S=G⋅e−2GS = G \cdot e^{-2G}|S=G⋅e−GS = G \cdot e^{-G}|
|**Maximum Throughput**|≈0.184\approx 0.184 (18.4% of capacity at G=0.5G = 0.5)|≈0.368\approx 0.368 (36.8% of capacity at G=1G = 1)|
|**Efficiency**|Lower efficiency due to longer vulnerable period.|Higher efficiency due to reduced collision window.|

# What is the problem of **collision in CSMA/CD**? How is it resolved?

In CSMA/CD (Carrier Sense Multiple Access with Collision Detection), multiple stations share a common transmission medium. The collision problem arises when two or more stations begin transmitting simultaneously, often due to propagation delays. This simultaneous transmission leads to overlapping signals (collisions), which corrupt the data frames being transmitted.

---

### How Collisions Occur

- **Carrier Sensing Limitations:**  
    Even though stations listen to the medium before transmitting, they may not detect a transmission from another station in time because of the inherent delay in signal propagation. This can lead to two stations starting their transmission almost simultaneously.
    
- **Overlapping Transmissions:**  
    When two transmissions overlap, the signals interfere with each other, resulting in data corruption. Both transmissions become unusable at the receiver end.
    

---

### Collision Resolution Mechanisms in CSMA/CD

1. **Collision Detection:**
    
    - Each station monitors the network while transmitting.
    - If a station detects a sudden increase in voltage or signal distortion (indicating that another signal is present), it concludes that a collision has occurred.
2. **Transmission Abortion and Jamming Signal:**
    
    - Once a collision is detected, the station immediately stops transmitting to avoid wasting further bandwidth.
    - It then sends out a jamming signal—a short burst of bits—to ensure that all nodes on the network are aware of the collision. This helps in synchronizing the network's response to the collision.
3. **Exponential Backoff Algorithm:**
    
    - After sending the jamming signal, the station waits for a random period before attempting to retransmit the frame.
    - The waiting time is determined using the binary exponential backoff algorithm:
        - Initially, the station picks a random number of time slots to wait.
        - If a collision happens again, the range of the random wait time doubles.
        - This exponential increase in the waiting period reduces the probability of repeated collisions in a congested network.
4. **Retransmission:**
    
    - After the backoff period expires, the station senses the medium again.
    - If the medium is idle, the station retransmits the frame.
    - This process continues until the frame is successfully transmitted or a maximum retry limit is reached.

---

### Summary

- **Problem:**  
    In CSMA/CD, collisions occur when multiple stations transmit simultaneously, leading to data corruption.
    
- **Resolution:**
    
    - **Collision Detection:** Stations monitor the medium to detect collisions.
    - **Jamming Signal:** Upon collision, a jamming signal alerts all stations.
    - **Exponential Backoff:** Stations wait for a random, increasingly longer period before retransmitting, reducing the likelihood of another collision.
    - **Retransmission:** The frame is resent after the backoff period if the channel is idle.


---
# Discuss **Carrier Sense Multiple Access (CSMA) protocols**.

Carrier Sense Multiple Access (CSMA) protocols are designed to allow multiple devices to share a common communication medium efficiently while minimizing the chance of collisions. The core idea is that before transmitting data, each station "listens" to (or senses) the medium to determine if it is idle. If the channel is in use, the station delays its transmission to avoid colliding with other transmissions. Below is a discussion of the main types and variants of CSMA protocols:

---

### Basic CSMA Operation

- **Carrier Sensing:**  
    Before a station transmits, it checks the channel to see if another transmission is already in progress.
- **Transmission Decision:**  
    If the channel is idle, the station transmits its data; if the channel is busy, it waits before trying again.

---

### Variants of CSMA Protocols

#### 1. **1-Persistent CSMA**

- **Operation:**
    - When a station senses the channel and finds it idle, it transmits immediately with a probability of 1.
    - If the channel is busy, it continues to sense the medium and transmits as soon as it becomes idle.
- **Characteristics:**
    - **Aggressive Approach:** This strategy maximizes channel usage but can lead to a high probability of collisions because multiple stations waiting for an idle channel may transmit almost simultaneously.
    - **Higher Collision Rate:** Particularly problematic in networks with high traffic.

#### 2. **Non-Persistent CSMA**

- **Operation:**
    - If the channel is busy, the station does not continuously sense the channel. Instead, it waits for a random period before checking again.
    - Once the channel is sensed to be idle, the station transmits immediately.
- **Characteristics:**
    - **Reduced Collision Probability:** The random wait time helps to stagger retransmissions, lowering the chance of simultaneous transmissions.
    - **Increased Delay:** This approach can lead to longer delays since stations might wait unnecessarily even if the channel becomes idle.

#### 3. **p-Persistent CSMA**

- **Operation:**
    - Typically used in slotted channels, the station senses the channel at the beginning of a time slot.
    - If the channel is idle, the station transmits with probability pp and defers with probability 1−p1-p until the next time slot.
- **Characteristics:**
    - **Balanced Approach:** The value of pp can be tuned to optimize performance based on traffic load.
    - **Flexibility:** It strikes a balance between the aggressive nature of 1-persistent and the conservative nature of non-persistent CSMA.

---

### Enhanced CSMA Variants for Collision Management

#### CSMA/CD (Carrier Sense Multiple Access with Collision Detection)

- **Usage:**  
    Primarily used in wired networks such as Ethernet.
    
- **How It Works:**
    
    - **Collision Detection:** While transmitting, a station continues to monitor the channel. If it detects a collision (e.g., by noticing a distortion in the signal), it immediately stops transmitting.
    - **Jamming Signal:** The station sends a jamming signal to ensure that all other nodes recognize that a collision has occurred.
    - **Exponential Backoff:** The station waits for a random, exponentially increasing amount of time before attempting to retransmit, which helps reduce the probability of repeated collisions.

#### CSMA/CA (Carrier Sense Multiple Access with Collision Avoidance)

- **Usage:**  
    Widely used in wireless networks, such as Wi-Fi (IEEE 802.11), where collision detection is challenging due to issues like the hidden node problem.
    
- **How It Works:**
    
    - **Collision Avoidance Techniques:** Instead of detecting collisions during transmission, CSMA/CA tries to avoid them by using methods such as:
        - **Random Backoff:** Stations wait for a random time period before transmitting.
        - **RTS/CTS Handshakes:** A Request-to-Send (RTS) and Clear-to-Send (CTS) exchange is used to reserve the channel before actual data transmission begins.
    - **Acknowledgments:** Successful transmissions are confirmed by acknowledgments (ACKs) from the receiver.

---

### Summary

- **CSMA protocols** help manage access to a shared medium by having stations sense the channel before transmitting.
- **1-Persistent CSMA** transmits immediately when the channel is idle, leading to higher collision probabilities.
- **Non-Persistent CSMA** introduces random waiting times when the channel is busy, reducing collisions but increasing delay.
- **p-Persistent CSMA** offers a balanced approach, especially useful in slotted channels.
- **Enhanced Protocols:**
    - **CSMA/CD** detects and resolves collisions on wired networks using collision detection and exponential backoff.
    - **CSMA/CA** avoids collisions in wireless networks through random backoff and handshake mechanisms like RTS/CTS.

---
# Reference
