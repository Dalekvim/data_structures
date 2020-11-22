from node import Node


class Stack(list):
    def push(self, item):
        self.append(item)

    def pull(self):
        if self.is_empty():
            raise Exception("The stack is empty.")
        return self.pop()

    def peek(self):
        if self.is_empty():
            raise Exception("The stack is empty.")
        return self[-1]

    def is_empty(self):
        if len(self):
            return False
        return True


class LinkedStack(Node):
    def is_empty(self):
        if (self.value is None) and (self.next is None):
            return True
        return False

    def last(self):
        cur = self
        while cur.next is not None:
            cur = cur.next
        return cur

    def push(self, item):
        cur = self
        if cur.value is None:
            cur.value = item
            return
        cur = self.last()
        cur.next = Node(item)

    def pull(self):
        if self.is_empty():
            raise Exception("The stack is empty.")
        cur = self
        if cur.next is None:
            temp = cur.value
            cur.value = None
            return temp
        while cur.next.next is not None:
            cur = cur.next
        temp = cur.next.value
        cur.next = None
        return temp

    def peek(self):
        if self.is_empty():
            raise Exception("The stack is empty.")
        return self.last().value
