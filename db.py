from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from contextlib import contextmanager


base = declarative_base()


class Database:
    def __init__(self, db_name):
        self.engine = create_engine(f"sqlite:///{db_name}")
        self.session = sessionmaker(bind = self.engine)



@contextmanager
def session_scope(session_maker):
    """Provide a transactional scope around a series of operations."""
    session = session_maker(expire_on_commit = False)
    try:
        yield session
        session.commit()
    except Exception:
        session.rollback()
        raise
    finally:
        session.close()