from typing import Optional
from models.project import Project


class ProjectService:
    def __init__(self):
        self.projects = []

    def create_project(self, project_id: int, name: str, description: str) -> Optional[Project]:
        if not self.is_valid_project(project_id, name, description):
            return None

        project = Project(project_id, name, description)
        self.projects.append(project)
        return project

    def is_valid_project(self, project_id: int, name: str, description: str) -> bool:
        if self.find_project_by_id(project_id):
            return False

        if self.find_project_by_name(name):
            return False

        if not description:
            return False

        return True

    def find_project_by_id(self, project_id: int) -> Optional[Project]:
        for project in self.projects:
            if project.project_id == project_id:
                return project
        return None

    def find_project_by_name(self, name: str) -> Optional[Project]:
        for project in self.projects:
            if project.name == name:
                return project
        return None
