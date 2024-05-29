from typing import List, Optional, Type
from sqlalchemy.orm import Session

from models import Task
from models.task import Task
from repositories.RepositoryBase import RepositoryBase


class TaskRepository(RepositoryBase):
    def __init__(self, session: Session):
        self.session = session

    def get_all(self) -> list[Type[Task]]:
        return self.session.query(Task).all()

    def get_by_id(self, id: int) -> Optional[Task]:
        return self.session.query(Task).get(id)

    def add(self, item: Task) -> None:
        self.session.add(item)
        self.session.commit()

    def delete_by_id(self, id: int) -> None:
        task = self.get_by_id(id)
        if task:
            self.session.delete(task)
            self.session.commit()

    def update(self, item: Task) -> None:
        self.session.merge(item)
        self.session.commit()
