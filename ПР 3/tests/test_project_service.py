import unittest
from models.project import Project
from services.project_service import ProjectService

class TestProjectService(unittest.TestCase):
    def setUp(self):
        self.project_service = ProjectService()

    def test_create_project_valid(self):
        # Проверка создания проекта с корректными данными
        project = self.project_service.create_project(1, "Project 1", "Description 1")
        self.assertIsNotNone(project)
        self.assertEqual(project.project_id, 1)
        self.assertEqual(project.name, "Project 1")
        self.assertEqual(project.description, "Description 1")

    def test_create_project_invalid_duplicate_id(self):
        # Проверка создания проекта с дублирующимся идентификатором
        self.project_service.create_project(1, "Project 1", "Description 1")
        project = self.project_service.create_project(1, "Project 2", "Description 2")
        self.assertIsNone(project)
        self.assertEqual(len(self.project_service.projects), 1)

    def test_create_project_invalid_duplicate_name(self):
        # Проверка создания проекта с дублирующимся названием
        self.project_service.create_project(1, "Project 1", "Description 1")
        project = self.project_service.create_project(2, "Project 1", "Description 2")
        self.assertIsNone(project)
        self.assertEqual(len(self.project_service.projects), 1)

    def test_create_project_invalid_empty_description(self):
        # Проверка создания проекта с пустым описанием
        project = self.project_service.create_project(1, "Project 1", "")
        self.assertIsNone(project)
        self.assertEqual(len(self.project_service.projects), 0)

    def test_find_project_by_id(self):
        # Проверка поиска проекта по идентификатору
        self.project_service.create_project(1, "Project 1", "Description 1")
        found_project = self.project_service.find_project_by_id(1)
        self.assertIsNotNone(found_project)
        self.assertEqual(found_project.project_id, 1)

    def test_find_project_by_name(self):
        # Проверка поиска проекта по названию
        self.project_service.create_project(1, "Project 1", "Description 1")
        found_project = self.project_service.find_project_by_name("Project 1")
        self.assertIsNotNone(found_project)
        self.assertEqual(found_project.name, "Project 1")

if __name__ == "__main__":
    unittest.main()
