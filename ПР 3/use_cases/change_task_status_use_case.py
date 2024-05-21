from models.task import Task
from typing import List
from models.status import Status
from services.task_service import TaskService

class ChangeTaskStatusUseCase:
    def __init__(self, task_service: TaskService):
        self.task_service = task_service

    def execute(self, tasks: List[Task], task_id: int, new_status: Status) -> bool:
        """Изменяет статус задачи."""
        return self.task_service.update_task_status(tasks, task_id, new_status)
