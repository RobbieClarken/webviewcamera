from requests import Session
from .utils import parse_response

try:
    from urlparse import urljoin
    from urllib import urlencode, quote
except ImportError:
    from urllib.parse import urljoin, urlencode, quote


class Camera(object):
    def __init__(self, url):
        self.base_url = urljoin(url, '/-wvhttp-01-/')
        self.session = Session()

    def url(self, endpoint):
        return urljoin(self.base_url, endpoint)

    def info(self):
        url = self.url('info.cgi')
        return parse_response(self.session.get(url).text)
