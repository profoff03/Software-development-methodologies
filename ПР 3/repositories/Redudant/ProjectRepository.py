from typing import List, Optional
from models.project import Project
from repositories.RepositoryBase import RepositoryBase


class ProjectRepository(RepositoryBase):
    def __init__(self):
        self.projects: List[Project] = []

    def get_all(self):
        pass

    def get_by_id(self, id):
        pass

    def add(self, item):
        pass

    def delete_by_id(self, id):
        pass

    def update(self, item):
        pass

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
