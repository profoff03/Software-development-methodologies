from models.task import Task
from models.status import Status

class TaskService:
    VALID_STATUSES = {"В процессе", "Завершена", "Готова к выполнению"}

    def change_task_status(self, task: Task, new_status: Status) -> bool:
        if new_status.name not in self.VALID_STATUSES:
            return False
        task.status = new_status
        return True

    def complete_task(self, task: Task) -> bool:
        """Завершение задачи"""
        if task.status.name != "В процессе":
            return False
        task.status = Status("Завершена")
        return True
