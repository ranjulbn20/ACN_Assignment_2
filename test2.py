# Name: Ranjul Bandyopadhyay
# Entry No: 2023JCS2541
import threading
import time
import random
import socket

def hostInit(numMessages, hostNo, obj):
    for i in range(numMessages):
        obj.localTime[hostNo] += 1
        message = f"S:{hostNo},M:{i}"
        obj.broadcast(hostNo, message)
        delay = random.uniform(0.1, 0.5)  # Introduce random delays
        time.sleep(delay)

def printTotalOrder(obj):
    for r in range(obj.numHosts):
        msgOrder = []
        for s, t, m in obj.buffer:
            if obj.commitTime[r] >= t:
                msgOrder.append(f"({m},R:{r},T:{t})")

        print(f"Total Order for Host No {r}: ", msgOrder)

def printCommitTime(obj):
    for i in range(obj.numHosts):
        print(f"Commit Time of Host {i} is {obj.commitTime[i]}")

class TwoPhaseMulticast:
    def __init__(self, numHosts):
        self.numHosts = numHosts
        self.localTime = [0] * numHosts
        self.commitTime = [0] * numHosts
        self.ack = [0] * numHosts  # To store the ACK time of each sender
        self.buffer = []  # To buffer the received messages

        # Create sockets for each host
        self.sockets = [socket.socket(socket.AF_INET, socket.SOCK_DGRAM) for _ in range(numHosts)]

        for i, sock in enumerate(self.sockets):
            sock.bind(('localhost', 9000 + i))

    def broadcast(self, sender, message):
        for i in range(self.numHosts):
            if i != sender:
                self.sockets[i].sendto(message.encode(), ('localhost', 9000 + i))
                delay = random.uniform(0.1, 0.5)  # Introduce random delays when sending
                time.sleep(delay)
        self.receive(sender)

    def receive(self, receiver):
        for i, sock in enumerate(self.sockets):
            if i != receiver:
                data, addr = sock.recvfrom(1024)
                message = data.decode()
                sender = i
                self.localTime[receiver] = max(self.localTime[receiver], self.localTime[sender])
                self.localTime[receiver] += 1
                self.ack[sender] = self.localTime[receiver]
                self.buffer.append((sender, self.localTime[sender], message))

        commit_time = max(self.ack)
        self.commitTime[receiver] = commit_time + 1

if __name__ == "__main__":
    numHosts = 5
    numMessages = 7

    obj = TwoPhaseMulticast(numHosts)

    hosts = []
    for i in range(numHosts):
        t = threading.Thread(target=hostInit, args=(numMessages, i, obj))
        t.start()
        hosts.append(t)

    for t in hosts:
        t.join()

    printTotalOrder(obj)
    printCommitTime(obj)
