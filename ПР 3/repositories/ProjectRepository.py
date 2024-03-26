from typing import List, Optional
from models.project import Project


class ProjectRepository:
    def __init__(self):
        self.projects = []

    def add_project(self, project: Project):
        """Добавление проекта"""
        self.projects.append(project)

    def find_project_by_id(self, project_id: int) -> Optional[Project]:
        """Поиск проекта по идентификатору"""
        for project in self.projects:
            if project.project_id == project_id:
                return project
        return None

    def find_project_by_name(self, name: str) -> Optional[Project]:
        """Поиск проекта по названию"""
        for project in self.projects:
            if project.name == name:
                return project
        return None

    def get_all_projects(self) -> List[Project]:
        """Получение всех проектов"""
        return self.projects
