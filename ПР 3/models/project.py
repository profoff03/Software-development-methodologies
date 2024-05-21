from typing import List
from models.task import Task

class Project:
    def __init__(self, project_id, name, description):
        self.project_id = project_id
        self.name = name
        self.description = description
        self.tasks = List[Task]

    def add_task(self, task):
        if isinstance(task, Task):
            self.tasks.append(task)
        else:
            raise ValueError("Only instances of Task class can be added to the project")

