from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from contextlib import contextmanager
from settings import DB_NAME


base = declarative_base()


class Database:
    def __init__(self):
        self.engine = create_engine(f"sqlite:///{DB_NAME}")
        self.session = sessionmaker(bind = self.engine)


        
@contextmanager
def session_scope(session_maker):
    """Provide a transactional scope around a series of operations."""
    session = session_maker
    try:
        yield session
        session.commit()
    except Exception:
        session.rollback()
        raise
    finally:
        session.close()