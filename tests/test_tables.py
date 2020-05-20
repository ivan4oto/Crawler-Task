import unittest
import os
from sqlalchemy.orm import sessionmaker
from db import Database, session_scope, base
from settings import TEST_DB
from services.gateways import UrlGateway
from models.url_model import Url


class UrlTestGate(UrlGateway):
    def __init__(self):
        self.db = Database(TEST_DB)
        self.session = sessionmaker(bind=self.db.engine)
        self.base = base

class TestUrl(unittest.TestCase):
    def setUp(self):
        self.gateway = UrlTestGate()
        self.gateway.create_all_tables()

    def tearDown(self):
        os.remove(TEST_DB)



    def test_add_url(self):
        url_name = 'https://github.com/ivan4oto'
        base_url = 'https://hackbulgaria.com/'
        url_domain = 'https://github.com/'

        self.gateway.add_url(url_name = url_name, base_url = base_url, url_domain = url_domain)
        with session_scope(self.gateway.session) as session:
            fetched = session.query(Url).one()

            self.assertEqual(fetched.url_name, url_name)
            self.assertEqual(fetched.base_url, base_url)
            self.assertEqual(fetched.url_domain, url_domain)



if __name__ == "__main__":
    unittest.main()