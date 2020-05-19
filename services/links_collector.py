import re
import requests
from bs4 import BeautifulSoup



def get_links(url):

    def filter_link(link):
        link = rawlink.get('href')
        if link != None and not link.startswith('#'):
            if not link.startswith('http'):
                link = url + link
            return link
        return False

    r = requests.get(url)
    print(r.status_code)
    soup = BeautifulSoup(r.text,features="html.parser")
    links = []
    for rawlink in soup.findAll('a'):
        filtered = filter_link(rawlink)
        if filtered:
            links.append(filtered)

    return links


if __name__ == "__main__":
    pass