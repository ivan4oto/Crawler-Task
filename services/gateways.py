from db import Database, base, session_scope
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import IntegrityError

from settings import DB_NAME
from models.url_model import Url, Domain
from sqlalchemy import func

db = Database(DB_NAME)


class UrlGateway:
    def __init__(self):
        self.db = Database(DB_NAME)
        self.session = sessionmaker(bind=self.db.engine)
        self.base = base

    def create_all_tables(self):
        self.base.metadata.create_all(self.db.engine)

    def add_url(self, url_name, base_url, url_domain):
        with session_scope(self.session) as session:
            url = Url(url_name = url_name, base_url = base_url, url_domain = url_domain)
            session.add(url)

            return url

    def add_url_list(self, url_list):
        with session_scope(self.session) as session:
            session.add_all(url_list)

            

    def get_all_urls(self):
        with session_scope(self.session) as session:
            urls = session.query(Url).all()
            return urls

    def get_unique_domains(self):
        with session_scope(self.session) as session:
            results = []
            for u in session.query(Url.url_domain).distinct():
                results.append(u.url_domain)

            return results

    def visit_url(self, url_name):
        with session_scope(self.session) as session:
            url = session.query(Url).filter(Url.url_name == url_name).all()
            if len(url) > 1:
                return False

            url[0].visited = True
            session.add(url[0])

            return True

    def visit_check(self, url_name):
        with session_scope(self.session) as session:
            url = session.query(Url).filter(Url.url_name == url_name).one()

            return url.visited


class DomainGateway:
    def __init__(self):
        self.db = Database(DB_NAME)
        self.session = sessionmaker(bind=self.db.engine)
        self.base = base

    
    def add_domain(self, domain_name, domain_server):
        with session_scope(self.session) as session:
            domain = Domain(domain_name = domain_name, domain_server = domain_server)
            session.add(domain)

            return domain

    def get_all_domains(self):
        with session_scope(self.session) as session:
            results = []
            for d in session.query(Domain.domain_name).all():
                results.append(d.domain_name)

            return results

    def count_servers(self):
        with session_scope(self.session) as session:
            q = (session.query(Domain.domain_server, func.count(Domain.id).label("#Servers"))
                .group_by(Domain.domain_server)
                ).all()

            return q