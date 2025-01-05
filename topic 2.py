import heapq
from collections import deque

class TaskManager:
    def __init__(self):
        self.task_queue = deque()  
        self.priority_heap = []   

    def add_task_to_queue(self, task):
        """Add a task to the queue."""
        self.task_queue.append(task)

    def process_task_from_queue(self):
        """Process the next task in the queue."""
        if not self.task_queue:
            return "Queue is empty"
        return self.task_queue.popleft()

    def add_task_to_heap(self, priority, task):
        """Add a task with priority to the heap."""
        heapq.heappush(self.priority_heap, (priority, task))

    def process_task_from_heap(self):
        """Process the highest-priority task from the heap."""
        if not self.priority_heap:
            return "Heap is empty"
        return heapq.heappop(self.priority_heap)
    def get_next_task(self):
        """
        Retrieve the next task to process.
        Priority tasks (from heap) are processed first.
        If no priority tasks exist, process the queue.
        """
        if self.priority_heap:
            priority, task = heapq.heappop(self.priority_heap)
            return f"Processing priority task: {task} (Priority: {priority})"
        elif self.task_queue:
            return f"Processing queued task: {self.task_queue.popleft()}"
        else:
            return "No tasks to process"

if __name__ == "__main__":
    manager = TaskManager()

    manager.add_task_to_queue("Task A")
    manager.add_task_to_queue("Task B")

    # Add priority tasks to heap
    manager.add_task_to_heap(1, "Urgent Task 1")
    manager.add_task_to_heap(3, "Task with Low Priority")
    manager.add_task_to_heap(2, "Urgent Task 2")
    print(manager.get_next_task())  
    print(manager.get_next_task())  
    print(manager.get_next_task())  
    print(manager.get_next_task())  
    print(manager.get_next_task())  
    print(manager.get_next_task())  

