from requests import Session
import yaml
from pkg_resources import resource_stream
from .utils import parse_response, Converter

try:
    from urlparse import urljoin
    from urllib import urlencode, quote
except ImportError:
    from urllib.parse import urljoin, urlencode, quote


class Camera(object):

    def __init__(self, url, specification=None):
        self._base_url = urljoin(url, '/-wvhttp-01-/')
        if specification is None:
            stream = resource_stream(__name__, 'canon-vb.specification.yaml')
            specification = yaml.load(stream)
        converters = {}
        for parameter, info in specification.items():
            if info['type']not in ('str', 'int', 'float'):
                raise Exception('Unexpected type')
            type_ = eval(info['type'])
            converters[parameter] = Converter(type_, info.get('list'))
        self._converters = converters
        self._session = Session()


    def url(self, endpoint):
        return urljoin(self._base_url, endpoint)


    def info(self):
        url = self.url('info.cgi')
        return parse_response(self._session.get(url).text, self._converters)
