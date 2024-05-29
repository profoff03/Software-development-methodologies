from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from models import Base, Task
from repositories.TableRepository import TableRepository
from repositories.XMLRepository import XMLRepository

DATABASE_URL = "sqlite:///database.db"
XML_FILE = 'tasks.xml'
ROOT_ELEMENT_NAME = 'task'


def get_repository(repo_type):
    if repo_type == 'sql':
        engine = create_engine(DATABASE_URL)
        SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
        session = SessionLocal()
        return TableRepository(session, Task)
    elif repo_type == 'xml':
        return XMLRepository(XML_FILE, ROOT_ELEMENT_NAME)
    else:
        raise ValueError(f"Unknown repository type: {repo_type}")
