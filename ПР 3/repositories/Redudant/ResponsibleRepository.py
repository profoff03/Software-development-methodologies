from typing import List, Optional
from models.responsible import Responsible
from repositories.RepositoryBase import RepositoryBase


class ResponsibleRepository(RepositoryBase):
    def __init__(self):
        self.responsibles: List[Responsible] = []

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



    def add_responsible(self, responsible: Responsible):
        """Добавление ответственного"""
        self.responsibles.append(responsible)

    def find_responsible_by_name(self, name: str) -> Optional[Responsible]:
        """Поиск ответственного по имени"""
        for responsible in self.responsibles:
            if responsible.name == name:
                return responsible
        return None

    def get_all_responsibles(self) -> List[Responsible]:
        """Получение всех ответственных"""
        return self.responsibles
