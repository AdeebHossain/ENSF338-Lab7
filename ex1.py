import random
import time
import matplotlib.pyplot as plt

class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None
    
    def insert(self, key):
        self.root = self._insert(self.root, key)
    
    def _insert(self, node, key):
        if node is None:
            return Node(key)
        if key < node.key:
            node.left = self._insert(node.left, key)
        elif key > node.key:
            node.right = self._insert(node.right, key)
        return node
    
    def search(self, key):
        return self._search(self.root, key)
    
    def _search(self, node, key):
        if node is None or node.key == key:
            return node
        if key < node.key:
            return self._search(node.left, key)
        return self._search(node.right, key)
    
    def measure_balance(self):
        return self._measure_balance(self.root)
    
    def _measure_balance(self, node):
        if node is None:
            return 0
        return abs(self._height(node.left) - self._height(node.right))
    
    def _height(self, node):
        if node is None:
            return 0
        return 1 + max(self._height(node.left), self._height(node.right))

def generate_search_tasks():
    integers = list(range(1, 1001))
    random_tasks = []
    for _ in range(1000):
        random.shuffle(integers)
        random_tasks.append(integers.copy())
    return random_tasks

def measure_performance(tree, tasks):
    avg_search_time = []
    max_balance_values = []
    for task in tasks:
        start_time = time.time()
        for key in task:
            tree.search(key)
        end_time = time.time()
        search_time = end_time - start_time
        avg_search_time.append(search_time / len(task))
        max_balance_values.append(tree.measure_balance())
    return avg_search_time, max_balance_values

def plot_scatter(avg_search_time, max_balance_values):
    plt.scatter(max_balance_values, avg_search_time, alpha=0.5)
    plt.xlabel('Absolute Balance')
    plt.ylabel('Search Time (s)')
    plt.title('Balance vs Search Time')
    plt.show()

if __name__ == "__main__":
    tree = BST()
    tasks = generate_search_tasks()
    avg_search_time, max_balance_values = measure_performance(tree, tasks)
    plot_scatter(avg_search_time, max_balance_values)
