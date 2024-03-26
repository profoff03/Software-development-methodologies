import unittest
from models.project import Project
from services.project_service import ProjectService


class TestProjectService(unittest.TestCase):
    def setUp(self):
        self.project_service = ProjectService()
        self.project = Project(1, "Project 1", "Description 1")

    def test_create_project_success(self):
        """Проверяет успешное создание проекта."""
        result = self.project_service.create_project(1, "Project 1", "Description 1")
        self.assertIsNotNone(result)
        self.assertEqual(result.name, "Project 1")

    def test_create_project_duplicate_id(self):
        """Проверяет, что нельзя создать проект с уже существующим идентификатором."""
        self.project_service.create_project(1, "Project 1", "Description 1")
        result = self.project_service.create_project(1, "Project 2", "Description 2")
        self.assertIsNone(result)

    def test_create_project_duplicate_name(self):
        """Проверяет, что нельзя создать проект с уже существующим названием."""
        self.project_service.create_project(1, "Project 1", "Description 1")
        result = self.project_service.create_project(2, "Project 1", "Description 2")
        self.assertIsNone(result)

    def test_create_project_missing_fields(self):
        """Проверяет, что нельзя создать проект без обязательных полей."""
        result = self.project_service.create_project(2, "", "")
        self.assertIsNone(result)

if __name__ == "__main__":
    unittest.main()
