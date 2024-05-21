from typing import List, Optional
from models.task import Task
from models.status import Status


class TaskService:
    VALID_STATUSES = {"В процессе", "Готова к выполнению", "Завершена"}

    def find_task_by_id(self, tasks: List[Task], task_id: int) -> Optional[Task]:
        """Поиск задачи по её ID."""
        for task in tasks:
            if task.id == task_id:
                return task
        return None

    def change_task_status(self, tasks: List[Task], task_id: int, new_status: Status) -> bool:
        """Изменение статуса задачи."""
        task = self.find_task_by_id(tasks, task_id)
        if not task:
            return False

        if new_status.name not in self.VALID_STATUSES:
            return False

        task.status = new_status
        return True

    def complete_task(self, tasks: List[Task], task_id: int) -> bool:
        """Завершение задачи."""
        task = self.find_task_by_id(tasks, task_id)
        if not task:
            return False

        if task.status.name != "В процессе":
            return False

        task.status = Status("Завершена")
        return True

    def update_task_status(self, tasks: List[Task], task_id: int, new_status: Status) -> bool:
        """Метод для обновления статуса задачи."""
        return self.change_task_status(tasks, task_id, new_status)
