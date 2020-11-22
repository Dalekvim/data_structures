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
