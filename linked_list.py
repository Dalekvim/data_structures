class Node:

  '''Creates a Node that contains a head and a next element.'''
  def __init__(self, data=None):
    self.data = data
    self.next = None

class LinkedList:

  '''Creates a Singly Linked List.'''
  def __init__(self, _list=[]):
    '''Initilises the head as an empty Node.'''
    self.head = Node()
    for i in _list:
      self.append(i)

  def __repr__(self):
    '''Displays the list representation of the linked list.'''
    return str(self.as_list())

  def last(self, func=None, /, last=None):
    '''This returns the last Node.'''
    current = self.head

    while current.next != last:
      current = current.next

      if func:
        '''This is used so it allow to allow the data to be read.'''
        func(current.data)
    
    return current

  def __getitem__(self, index):
    return self.get_node(index).data

  def get_node(self, index):
    if index >= self.size() or index < 0:
      raise IndexError('Index out of range.')
    
    current = self.head

    for i in range(index + 1):
      current = current.next
    
    return current

  def as_list(self):
    '''Creates a list of all the elements from the linked list.'''
    linked_list = []
    
    self.last(linked_list.append)
    
    return linked_list

  def size(self):
    '''Converts linked list to list and calculates it's length.'''
    return len(self.as_list())

  def append(self, data):
    '''This adds an item to the end of a linked list.'''
    self.last().next = Node(data)
  
  def pop(self):
    '''This deletes the last Node in the list and returns it's data.'''
    last = self.last()

    self.last(last=last).next = None

    return last.data

  def add(self, data, index=0):
    if index:
      current = self.get_node(index)
      current.next = self.get_node(index)
      current.data = data

    else:
      pass


linked_list = LinkedList()
linked_list.append("hello")
linked_list.add(1, 0)
print(linked_list.as_list())