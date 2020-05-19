from db import Database, base, session_scope
from sqlalchemy.orm import sessionmaker
from settings import DB_NAME
from models.url_model import Url

db = Database(DB_NAME)


class UrlGateway:
    def __init__(self):
        self.db = Database(DB_NAME)
        self.session = sessionmaker(bind=self.db.engine)
        self.base = base

    def create_all_tables(self):
        self.base.metadata.create_all(self.db.engine)

    def add_url(self, url_name, base_url):
        with session_scope(self.session) as session:
            url = Url(url_name = url_name, base_url = base_url)
            session.add(url)

            return url

    def add_url_list(self, url_list, base_url):
        with session_scope(self.session) as session:
            urlobjlist = [Url(url_name = u, base_url = base_url) for u in url_list]
            session.add_all(urlobjlist)

            return urlobjlist