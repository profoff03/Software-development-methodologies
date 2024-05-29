from sqlalchemy import Column, Integer, Date
from models.base import Base


class Deadline(Base):
    __tablename__ = 'deadlines'
    id = Column(Integer, primary_key=True, autoincrement=True)
    object_id = Column(Integer)
    start_date = Column(Date)
    end_date = Column(Date)
