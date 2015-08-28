from requests import Session
import six
import yaml
from six.moves.urllib.parse import urljoin
from pkg_resources import resource_stream
from .utils import parse_response, Converter, urlencode_with_safe_chars


class Camera(object):

    def __init__(self, url, specification=None):
        self._base_url = urljoin(url, '/-wvhttp-01-/')
        if specification is None:
            stream = resource_stream(__name__, 'canon-vb.specification.yml')
            specification = yaml.load(stream)
        converters = {}
        for parameter, info in specification.items():
            if info['type'] not in ('str', 'int', 'float'):
                raise Exception('Unexpected type')
            type_ = eval(info['type'])
            converters[parameter] = Converter(type_, info.get('list'))
        self._converters = converters
        self._session = Session()


    def url(self, endpoint):
        return urljoin(self._base_url, endpoint)


    def query(self, endpoint, params=None, stream=False):
        if params is not None:
            params = {k: v for k, v in params.items() if v is not None}
            params = urlencode_with_safe_chars(params, safe='+:,!')
        url = self.url(endpoint)
        response = self._session.get(url, params=params, stream=stream)
        return response


    def info(self, parameter=None):
        if parameter and not isinstance(parameter, six.string_types):
            parameter = ','.join(parameter)
        params = dict(item=parameter)
        response = self.query('info.cgi', params=params)
        return parse_response(response, self._converters)


    def get(self, parameter):
        info = self.info(parameter)
        return info[parameter]


    def control(self, updates):
        response = self.query('control.cgi', params=updates)
        return parse_response(response, self._converters)


    def set(self, parameter, value):
        self.control({parameter: value})


    def image(self, format=None):
        params = {
            'v': format,
        }
        response = self.query('image.cgi', params=params)
        return parse_response(response)


    def video(self, format='h264', duration=None):
        params = {
            'v': format,
            'duration': duration,
        }
        response = self.query('video.cgi', params=params)
        return parse_response(response)
