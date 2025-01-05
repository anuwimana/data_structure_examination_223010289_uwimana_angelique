class TreeNode:
    def __init__(self, key, data):
        self.key = key  
        self.data = data  
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, key, data):
        """Insert a new node into the BST."""
        if self.root is None:
            self.root = TreeNode(key, data)
        else:
            self._insert_recursive(self.root, key, data)

    def _insert_recursive(self, node, key, data):
        if key < node.key:
            if node.left is None:
                node.left = TreeNode(key, data)
            else:
                self._insert_recursive(node.left, key, data)
        elif key > node.key:
            if node.right is None:
                node.right = TreeNode(key, data)
            else:
                self._insert_recursive(node.right, key, data)
        else:
            node.data = data  

    def search(self, key):
        """Search for a node by key."""
        return self._search_recursive(self.root, key)

    def _search_recursive(self, node, key):
        if node is None or node.key == key:
            return node
        if key < node.key:
            return self._search_recursive(node.left, key)
        return self._search_recursive(node.right, key)

    def delete(self, key):
        """Delete a node by key."""
        self.root = self._delete_recursive(self.root, key)

    def _delete_recursive(self, node, key):
        if node is None:
            return None
        if key < node.key:
            node.left = self._delete_recursive(node.left, key)
        elif key > node.key:
            node.right = self._delete_recursive(node.right, key)
        else:
            
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left
            
            successor = self._min_value_node(node.right)
            node.key = successor.key
            node.data = successor.data
            node.right = self._delete_recursive(node.right, successor.key)
        return node

    def _min_value_node(self, node):
        while node.left:
            node = node.left
        return node

    def inorder_traversal(self):
        """Perform in-order traversal to get sorted data."""
        result = []
        self._inorder_recursive(self.root, result)
        return result

    def _inorder_recursive(self, node, result):
        if node is not None:
            self._inorder_recursive(node.left, result)
            result.append((node.key, node.data))
            self._inorder_recursive(node.right, result)

if __name__ == "__main__":
    bst = BinarySearchTree()

    # Insert tasks (key = deadline, data = task description)
    bst.insert(5, "Task with deadline 5 days")
    bst.insert(2, "Task with deadline 2 days")
    bst.insert(8, "Task with deadline 8 days")
    bst.insert(1, "Task with deadline 1 day")
    bst.insert(3, "Task with deadline 3 days")

    search_result = bst.search(3)
    if search_result:
        print(f"Found: {search_result.data}")
    else:
        print("Task not found")

    bst.delete(2)

    print("Tasks sorted by deadlines:")
    for key, data in bst.inorder_traversal():
        print(f"Deadline: {key}, Task: {data}")