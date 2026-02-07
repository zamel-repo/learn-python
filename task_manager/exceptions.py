class TaskNotFoundError(Exception):
    """Exception raised when a task is not found."""
    def __init__(self, task_id: int):
        self.task_id = task_id
        self.message = f"Task with ID {task_id} not found."
        super().__init__(self.message)

    def remove_task(task_id: int, tasks: list):
        # task = find_task_by_id(task_id)
        if not tasks:
            raise TaskNotFoundError(task_id)
    pass