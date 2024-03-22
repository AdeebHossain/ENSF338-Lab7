# Node class
class Node:
    def __init__(self, data, parent=None, left=None, right=None):
        self.parent = parent
        self.data = data
        self.left = left
        self.right = right
        self.balance = 0  # Added balance factor to the Node


# is balanced
def is_balanced(root):
    if not root:
        return True, 0

    left, right = is_balanced(root.left), is_balanced(root.right)
    balanced = left[0] and right[0] and abs(left[1] - right[1]) <= 1
    height = 1 + max(left[1], right[1])
    balanced_factor = abs(left[1] - right[1])
    return (balanced, height, balanced_factor)


# node insertion
def insert(data, root=None):
    current = root
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
    if root is None:
        root = newNode
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


# Test Case 1: Adding a node results in case 1
def test_case_1():
    root = Node(10)
    insert(5, root)
    insert(15, root)
    insert(3, root)
    insert(7, root)
    insert(12, root)
    insert(17, root)
    insert(2, root)  # Should result in Case #1: Pivot not detected


# Test Case 2: Adding a node results in case 2
def test_case_2():
    root = Node(10)
    insert(5, root)
    insert(15, root)
    insert(3, root)
    insert(7, root)
    insert(12, root)
    insert(17, root)
    insert(
        8, root
    )  # Should result in Case #2: A pivot exists, and a node was added to the shorter subtree


# Test Case 3: Adding a node results in case 3
def test_case_3():
    root = Node(10)
    insert(5, root)
    insert(15, root)
    insert(3, root)
    insert(7, root)
    insert(12, root)
    insert(17, root)
    insert(6, root)  # Should print "Case 3 not supported"


# Test Case 4: Testing balance factor update and pivot detection
def test_balance_and_pivot():
    root = Node(10)
    insert(5, root)
    insert(15, root)
    insert(3, root)
    insert(7, root)
    insert(12, root)
    insert(17, root)
    insert(2, root)  # Should result in Case #1: Pivot not detected
    insert(
        8, root
    )  # Should result in Case #2: A pivot exists, and a node was added to the shorter subtree


# Running the tests
if __name__ == "__main__":
    test_case_1()
    test_case_2()
    test_case_3()
    test_balance_and_pivot()
