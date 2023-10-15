## Report on Two-Phase Multicast Algorithm Implementation

### Introduction
This report provides an overview of the implementation of the Two-Phase Multicast algorithm using Python and socket programming. The pseudocode has been realized into a functional system for achieving total message ordering in a distributed environment. The report covers the pseudocode of the algorithm, design details, and preliminary experimental evaluation.

### Pseudocode of the Algorithm
The pseudocode provided describes a simplified Two-Phase Multicast algorithm. The primary components of the pseudocode are as follows:

1. **Class TwoPhaseMulticast:** This class represents the core of the algorithm. It maintains data structures for local time, commit time, ACKs, and a message buffer. It also creates and binds sockets for communication.

2. **Method broadcast(sender, message):** This method sends a message from the sender to all other hosts using sockets. It then calls the `receive` method to process incoming messages for the sender.

3. **Method receive(receiver):** The `receive` method is responsible for processing incoming messages for the receiver. It updates the local time, computes ACK times, and maintains a message buffer. It determines the commit time for the receiver based on the maximum ACK time.

4. **Function hostInit(numMessages, hostNo, obj):** This function simulates message sending by each host. It increments the host's local time, generates a message, broadcasts it to other hosts, and introduces random delays to simulate network latency.

5. **Function printTotalOrder(obj):** This function prints the messages in total order for each host based on the commit times. It creates a list of messages in order and displays them.

6. **Function printCommitTime(obj):** This function prints the commit times of each host.

The algorithm follows a two-phase approach, where hosts multicast messages to others, and the receiving hosts determine the commit time based on the maximum ACK time. Messages are printed in total order, ensuring that all hosts see the messages in the same order.

### Design Details
The implementation closely follows the provided pseudocode. Each host is represented as a separate thread, simulating independent hosts in a distributed system. The use of sockets and UDP communication allows messages to be exchanged between hosts. Random delays simulate network latency, contributing to a more realistic test environment.

The `TwoPhaseMulticast` class serves as the central component of the system. It encapsulates data structures and methods for message handling and ordering. The `broadcast` and `receive` methods work together to achieve total message ordering, ensuring that messages are delivered and processed correctly.

### Experimental Evaluation

### Test Case 1: No Delay
- Simulated in main.py
- Number of Hosts: 3
- Number of Messages: 2

### Test Case 2: Minimum Delay
- Simulated in test1.py
- Number of Hosts: 4
- Number of Messages: 6

### Test Case 3: Variable Delay
- Simulated in test2.py
- Number of Hosts: 5
- Number of Messages: 7

Experimental results demonstrate the correct functioning of the Two-Phase Multicast algorithm. Messages are delivered, ordered, and printed in total order, as expected.

### Conclusion
In conclusion, we have successfully implemented the Two-Phase Multicast algorithm using Python and socket programming to achieve total message ordering in a distributed system. The preliminary experimental evaluation validates the correctness of the system's operation. 
