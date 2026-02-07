import argparse

def parse_arguments():
    parser = argparse.ArgumentParser(
        description="Task Manager Command Line Interface"
    )
    # Add argument for adding a new task
    parser.add_argument(
        "--add",
        type=str,
        help="Add a new task with the given description",
        required=True
    )
    # Add argument for listing all tasks
    parser.add_argument(
        "--list",
        action="store_true",
        help="List all tasks"
    )
    # Add argument for marking a task as completed
    parser.add_argument(
        "--complete",
        type=int,
        help="Mark the task with the given ID as completed"
    )
    # Add argument for removing a task
    parser.add_argument(
        "--remove",
        type=int,
        help="Remove the task with the given ID"
    )
    
    return parser.parse_args()

