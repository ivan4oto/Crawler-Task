import sys
from services import get_link_domain, get_link_server, get_links
from services.gateways import UrlGateway, DomainGateway
from models.url_model import Url, Domain


class Application:
    def __init__(self, url, suffix):
        self.url = url
        self.suffix = suffix
        self.url_gateway = UrlGateway()
        self.domain_gateway = DomainGateway()

    def add_start_url(self):
        startingUrl = self.url
        base_url = None
        url_domain = get_link_domain(startingUrl, self.suffix)

        self.url_gateway.add_url(url_name = self.url, base_url = base_url, url_domain = url_domain)



    def create_tables(self):
        self.url_gateway.create_all_tables()


    def crawler(self):
        tocrawl = self.url_gateway.get_all_urls()
        for i in tocrawl:
            if i.visited == 0 and self.url_gateway.visit_url(url_name = i.url_name):
                self.url_gateway.visit_url(url_name = i.url_name)
                result = self.crawl(i.url_name)
                if result:
                    self.url_gateway.add_url_list(url_list = result)
                else:
                    pass

    def crawl(self, url):
        rawlinks = get_links(url)
        if not rawlinks:
            return False

        url_list = []
        for link in rawlinks:
            l = get_link_domain(link, self.suffix)
            if l:
                u = Url(url_name = link, base_url = url, url_domain = l)
                print(u)
                url_list.append(u)

        return url_list


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
    app.create_tables()
    app.add_start_url()
    app.crawler()

if __name__ == "__main__":
    main()