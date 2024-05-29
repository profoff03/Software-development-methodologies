from typing import List, Optional
from models.status import Status
from repositories.RepositoryBase import RepositoryBase


class StatusRepository(RepositoryBase):
    def __init__(self):
        self.tasks: List[Status] = []

    def get_all(self):
        return self.tasks

    def get_by_id(self, id):
        pass

    def add(self, item):
        pass

    def delete_by_id(self, id):
        pass

    def update(self, item):
        pass