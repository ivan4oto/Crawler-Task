import unittest
from services import get_link_server, get_link_domain


class TestGetLinkServer(unittest.TestCase):

    #might change if google decides to change server name
    def test_get_link_server_returns_correct(self):
        result = get_link_server('https://www.google.com/')

        self.assertEqual(result, 'gws')

    def test_get_link_server_returns_false_if_link_invalid(self):
        result = get_link_server('trolololol')

        self.assertFalse(result)


class TestLinksDisassembler(unittest.TestCase):
    def test_func_returns_full_domain_from_path_link(self):
        result = get_link_domain('https://requests.readthedocs.io/en/master/user/quickstart/#redirection-and-history', 'io')
        expected = 'https://requests.readthedocs.io/'

        self.assertEqual(result, expected)


if __name__ == "__main__":
    unittest.main()