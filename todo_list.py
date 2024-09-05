class ToDoList:
    def __init__(self):
        self._tasks = []

    # Getter for tasks
    @property
    def tasks(self):
        return self._tasks

    # Add a task
    def add_task(self, task):
        if task:
            self._tasks.append(task)
        else:
            raise ValueError("Task cannot be empty")

    # Remove a task by its index
    def remove_task(self, index):
        if 0 <= index < len(self._tasks):
            del self._tasks[index]
        else:
            raise IndexError("Task index out of range")