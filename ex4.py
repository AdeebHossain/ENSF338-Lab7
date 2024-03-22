# Node class
class Node:
    def __init__(self, data, parent=None, left=None, right=None):
        self.parent = parent
        self.data = data
        self.left = left
        self.right = right
        self.balance = 0  # Added balance factor to the Node


# AVL Tree class
class AVLTree:
    def __init__(self):
        self.root = None

    # Internal left rotation method
    def _left_rotate(self, node):
        # Implement left rotation logic here
        pass

    # Internal right rotation method
    def _right_rotate(self, node):
        # Implement right rotation logic here
        pass

    # Node insertion
    def insert(self, data):
        current = self.root
        parent = None
        pivot = None  # Variable to store the pivot node

        while current is not None:
            parent = current
            if data <= current.data:
                current.balance += 1  # Increment balance when going left
                if current.balance > 1:
                    pivot = current  # Update pivot when balance > 1
                current = current.left
            else:
                current.balance -= 1  # Decrement balance when going right
                if current.balance < -1:
                    pivot = current  # Update pivot when balance < -1
                current = current.right

        newNode = Node(data, parent)
        if self.root is None:
            self.root = newNode
        elif data <= parent.data:
            parent.left = newNode
        else:
            parent.right = newNode

        # Check if pivot exists
        if pivot is None:
            print("Case #1: Pivot not detected")
        else:
            # Check if the new node is inserted into the shorter subtree
            if (pivot.balance > 0 and data <= pivot.data) or (
                pivot.balance < 0 and data > pivot.data
            ):
                print(
                    "Case #2: A pivot exists, and a node was added to the shorter subtree"
                )
            else:
                # Check if the new node is inserted into the inner subtree
                if pivot.parent is not None and (
                    (data > pivot.data and data <= pivot.parent.data)
                    or (data <= pivot.data and data > pivot.parent.data)
                ):
                    print("Case #3b: not supported")  # Handle case 3b
                else:
                    print("Case #3a: adding a node to an outside subtree")

        # Handle case 3a
        if pivot is not None and pivot.balance != 0:
            print("Case #3a: adding a node to an outside subtree")

        return newNode


# Test cases
if __name__ == "__main__":
    # Test Case 1: Adding a node resulting in case 3a
    tree = AVLTree()
    tree.insert(10)
    tree.insert(5)
    tree.insert(15)
    tree.insert(3)
    tree.insert(7)
    tree.insert(12)
    tree.insert(17)
    tree.insert(2)  # Should result in Case #3a: adding a node to an outside subtree

    # Test Case 2: Adding a node resulting in case 3b
    tree = AVLTree()
    tree.insert(10)
    tree.insert(5)
    tree.insert(15)
    tree.insert(3)
    tree.insert(7)
    tree.insert(12)
    tree.insert(17)
    tree.insert(11)  # Should print "Case 3b not supported"
