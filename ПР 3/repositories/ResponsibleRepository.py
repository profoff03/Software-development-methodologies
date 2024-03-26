from typing import List, Optional
from models.responsible import Responsible


class ResponsibleRepository:
    def __init__(self):
        self.responsibles = []

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
