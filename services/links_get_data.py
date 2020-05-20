import requests

def get_link_server(link):
    try:
        r = requests.get(link)
        server = r.headers['Server']
    except Exception:
        return None

    return server


if __name__ == "__main__":
    pass