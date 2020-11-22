import unittest
from node import Node
from stack import Stack, LinkedStack
from queue import Queue


class MyTestCase(unittest.TestCase):
    string1 = "testing"
    string2 = "another_test"

    def test_node(self):
        # Tests whether the value of the node.
        node = Node(self.string1)
        self.assertEqual(node.value, self.string1)

        # Tests the next pointer in the node.
        node.next = Node(self.string2)
        self.assertEqual(node.next.value, self.string2)

    def test_stack(self):
        stack = Stack()

        # The new stack should be empty.
        self.assertEqual(stack.is_empty(), True)

        # Pushing one item.
        stack.push(self.string1)
        self.assertEqual(stack.peek(), self.string1)

        # Now the stack should not be empty.
        self.assertEqual(stack.is_empty(), False)

        # Pushing another item.
        stack.push(self.string2)
        self.assertEqual(stack.peek(), self.string2)

        # Pulling should return the items in the opposite order
        # to the way they were inputted.
        self.assertEqual(stack.pull(), self.string2)
        self.assertEqual(stack.pull(), self.string1)

        # Now the stack should be empty.
        self.assertEqual(stack.is_empty(), True)

        # Pulling an empty stack should cause an error.
        with self.assertRaises(Exception):
            stack.pull()

        # Peeking at an empty stack should cause an error.
        with self.assertRaises(Exception):
            stack.peek()

    def test_linked_stack(self):
        linked_stack = LinkedStack()

        # The new linked stack should be empty.
        self.assertEqual(linked_stack.is_empty(), True)

        # Pushing one item
        linked_stack.push(self.string1)
        self.assertEqual(linked_stack.peek(), self.string1)

        # Now the stack should not be empty.
        self.assertEqual(linked_stack.is_empty(), False)

        # Pushing another item.
        linked_stack.push(self.string2)
        self.assertEqual(linked_stack.peek(), self.string2)

        # Pulling should return the items in the opposite order
        # to the way they were inputted.
        self.assertEqual(linked_stack.pull(), self.string2)
        self.assertEqual(linked_stack.pull(), self.string1)

        # Now the stack should be empty.
        self.assertEqual(linked_stack.is_empty(), True)

        # Pulling an empty stack should cause an error.
        with self.assertRaises(Exception):
            stack.pull()

        # Peeking at an empty stack should cause an error.
        with self.assertRaises(Exception):
            stack.peek()

    def test_queue(self):
        queue = Queue()

        # New queues should be empty.
        self.assertEqual(queue.is_empty(), True)

        # Added an item to the queue.
        queue.enqueue(self.string1)
        self.assertEqual(queue.peek(), self.string1)

        # Now the queue should no longer be empty.
        self.assertEqual(queue.is_empty(), False)

        # Added another item to the list.
        queue.enqueue(self.string2)
        # Unlike in stacks, when new items are added to the queue,
        # what's at the front does not change.
        self.assertEqual(queue.peek(), self.string1)

        # The strings should be returned in FILO order.
        self.assertEqual(queue.dequeue(), self.string1)
        self.assertEqual(queue.dequeue(), self.string2)

        # Now that both strings have been dequeued,
        # the queue should be empty.
        self.assertEqual(queue.is_empty(), True)

        # Peeking at an empty queue should cause an error.
        with self.assertRaises(Exception):
            queue.peek()

        # Trying to dequeue an empty queue should cause an error.
        with self.assertRaises(Exception):
            queue.dequeue()


if __name__ == '__main__':
    unittest.main()
