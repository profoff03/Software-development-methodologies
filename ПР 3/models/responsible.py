from sqlalchemy import Column, Integer, String
from models.base import Base


class Responsible(Base):
    __tablename__ = 'responsibles'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)
    contact_info = Column(String)
