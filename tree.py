from node import Node
from stack import LinkedStack


class TreeNode(Node):
    def __init__(self, value=None):
        super().__init__(value)
        self.parent = None
        self.children = []

    def add_child(self, child):
        if not isinstance(child, TreeNode):
            raise TypeError("Child should be of type Tree.")
        child.parent = self
        self.children.append(child)

    def dfs_tree(self):
        yield self.value

        stack = LinkedStack()
        for child in reversed(self.children):
            stack.push(child)

        while not stack.is_empty():
            for value in stack.pull().dfs_tree():
                yield value
