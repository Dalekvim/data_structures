import unittest
from node import Node
from stack import Stack, LinkedStack


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


if __name__ == '__main__':
    unittest.main()
