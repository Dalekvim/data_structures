"""
A queue is a first in last out data structure,
which means the first element you add will be the first taken out.
"""

import node as Node


class Queue:
    """
    This queue uses the linked list implimentation.
    """
    def __init__(self):
        self.front = self.rear = None

    def enqueue(self, item):
        if not self.front:

