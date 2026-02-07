def validate_task(fun):
    def wrapper(task, *args, **kwargs):
        if not task or len(task.strip()) == 0:
            raise ValueError("Task description cannot be empty.")
        return fun(task, *args, **kwargs)
    return wrapper

@validate_task
def add_task(task):
    """Add a new task."""
    print(f"Task '{task}' added successfully.")
