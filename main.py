import sys
from time import time
from services import get_link_domain, get_link_server, get_links
from services.gateways import UrlGateway, DomainGateway
from services.controllers_url import UrlController
from models.url_model import Url, Domain
from analytics.plotting import main_plot

class Application:
    def __init__(self, url = '', suffix = ''):
        self.url = url
        self.suffix = suffix
        self.url_gateway = UrlGateway()
        self.url_controller = UrlController()
        self.domain_gateway = DomainGateway()

    def add_start_url(self):
        startingUrl = self.url
        base_url = None
        url_domain = get_link_domain(startingUrl, self.suffix)

        self.url_gateway.add_url(url_name = self.url, base_url = base_url, url_domain = url_domain, time = None)



    def create_tables(self):
        self.url_gateway.create_all_tables()


    def crawler(self):
        tocrawl = self.url_gateway.visit_n_urls(20)
        for i in tocrawl:
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
                print(f'DOMAIN = {d}  SERVER = {domain_server}')
                self.domain_gateway.add_domain(domain_name = d, domain_server = domain_server)



def main():
    command = input('''Please choose an option:
    
    1. Crawl urls from starting url.
    2. Crawl urls and save domains (>>> run option 1 to gather urls first <<<)
    3. Get Servers stats (>>> run option 1 and 2 to gather data first <<<)
    4. Get number of visited links.
    \n''')

    
    if command == '1':
        starting_url = input('Enter starting URL: \n')
        geo_domain = input('Enter geographical domain. Example, ".com", ".net":\n')

        app = Application(url = starting_url, suffix = geo_domain)
        app.create_tables()
        app.add_start_url()
        while True:
            app.crawler()

    if command == '2':
        app = Application()
        app.store_domains()


    if command == '3':
        main_plot()

    if command == '4':
        command = input('''
        Do you wish to get results for:
        
        1. Total number of visited links and time.
        2. Number of visited links for given time.\n        
        ''')

        app = Application()

        if command == '1':
            app.url_controller.get_count_and_time()
        if command == '2':
            timerange = input('\nGet visits for the last: ')
            if timerange.split(' ')[1] == 'minutes':
                print(app.url_controller.get_count_last_minutes(int(timerange.split(' ')[0])))

if __name__ == "__main__":
    main()