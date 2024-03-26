from typing import List, Optional
from models.task import Task


class TaskRepository:
    def __init__(self):
        self.tasks = []

    def add_task(self, task: Task):
        """Добавление задачи"""
        self.tasks.append(task)

    def find_task_by_id(self, task_id: int) -> Optional[Task]:
        """Поиск задачи по идентификатору"""
        for task in self.tasks:
            if task.id == task_id:
                return task
        return None

    def get_all_tasks(self) -> List[Task]:
        """Получение всех задач"""
        return self.tasks
