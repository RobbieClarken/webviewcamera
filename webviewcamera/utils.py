import re
from . import exceptions

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

