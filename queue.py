"""
A queue is a first in last out data structure,
which means the first element you add will be the first taken out.
"""

from node import Node


class Queue:
    """
    This queue uses the linked list implementation.
    """

    def __init__(self):
        self.front = self.rear = None

    def is_empty(self):
        return not self.front

    def peek(self):
        if self.is_empty():
            raise Exception("The queue is empty.")

        return self.front.value

    def enqueue(self, item):

        temp = Node(item)

        if self.is_empty():
            self.front = self.rear = temp
            return

        self.rear.next = temp
        self.rear = self.rear.next

    def dequeue(self):

        temp = self.peek()
        self.front = self.front.next

        return temp


class CircularQueue(list):

    def __init__(self, size):
        super().__init__()

        if size < 1:
            raise Exception("The queue is too small.")

        self.size = size
        for i in range(size):
            self.append(None)

        self.front = self.rear = -1

    def is_full(self):
        return self.front == (self.rear + 1) % self.size

    def is_empty(self):
        return self.front == self.rear == -1

    def peek(self):
        if self.is_empty():
            raise Exception("The queue is empty.")
        return self[self.front]

    def enqueue(self, item):
        if self.is_full():
            raise Exception("The queue is full.")
        if self.front == self.rear == -1:
            self.front = 0
        self.rear = (self.rear + 1) % self.size
        self[self.rear] = item

    def dequeue(self):
        temp = self.peek()

        if self.front == self.rear:
            self.front = self.rear = -1
        else:
            self.front = (self.front + 1) % self.size

        return temp
