from models.deadline import Deadline
from models.responsible import Responsible
from models.status import Status


class Task:
    def __init__(self, id, name, description, task_deadline: Deadline, task_responsible: Responsible,
                 task_status: Status):
        self.id = id
        self.name = name
        self.description = description
        self.deadline = task_deadline
        self.responsible = task_responsible
        self.status = task_status

    def __eq__(self, other):
        if not isinstance(other, Task):
            return False
        return (self.id, self.name, self.description, self.deadline, self.responsible, self.status) == \
            (other.id, other.name, other.description, other.deadline, other.responsible, other.status)
