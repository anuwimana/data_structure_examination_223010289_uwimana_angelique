class TreeNode:
    def __init__(self, id, name, data=None):
        """
        Represents a single node in the tree.
        :param id: Unique identifier for the node.
        :param name: Name of the node (e.g., Project/Task name).
        :param data: Additional data (e.g., freelancer details, deadlines).
        """
        self.id = id
        self.name = name
        self.data = data  
        self.children = []  

    def add_child(self, child_node):
        """
        Adds a child node to the current node.
        :param child_node: Instance of TreeNode to be added.
        """
        self.children.append(child_node)

    def find_node(self, id):
        """
        Recursively finds a node with the given id.
        :param id: Unique identifier of the node to find.
        :return: TreeNode if found, None otherwise.
        """
        if self.id == id:
            return self
        for child in self.children:
            result = child.find_node(id)
            if result:
                return result
        return None

    def display_tree(self, level=0):
        """
        Recursively prints the tree structure.
        :param level: Depth of the current node (used for indentation).
        """
        print(" " * (level * 4) + f"{self.name} (ID: {self.id})")
        for child in self.children:
            child.display_tree(level + 1)
if __name__ == "__main__":
    project = TreeNode(1, "Website Redesign", {"deadline": "2025-01-31", "freelancer": None})
    task1 = TreeNode(2, "Design Mockups", {"deadline": "2025-01-15", "freelancer": "Alice"})
    task2 = TreeNode(3, "Develop Backend", {"deadline": "2025-01-20", "freelancer": "Bob"})
    project.add_child(task1)
    project.add_child(task2)
    subtask1 = TreeNode(4, "Create Wireframes", {"deadline": "2025-01-10", "freelancer": "Alice"})
    subtask2 = TreeNode(5, "Finalize Design", {"deadline": "2025-01-14", "freelancer": "Alice"})
    task1.add_child(subtask1)
    task1.add_child(subtask2)
    print("Project Hierarchy:")
    project.display_tree()
    node_id = 4
    found_node = project.find_node(node_id)
    if found_node:
        print(f"\nFound Node: {found_node.name} (ID: {found_node.id}, Data: {found_node.data})")
    else:
        print(f"\nNode with ID {node_id} not found.")