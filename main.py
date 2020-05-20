import sys
from services import get_links, get_link_url, get_link_server
from services.gateways import UrlGateway, DomainGateway
from models.url_model import Url, Domain



class Application:
    def __init__(self, url, suffix):
        self.url = url
        self.suffix = suffix
        self.url_gateway = UrlGateway()
        self.domain_gateway = DomainGateway()


    def create_tables(self):
        self.url_gateway.create_all_tables()

    def crawl(self):
        rawlinks = get_links(self.url)

        for link in rawlinks:
            l = get_link_url(link, self.suffix)
            if l:
                self.url_gateway.add_url(url_name = link, base_url = self.url, url_domain = l)


    def get_domains(self):
        return self.url_gateway.get_unique_domains()

    def store_domains(self):
        new_domains = self.url_gateway.get_unique_domains()
        old_domains = self.domain_gateway.get_all_domains()
        for d in new_domains:
            if d not in old_domains:
                domain_server = get_link_server(d)
                self.domain_gateway.add_domain(domain_name = d, domain_server = domain_server)



def main():
    app = Application(sys.argv[1], sys.argv[2])
    # app.create_tables()
    # app.crawl()
    # app.get_domains()
    # app.store_domains()
    

if __name__ == "__main__":
    main()