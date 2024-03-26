from typing import Optional
from models.project import Project

class ProjectService:
    def __init__(self):
        self.projects = []

    def create_project(self, project_id: int, name: str, description: str) -> Optional[Project]:
        """Создает новый проект с заданными параметрами.

        Args:
            project_id (int): Уникальный идентификатор проекта.
            name (str): Название проекта.
            description (str): Описание проекта.

        Returns:
            Optional[Project]: Созданный проект или None, если не удалось создать проект.
        """
        if not self.is_valid_project(project_id, name, description):
            return None

        project = Project(project_id, name, description)
        self.projects.append(project)
        return project

    def is_valid_project(self, project_id: int, name: str, description: str) -> bool:
        """Проверяет, что проект соответствует бизнес-правилам.

        Args:
            project_id (int): Уникальный идентификатор проекта.
            name (str): Название проекта.
            description (str): Описание проекта.

        Returns:
            bool: True, если проект соответствует бизнес-правилам, иначе False.
        """
        if self.find_project_by_id(project_id):
            return False

        if self.find_project_by_name(name):
            return False

        if not description:
            return False

        return True

    def find_project_by_id(self, project_id: int) -> Optional[Project]:
        """Находит проект по его идентификатору.

        Args:
            project_id (int): Идентификатор проекта.

        Returns:
            Optional[Project]: Найденный проект или None, если проект не найден.
        """
        for project in self.projects:
            if project.project_id == project_id:
                return project
        return None

    def find_project_by_name(self, name: str) -> Optional[Project]:
        """Находит проект по его названию.

        Args:
            name (str): Название проекта.

        Returns:
            Optional[Project]: Найденный проект или None, если проект не найден.
        """
        for project in self.projects:
            if project.name == name:
                return project
        return None
