import random
import timeit
import matplotlib.pyplot as plt


# Node class
class Node:
    def __init__(self, data, parent=None, left=None, right=None):
        self.parent = parent
        self.data = data
        self.left = left
        self.right = right


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


# Generate the list of the first 1000 integers
integers_list = list(range(1, 1002))

# Shuffle the list 1000 times to create 1000 different tasks
tasks = [random.sample(integers_list, len(integers_list)) for _ in range(1000)]

# Initialize lists to store balance and search time data
balance_values = []
search_times = []

# For each task, create a binary search tree, measure performance, and balance
for task in tasks:
    # Create a new BST for each task
    root = None
    for num in task:
        root = insert(num, root)

    # Measure search time for each integer in the tree
    search_task_time = (
        timeit.timeit(lambda: search(random.choice(integers_list), root), number=100)
        / 100
    )

    # Check balance and get the largest absolute balance value
    is_tree_balanced = is_balanced(root)[2]
    balance_values.append(is_tree_balanced)
    search_times.append(search_task_time)

# Generate a scatterplot
plt.scatter(balance_values, search_times, alpha=0.5)
plt.title("Balance vs Search Time")
plt.xlabel("Absolute Balance Value")
plt.ylabel("Search Time (seconds)")
plt.show()
