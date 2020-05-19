import sys

from services.links_collector import get_links
from services.gateways import UrlGateway



def main():
    url_gateway = UrlGateway()
    url_gateway.create_all_tables()


    


if __name__ == "__main__":
    main()