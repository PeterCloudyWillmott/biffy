from .client import *

def ewdconnect(*args, **kwargs):
    """connect(host, port=0, auth=None, username=None, password=None, protocol='http', path="/")"""
    return Client(*args, **kwargs)
