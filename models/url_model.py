from db import base
from sqlalchemy import Column, Integer, String, Boolean, Float

class Url(base):
    __tablename__ = 'urls'

    id = Column(Integer, primary_key=True)
    url_name = Column(String)
    base_url = Column(String)
    url_domain = Column(String)
    visited = Column(Integer, default=0, nullable=False)
    time = Column(Float, nullable = True)

    def __str__(self):
        return f'Url = {self.url_name}, matternalURL = {self.base_url}'

    def __repr__(self):
        return str(self)


class Domain(base):
    __tablename__ = 'domains'

    id = Column(Integer, primary_key=True)
    domain_name = Column(String)
    domain_server = Column(String)

    def __str__(self):
        return f"domain name = {self.domain_name}  domain server = {self.domain_server}"

    def __repr__(self):
        return str(self)
