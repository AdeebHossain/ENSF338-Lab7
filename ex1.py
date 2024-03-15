# Node class
class Node:
    def __init__(self, data, parent=None, left=None, right=None):
        self.parent = parent
        self.data = data
        self.left = left
        self.right = right

    def balance_factor(self):
        left_height = self.left.height() if self.left else 0
        right_height = self.right.height() if self.right else 0
        return left_height - right_height

    def height(self):
        left_height = self.left.height() if self.left else 0
        right_height = self.right.height() if self.right else 0
        return 1 + max(left_height, right_height)

    def is_balanced(self):
        return abs(self.balance_factor()) <= 1


# node insertion
def insert(data, root=None):
    current = root
    parent = None

    while current is not None:
        parent = current
        if data <= current.data:
            current = current.left
        else:
            current = current.right

    newNode = Node(data, parent)
    if root is None:
        root = newNode
    elif data <= parent.data:
        parent.left = newNode
    else:
        parent.right = newNode

    return newNode


# searching algs
def search(data, root):
    current = root
    while current is not None:
        if data == current.data:
            return current
        elif data <= current.data:
            current = current.left
        else:
            current = current.right
    return None
