from urllib.parse import urlparse


def get_link_domain(link, suffix):
    o = urlparse(link)
    
    if not o.netloc.endswith(suffix):
        return False
    result = o.scheme + "://" + o.netloc + '/'
    
    return result


if __name__ == "__main__":
    pass