from dataclasses import dataclass
from models.deadline import Deadline
from models.responsible import Responsible
from models.status import Status


class Task:
    id: int
    name: str
    description: str
    deadline: Deadline
    responsible: Responsible
    status: Status
