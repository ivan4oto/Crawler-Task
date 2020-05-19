import sys
from services import get_links, get_link_url
from services.gateways import UrlGateway



def main():
    url_gateway = UrlGateway()
    url_gateway.create_all_tables()
    print(get_links(sys.argv[1]))
    

if __name__ == "__main__":
    main()