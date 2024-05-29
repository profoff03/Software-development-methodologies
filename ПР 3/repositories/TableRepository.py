from sqlalchemy.orm import Session
from repositories.RepositoryBase import RepositoryBase
from models.base import Base

class TableRepository(RepositoryBase):

    def __init__(self, session: Session, model: Base):
        self.session = session
        self.model = model

    def get_all(self):
        return self.session.query(self.model).all()

    def get_by_id(self, id):
        return self.session.query(self.model).filter(self.model.id == id).first()

    def add(self, item):
        self.session.add(item)
        self.session.commit()

    def delete_by_id(self, id):
        item = self.get_by_id(id)
        if item:
            self.session.delete(item)
            self.session.commit()

    def update(self, item):
        self.session.merge(item)
        self.session.commit()
