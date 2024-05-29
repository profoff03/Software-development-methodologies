from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from models.base import Base
from typing import List, Dict, Any
from dataclasses import dataclass, field


class Project(Base):
    __tablename__ = 'projects'
    project_id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    description = Column(String, nullable=True)
    tasks = relationship('Task', back_populates='project')
