class Task:
    def __init__(self, task_id, task_name, priority):
        """
        Represents a task in the SaaS application.
        :param task_id: Unique identifier for the task.
        :param task_name: Name of the task.
        :param priority: Priority of the task (lower value = higher priority).
        """
        self.task_id = task_id
        self.task_name = task_name
        self.priority = priority

    def __repr__(self):
        return f"Task(ID: {self.task_id}, Name: {self.task_name}, Priority: {self.priority})"


def selection_sort(tasks):
    """
    Sorts a list of tasks based on priority using Selection Sort.
    :param tasks: List of Task objects.
    :return: Sorted list of Task objects.
    """
    n = len(tasks)
    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            if tasks[j].priority < tasks[min_index].priority:
                min_index = j
        tasks[i], tasks[min_index] = tasks[min_index], tasks[i]
    return tasks
if __name__ == "__main__":
    tasks = [
        Task(1, "Finalize Design", 3),
        Task(2, "Write Documentation", 5),
        Task(3, "Develop Backend", 1),
        Task(4, "Test Application", 4),
        Task(5, "Create Wireframes", 2),
    ]

    print("Before Sorting:")
    print(tasks)

    sorted_tasks = selection_sort(tasks)

    print("\nAfter Sorting by Priority:")
    print(sorted_tasks)
