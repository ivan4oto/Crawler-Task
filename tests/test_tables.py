import unittest
import os
from time import time
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
        current_time = time()

        self.gateway.add_url(url_name = url_name, base_url = base_url, url_domain = url_domain, time = current_time)
        with session_scope(self.gateway.session) as session:
            fetched = session.query(Url).one()

            self.assertEqual(fetched.url_name, url_name)
            self.assertEqual(fetched.base_url, base_url)
            self.assertEqual(fetched.url_domain, url_domain)
            self.assertEqual(fetched.time, current_time)

            self.assertEqual(fetched.visited, False)

    def test_visit_url(self):
        url_name = 'https://github.com/ivan4oto'
        base_url = 'https://hackbulgaria.com/'
        url_domain = 'https://github.com/'
        current_time = time()

        self.gateway.add_url(url_name = url_name, base_url = base_url, url_domain = url_domain, time = current_time)
        self.gateway.visit_url(url_name)

        with session_scope(self.gateway.session) as session:
            fetched = session.query(Url).one()

            self.assertTrue(fetched.visited)        




    def test_visit_n_urls(self):
        url_name = 'https://github.com/ivan4oto'
        base_url = 'https://hackbulgaria.com/'
        url_domain = 'https://github.com/'
        url_one = Url(url_name = url_name, base_url = base_url, url_domain = url_domain)

        url_name_two = 'http://www.start.bg/lenta/horoskopi.html'
        base_url_two = 'https://facebook.com/'
        url_domain_two = 'https://start.bg/'
        url_two = Url(url_name = url_name_two, base_url = base_url_two, url_domain = url_domain_two)

        self.gateway.add_url_list([url_one, url_two])

        self.gateway.visit_n_urls(2)

        with session_scope(self.gateway.session) as session:
            fetched = session.query(Url).all()
            self.assertTrue(fetched[0].visited)
            self.assertTrue(fetched[1].visited)







if __name__ == "__main__":
    unittest.main()