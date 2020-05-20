from db import base
from sqlalchemy import Column, Integer, String

class Url(base):
    __tablename__ = 'urls'

    id = Column(Integer, primary_key = True)
    url_name = Column(String)
    base_url = Column(String)
    url_domain = Column(String)

    def __str__(self):
        return f'''ID = {self.id} Url = {self.url_name} base_link = {self.base_url} domain = {self.url_domain}'''

    def __repr__(self):
        return str(self)


class Domain(base):
    __tablename__ = 'domains'

    id = Column(Integer, primary_key = True)
    domain_name = Column(String)
    domain_server = Column(String)

    def __str__(self):
        return f"domain name = {self.domain_name}  domain server = {self.domain_server}"

    def __repr__(self):
        return str(self)
