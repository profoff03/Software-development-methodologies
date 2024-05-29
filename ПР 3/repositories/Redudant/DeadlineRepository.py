from typing import List, Optional
from models.deadline import Deadline
from repositories.RepositoryBase import RepositoryBase


class DeadlineRepository(RepositoryBase):
    def __init__(self):
        self.deadlines: List[Deadline] = []

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

