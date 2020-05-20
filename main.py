import sys
from services import get_links, get_link_url, get_link_server
from services.gateways import UrlGateway
from models.url_model import Url




class Application:
    def __init__(self, url, suffix):
        self.url = url
        self.suffix = suffix
        self.gateway = UrlGateway()

    def create_tables(self):
        self.gateway.create_all_tables()

    def crawl(self):
        rawlinks = get_links(self.url)

        # results = []
        for link in rawlinks:
            l = get_link_url(link, self.suffix)
            if l:
                l_server = get_link_server(l)
                self.gateway.add_url(url_name = link, base_url = self.url, url_server = l_server, url_domain = l)














def main():
    app = Application(sys.argv[1], sys.argv[2])
    app.crawl()
    

if __name__ == "__main__":
    main()