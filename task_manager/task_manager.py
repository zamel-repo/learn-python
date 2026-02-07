import argparse
from task import Task
from validations import add_task
from exceptions import TaskNotFoundError

def main():
    args = parse_arguments()
    if args.add:
        add_task(args.add)
    elif args.list:
        list_tasks()
    elif args.remove:
        remove_task(args.remove)
    elif args.complete:
        complete_task(args.complete)
    else:
        print("Invalid option. Use --help for guidance.")
        
if __name__ == "__main__":
    main()
    