import requests

def get_link_server(link):
    try:
        r = requests.get(link)
    except Exception:
        return False
    
    return r.headers['Server']


if __name__ == "__main__":
    pass