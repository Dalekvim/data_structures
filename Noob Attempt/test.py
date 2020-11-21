import unittest
from unittest import TestCase
from linked_list import LinkedList

class LinkedListTest(TestCase):

  def setUp(self):
    self.linked_list = LinkedList()
  
  def test_list_init(self):
    _list = [1, "hello"]
    linked_list = LinkedList(_list)

    self.assertEqual(linked_list.size(), 2)

    self.assertEqual(linked_list.pop(), "hello")
    self.assertEqual(linked_list.size(), 1)

    self.assertEqual(linked_list.pop(), 1)
    self.assertEqual(linked_list.size(), 0)

  def test_linked_list(self):
    self.assertIsNotNone(str(self.linked_list))

    self.linked_list.append(1)
    self.assertIsNotNone(str(self.linked_list))

    self.linked_list.append("hello")
    self.assertIsNotNone(str(self.linked_list))

  def test_as_list(self):
    self.assertEqual(len(self.linked_list.as_list()), 0)

  def test_last(self):
    self.assertIsNone(self.linked_list.last().next)

    self.linked_list.append(1)
    self.assertIsNone(self.linked_list.last().next)

    self.linked_list.append("hello")
    self.assertIsNone(self.linked_list.last().next)

  def test_append(self):
    self.linked_list.append(1)
    self.assertEqual(self.linked_list.size(), 1)

    self.linked_list.append("hello")
    self.assertEqual(self.linked_list.size(), 2)
  
  def test_pop(self):
    self.linked_list.append(1)
    self.linked_list.append("hello")

    self.assertEqual(self.linked_list.size(), 2)

    self.assertEqual(self.linked_list.pop(), "hello")
    self.assertEqual(self.linked_list.size(), 1)

    self.assertEqual(self.linked_list.pop(), 1)
    self.assertEqual(self.linked_list.size(), 0)

  def test_index(self):
    self.linked_list.append(1)
    self.assertEqual(self.linked_list[0], 1)

    self.linked_list.append("hello")
    self.assertEqual(self.linked_list[0], 1)
    self.assertEqual(self.linked_list[1], "hello")
    self.assertEqual(self.linked_list[self.linked_list.size()-1], "hello")

    # This uses a context manager.
    with self.assertRaises(IndexError):
      self.linked_list[-1]

    with self.assertRaises(IndexError):
      self.linked_list[self.linked_list.size()]



if __name__ == '__main__':
  unittest.main()