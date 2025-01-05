class TaskNode:
    def __init__(self, task_id, task_name, priority):
        self.task_id = task_id
        self.task_name = task_name
        self.priority = priority
        self.left = None  
        self.right = None  

class TaskBinaryTree:
    def __init__(self):
        self.root = None

    def add_task(self, task_id, task_name, priority):
        new_task = TaskNode(task_id, task_name, priority)
        if not self.root:
            self.root = new_task
        else:
            self._add_task(self.root, new_task)

    def _add_task(self, current, new_task):
        if new_task.priority < current.priority:
            if current.left is None:
                current.left = new_task
            else:
                self._add_task(current.left, new_task)
        else:
            if current.right is None:
                current.right = new_task
            else:
                self._add_task(current.right, new_task)

    def find_task(self, priority):
        return self._find_task(self.root, priority)

    def _find_task(self, current, priority):
        if not current:
            return None
        if current.priority == priority:
            return current
        elif priority < current.priority:
            return self._find_task(current.left, priority)
        else:
            return self._find_task(current.right, priority)

    def inorder_traversal(self):
        tasks = []
        self._inorder_traversal(self.root, tasks)
        return tasks

    def _inorder_traversal(self, current, tasks):
        if current:
            self._inorder_traversal(current.left, tasks)
            tasks.append((current.task_id, current.task_name, current.priority))
            self._inorder_traversal(current.right, tasks)
if __name__ == "__main__":
    tree = TaskBinaryTree()
    tree.add_task(1, "Design Mockups", 3)
    tree.add_task(2, "Write Code", 1)
    tree.add_task(3, "Test Application", 2)

    print("Inorder Traversal (Tasks by Priority):")
    print(tree.inorder_traversal())

    print("\nFind Task with Priority 2:")
    task = tree.find_task(2)
    if task:
        print(f"Found Task: {task.task_id} - {task.task_name}")
    else:
        print("Task not found.")
