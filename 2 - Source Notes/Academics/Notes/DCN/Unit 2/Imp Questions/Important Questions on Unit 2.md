2025-03-06 06:16

Status: [[t-child]]

Tags: [[t-dcn]] [[t-introductiontonetworking]] [[t-dcn_unit2]] [[t-sem4]] [[t-academics]]

# Important Questions on Unit 2

# **1. Describe Framing, Framing techniques and their importance.**

**Framing** is the process of dividing raw data (bits) received from the physical layer into **structured units called frames**, which include headers and trailers for control information. It ensures that the receiver can identify the start and end of each frame and interpret the data correctly.  

---

### **Framing Techniques**  
Framing techniques are categorized based on how data is organized and delimited:  

#### **1. Fixed-Size Framing**  
- **Description**: All frames have a predefined, fixed length.  
- **Example**: ATM (Asynchronous Transfer Mode) cells (53 bytes: 5-byte header + 48-byte payload).  
- **Advantage**: Simplifies synchronization (no delimiters needed).  
- **Disadvantage**: Inefficient for variable-sized data.  

#### **2. Variable-Size Framing**  
- **Description**: Frames vary in size, requiring delimiters to mark boundaries.  
- **Approaches**:  
  - **Bit-Oriented Framing**:  
    - Treats data as a stream of bits.  
    - **Example**: **HDLC** (High-Level Data Link Control) uses the flag `01111110` to mark frame boundaries.  
    - **Bit Stuffing**: Inserts a `0` after five consecutive `1`s to avoid confusion with the flag.  
      - Example: Data `01111101` → Stuffed as `011111**0**01`.  
  - **Byte-Oriented Framing**:  
    - Treats data as a sequence of bytes.  
    - **Example**: **PPP** (Point-to-Point Protocol) uses byte stuffing with **DLE (Data Link Escape)**.  
      - Control characters (e.g., `DLE STX`, `DLE ETX`) mark frame boundaries.  
      - Example: Data `DLE` → Escaped as `DLE DLE`.  
  - **Clock-Based Framing**:  
    - Uses synchronization signals (e.g., SONET/SDH) for timing.  

---

### **Importance of Framing**  
1. **Data Delimitation**:  
   - Identifies **start/end of frames**, preventing data corruption.  
   - Example: Without flags, the receiver cannot distinguish between two consecutive frames.  

2. **Error Detection/Correction**:  
   - Headers/trailers include checksums (e.g., CRC) to detect corrupted bits.  
   - Enables retransmission (e.g., ARQ protocols).  

3. **Flow Control**:  
   - Manages data transmission speed between sender and receiver.  
   - Example: **Sliding Window Protocol** uses frame sequence numbers for efficiency.  

4. **Addressing**:  
   - Headers include **source/destination MAC addresses** for hop-to-hop delivery.  

5. **Synchronization**:  
   - Ensures sender and receiver clocks are aligned (e.g., preamble bits in Ethernet).  

6. **Media Access Control**:  
   - Prevents collisions in shared media (e.g., CSMA/CD in Ethernet).  

---

# 2. Explain **CRC error detection technique** with an example.

CRC (Cyclic Redundancy Check) is a widely used error detection technique that treats data as a polynomial over a binary field. It helps ensure that the data received is the same as the data sent, by appending a checksum (the CRC) computed through polynomial division. Here’s how it works, along with an example:

---

### How CRC Works

1. **Selection of a Generator Polynomial:**  
    Both sender and receiver agree on a generator polynomial, G(x)G(x). This polynomial is represented in binary. For example, consider:
    
    - $G(x)=x^3+x+1G(x) = x^3 + x + 1$
    - In binary form, it is **1011**.
2. **Augmenting the Data:**  
    Suppose the original message (data) is represented as a binary string, MM. The degree of G(x)G(x) (which is 3 in our example) tells us how many zeros to append.
    
    - **Example Message:** M=110100111M = 110100111
    - **Augmented Message:** Append three zeros to get 110100111000110100111000.
3. **Binary Division Using XOR:**  
    The augmented message is then divided by the generator polynomial using binary (modulo-2) division. In this division, subtraction is replaced by the XOR operation.
    
    - The division is carried out bit by bit.
    - The remainder obtained from this division is the CRC value.
4. **Forming the Transmitted Message:**  
    The computed remainder (CRC bits) is appended to the original message. This complete bit stream is what gets transmitted.
    
5. **Error Detection at the Receiver:**  
    The receiver divides the received message (original data + CRC) by the same generator polynomial.
    
    - **If the remainder is zero:** It’s assumed that no error occurred during transmission.
    - **If the remainder is non-zero:** An error is detected.

---

### Detailed Example

Let’s walk through an example with our chosen values:

- **Original Message (M):** 110100111
- **Generator Polynomial (G):** 1011 (which represents x3+x+1x^3 + x + 1)

**Step 1: Augment the Message**  
Since the degree of G(x)G(x) is 3, append three zeros:

- Augmented Message: **110100111000**

**Step 2: Perform Binary Division**  
Divide the augmented message by the generator polynomial using modulo-2 division (XOR operations). The process is similar to long division:

- **Initial Division:**
    
    - Take the first 4 bits (since the generator is 4 bits long): **1101**
    - XOR with **1011** (because the leading bit is 1): 1101⊕1011=01101101 \oplus 1011 = 0110
- **Continue the Process:**
    
    - Bring down the next bit from the augmented message.
    - Repeat the XOR division step each time the leftmost bit of the current working dividend is 1.
    - Continue until all bits of the augmented message are processed.
- **Suppose** after completing the division, the final remainder is found to be **100**.
    

**Step 3: Create the Transmitted Message**  
Append the remainder to the original message:

- **Transmitted Message:** 110100111 **100**

**Step 4: Error Detection**  
When the receiver gets the transmitted message, it divides it by 1011.

- If the division yields a remainder of **000**, the data is accepted as error-free.
- A non-zero remainder indicates an error in transmission.

---

Stop-and-Wait ARQ (Automatic Repeat reQuest) is a fundamental protocol used in data communication to ensure reliable data transfer between a sender and a receiver. Here's a detailed explanation:

---

# 4. Explain **Stop-and-Wait ARQ protocol** with a flow diagram.

Stop-and-Wait ARQ (Automatic Repeat reQuest) is a fundamental protocol used in data communication to ensure reliable data transfer between a sender and a receiver. Here's a detailed explanation:
### How Stop-and-Wait ARQ Works

1. **Frame Transmission:**
    - The sender transmits one frame (or packet) of data.
2. **Waiting for Acknowledgment (ACK):**
    - After sending the frame, the sender stops and waits for an acknowledgment from the receiver.
3. **Acknowledgment Received:**
    - If the receiver successfully receives and verifies the frame (using error detection techniques such as CRC), it sends an ACK back to the sender.
    - Upon receiving the ACK, the sender proceeds to transmit the next frame.
4. **Timeout and Retransmission:**
    - If the sender does not receive an ACK within a predetermined timeout period, it assumes the frame was lost or corrupted.
    - The sender then retransmits the same frame.
5. **Cycle Repeats:**
    - This process repeats for each frame until the entire data is transmitted reliably.

---

### Key Characteristics

- **Simplicity:**  
    The protocol is easy to implement since only one frame is in transit at any time.
    
- **Reliability:**  
    It guarantees that each frame is received correctly, as the sender waits for confirmation before proceeding.
    
- **Error Recovery:**  
    The retransmission mechanism ensures that lost or corrupted frames are resent, enhancing data reliability.
    

---

### Advantages and Disadvantages

#### Advantages:

- **Simplicity:**  
    Straightforward design makes it easy to understand and implement.
    
- **Reliable Transmission:**  
    Ensures that every frame is acknowledged before sending the next, which reduces the chance of data loss.
    

#### Disadvantages:

- **Low Channel Utilization:**  
    Since the sender waits for an ACK after every frame, the link can be idle during the round-trip time, especially problematic in high-latency networks.
    
- **Limited Throughput:**  
    The stop-and-wait nature limits the amount of data that can be transmitted in a given time, making it inefficient for large data transfers or high-speed networks.
    

---

# 5. Compare **Go-Back-N vs Selective Repeat ARQ**.

Both Go-Back-N and Selective Repeat ARQ are sliding window protocols that ensure reliable data transmission, but they differ in how they handle error recovery and manage the transmission window.

---

### Go-Back-N ARQ

- **Transmission Window:**  
    The sender can transmit multiple frames up to a fixed window size without waiting for individual acknowledgments.
    
- **Error Recovery:**  
    If an error (or a timeout) is detected in a frame, the sender **goes back** and retransmits that frame along with all subsequent frames, even if some were received correctly.
    
- **Acknowledgment:**  
    Acknowledgments are typically cumulative. The receiver sends an ACK for the highest contiguous sequence of correctly received frames. Any frame after the first error is ignored, even if received without error.
    
- **Buffering at Receiver:**  
    The receiver generally does not buffer out-of-order frames. It only accepts frames in order.
    
- **Efficiency:**  
    While simple, Go-Back-N can be inefficient on noisy channels because a single error can force the retransmission of many correct frames.
    

---

### Selective Repeat ARQ

- **Transmission Window:**  
    Similar to Go-Back-N, the sender can transmit multiple frames, but the protocol handles errors more granularly.
    
- **Error Recovery:**  
    When a frame error is detected, **only that specific frame** is retransmitted. The receiver buffers any out-of-order frames until the missing ones are received, ensuring all frames can eventually be put in order.
    
- **Acknowledgment:**  
    The receiver sends individual acknowledgments for each correctly received frame, allowing the sender to identify and retransmit only the frames that were lost or corrupted.
    
- **Buffering at Receiver:**  
    The receiver must maintain a buffer to store out-of-order frames until any missing frames are received.
    
- **Efficiency:**  
    More bandwidth-efficient in environments with higher error rates because it avoids the unnecessary retransmission of correctly received frames. However, it requires more complex control logic and additional buffering at the receiver.
    

---

### Summary Comparison

|Feature|Go-Back-N ARQ|Selective Repeat ARQ|
|---|---|---|
|**Error Recovery**|Retransmits the error frame and all subsequent frames.|Retransmits only the error frame(s).|
|**Acknowledgments**|Uses cumulative acknowledgments.|Uses individual acknowledgments.|
|**Receiver Buffering**|Minimal buffering; only accepts in-order frames.|Requires buffering of out-of-order frames.|
|**Complexity**|Simpler to implement.|More complex due to selective retransmissions and buffering.|
|**Efficiency**|Less efficient in high-error environments.|More efficient, as only erroneous frames are resent.|
# Draw and explain **HDLC frame format**.
![[Pasted image 20250306074109.png]]

HDLC (High-Level Data Link Control) is a bit-oriented protocol that structures data into frames for reliable transmission over synchronous links. The HDLC frame format is designed to encapsulate data and control information, and it includes several key fields that allow the receiver to delimit the frame, manage addressing, control flow, and detect errors. Below is an explanation of the HDLC frame format along with its key components:

---

### HDLC Frame Structure

An HDLC frame is generally composed of the following fields:

1. **Flag Field:**
    
    - **Purpose:** Marks the beginning and end of a frame.
    - **Value:** A fixed 8-bit pattern, typically `01111110` (hexadecimal 0x7E).
    - **Usage:** Both the sender and receiver use this unique bit pattern to identify frame boundaries.
2. **Address Field:**
    
    - **Purpose:** Identifies the station (or stations) involved in the communication.
    - **Details:**
        - In point-to-point configurations, this field might be a single byte (often set to a default value like `11111111`) since there’s usually only one secondary station.
        - In multipoint configurations, it can be used to differentiate among multiple stations on the same link.
3. **Control Field:**
    
    - **Purpose:** Contains control information needed for managing the link, such as frame sequencing, acknowledgments, and flow control.
    - **Variations:**
        - **I-frames (Information frames):** Carry user data along with sequence numbers for error detection and correction.
        - **S-frames (Supervisory frames):** Used for control purposes (e.g., acknowledgments, request to resend).
        - **U-frames (Unnumbered frames):** Used for link management tasks and may not include sequence numbers.
    - **Size:** Often 8 bits, though the length can vary based on the specific HDLC mode.
4. **Information Field:**
    
    - **Purpose:** Carries the actual payload or user data.
    - **Details:**
        - This field is variable in length.
        - In control frames (such as certain S-frames), this field might be absent.
5. **Frame Check Sequence (FCS):**
    
    - **Purpose:** Provides error detection by appending a cyclic redundancy check (CRC) to the frame.
    - **Details:**
        - Typically, a 16-bit or 32-bit FCS is used.
        - The FCS is computed over the Address, Control, and Information fields (the flags are excluded).
        - At the receiver, recalculating the FCS and comparing it with the transmitted FCS allows detection of any errors in transmission.
6. **Closing Flag Field:**
    
    - **Purpose:** Similar to the starting flag, it marks the end of the frame using the same fixed pattern `01111110`.

---

# Reference