import unittest
from models.task import Task
from models.deadline import Deadline
from models.responsible import Responsible
from models.status import Status
from services.task_service import TaskService


class TestTaskService(unittest.TestCase):
    def setUp(self):
        self.task_service = TaskService()
        self.deadline = Deadline("2024-02-28", "2024-03-15")
        self.responsible = Responsible("John Doe", "john@example.com")
        self.status = Status("В процессе")
        self.task = Task(1, "Task 1", "Description 1", self.deadline, self.responsible, self.status)

    def test_change_task_status_valid(self):
        result = self.task_service.change_task_status(self.task, Status("Готова к выполнению"))
        self.assertTrue(result)
        self.assertEqual(self.task.status, Status("Готова к выполнению"))

    def test_change_task_status_invalid(self):
        result = self.task_service.change_task_status(self.task, Status("Invalid Status"))
        self.assertFalse(result)
        self.assertEqual(self.task.status, self.status)

    def test_complete_task_success(self):
        result = self.task_service.complete_task(self.task)
        self.assertTrue(result)
        self.assertEqual(self.task.status, Status("Завершена"))

    def test_complete_task_invalid_status(self):
        self.task.status = Status("Готова к выполнению")
        result = self.task_service.complete_task(self.task)
        self.assertFalse(result)
        self.assertEqual(self.task.status, Status("Готова к выполнению"))

if __name__ == "__main__":
    unittest.main()
