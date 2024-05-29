from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from models.base import Base
from typing import List, Dict, Any
from dataclasses import dataclass, field


class Task(Base):
    __tablename__ = 'tasks'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    description = Column(String, nullable=True)
    deadline_id = Column(Integer, ForeignKey('deadlines.id'), nullable=True)
    responsible_id = Column(Integer, ForeignKey('responsibles.id'), nullable=True)
    status_name = Column(String, ForeignKey('statuses.name'), nullable=True)
    project_id = Column(Integer, ForeignKey('projects.project_id'), nullable=False)

    deadline = relationship('Deadline')
    responsible = relationship('Responsible')
    status = relationship('Status')
    project = relationship('Project', back_populates='tasks')
