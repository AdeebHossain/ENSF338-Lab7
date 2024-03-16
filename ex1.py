import random
import numpy as np
import timeit
import matplotlib.pyplot as plt


# Node class
class Node:
    def __init__(self, data, parent=None, left=None, right=None):
        self.parent = parent
        self.data = data
        self.left = left
        self.right = right

    def height(self):
        if self is None:
            return 0
        else:
            return 1 + max(Node.height(self.left), Node.height(self.right))


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


# checking if it is a balanced tree
def isBalanced(root):
    if root is None:
        return True
    lh = root.left.height() if root.left else 0
    rh = root.right.height() if root.right else 0
    if abs(lh - rh) <= 1 and isBalanced(root.left) and isBalanced(root.right):
        return True
    return False


# Function to shuffle the list of integers
def shuffle_list(lst):
    random.shuffle(lst)
    return lst


# Generate the list of the first 1000 integers
integer_list = list(range(1, 1001))

# Initialize lists to store performance measures
search_times = []
largest_balance_values = []

# Perform 1000 shuffles and measure performance
for _ in range(1000):
    shuffled_list = shuffle_list(integer_list)
    bst_root = None
    total_balance = 0

    # Construct the BST with the shuffled list
    for num in shuffled_list:
        bst_root = insert(num, bst_root)

    # Measure time for searching each integer in the tree
    search_time = timeit.timeit(
        lambda: search(random.choice(integer_list), bst_root), number=1000
    )
    search_times.append(search_time)

    # Measure largest balance value for this shuffle
    largest_balance_values.append(isBalanced(bst_root))

# Calculate overall average time and largest balance value
overall_average_time = np.mean(search_times)
overall_largest_balance_value = max(
    largest_balance_values
)  ############## Need to figure this out ##############

print("Overall Average Time for Searching:", overall_average_time)
print("Overall Largest Balance Value:", overall_largest_balance_value)

# Store the absolute balance and search time for each task
scatter_data = []

# Perform 1000 shuffles and measure performance
for _ in range(1000):
    shuffled_list = shuffle_list(integer_list)
    bst_root = None

    # Construct the BST with the shuffled list
    for num in shuffled_list:
        bst_root = insert(num, bst_root)

    # Measure time for searching each integer in the tree
    search_time = timeit.timeit(
        lambda: search(random.choice(integer_list), bst_root), number=1000
    )

    # Measure largest balance value for this shuffle
    largest_balance = isBalanced(bst_root)

    # Store the absolute balance and search time
    scatter_data.append((largest_balance, search_time))

# Separate the data for plotting
x_values, y_values = zip(*scatter_data)

# Plot the scatterplot
plt.figure(figsize=(10, 6))
plt.scatter(x_values, y_values, alpha=0.5)
plt.title("Scatterplot of Absolute Balance vs. Search Time")
plt.xlabel("Absolute Balance")
plt.ylabel("Search Time (seconds)")
plt.grid(True)
plt.show()
