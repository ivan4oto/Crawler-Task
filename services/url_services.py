import re
import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse




def get_links(url):

    def filter_link(link):
        link = rawlink.get('href')
        if link != None and not link.startswith('#'):
            if not link.startswith('http'):
                link = url + link
            return link
        return False
    try:
        r = requests.get(url)
        print(r.status_code)
        soup = BeautifulSoup(r.text,features="html.parser")
        links = []
        for rawlink in soup.findAll('a'):
            filtered = filter_link(rawlink)
            if filtered:
                links.append(filtered)
    except Exception:
        return False

    return links



def get_link_server(url):
    try:
        r = requests.get(url)
        return r.headers['Server']
        
    except Exception:
        return None



def get_link_domain(link, suffix):
    o = urlparse(link)
    
    if (not o.netloc.endswith(suffix)) or len(o.geturl().split('.')) >= 3:
        return False
    result = o.scheme + "://" + o.netloc + '/'
    
    return result
