class Node:
    def __init__(self, prev=None, val=None, _next=None):
        self.prev = prev
        self.val = val
        self.next = _next


class DoublyLinkedList:
    def __init__(self, node=Node()):
        self.node = node

    def __repr__(self):
        return self.display()

    def __getitem__(self, item):
        cur = self.node
        try:
            for i in range(item+1):
                cur = cur.next
            if cur.val:
                pass
        except AttributeError:
            raise IndexError("List index out of range.")
        return cur

    def append(self, val):
        cur = self.last()
        cur.next = Node(cur, val)

    def as_array(self):
        array = []
        cur = self.node
        while cur is not None:
            array.append(cur.val)
            cur = cur.next
        array.append(cur)
        return array

    def as_reversed_array(self):
        reversed_array = []
        cur = self.last()
        while cur is not None:
            reversed_array.append(cur.val)
            cur = cur.prev
        reversed_array = [cur] + reversed_array
        return reversed_array

    def last(self):
        cur = self.node
        while cur.next is not None:
            cur = cur.next
        return cur

    def display(self):
        return ' <-> '.join([str(i) for i in self.as_array()])


doulby_linked_list = DoublyLinkedList()
doulby_linked_list.append(3)
doulby_linked_list.append(5)

print(doulby_linked_list.display())
print(doulby_linked_list.as_array())
print(doulby_linked_list.as_reversed_array())
print(doulby_linked_list)
print(doulby_linked_list[2].val)