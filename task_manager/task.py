class Task:
    """
    Class to represent a task in the task manager.

    Atributes:
        id (int): Unique identifier for the task.
        description (str): Description of the task.
        completed (bool): Status of the task, whether it is completed or not.
    """

    def __init__(self, id, description):
        """
        Docstring for __init__
        
        :param self: Description
        :param id: Description
        :param description: Description
        """

        self.id = id
        self.description = description
        self.completed = False

