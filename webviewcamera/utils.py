import re
from six.moves.urllib.parse import  urlencode, quote
from . import exceptions


def urlencode_with_safe_chars(query, safe=''):
    try:
        return urlencode(query, safe=safe)
    except TypeError:
        # Python 2
        if hasattr(query, 'items'):
            query = query.items()
        return '&'.join('{}={}'.format(k, quote(str(v), safe=safe))
                        for k, v in query)


def parse_response(response_data, converters=None):
    if converters is None:
        converters = {}
    regex = re.compile(r'([^:=]+)(?::=|==|=)(.*)')
    try:
        data = {}
        for line in response_data.split('\n'):
            if not line:
                continue
            attribute, value = regex.search(line).groups()
            converter = converters.get(attribute)
            if converter is not None:
                value = converter(value)
            data[attribute] = value
        return data
    except AttributeError:
        raise exceptions.UnexpectedResponse


class Converter(object):
    def __init__(self, type_, list_=False):
        self.type_ = type_
        self.list_ = list_

    def __call__(self, value):
        if self.list_:
            return [self.type_(v) for v in value.split(',')]
        else:
            return self.type_(value)

