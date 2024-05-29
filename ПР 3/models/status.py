from sqlalchemy import Column, String
from models.base import Base


class Status(Base):
    __tablename__ = 'statuses'
    name = Column(String, primary_key=True)
