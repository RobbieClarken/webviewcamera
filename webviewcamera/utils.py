import re
from . import exceptions

def parse_response(response_data):
    regex = re.compile(r'([^:=]+)(?::=|==|=)(.*)')
    try:
        data = dict(regex.search(line).groups()
                    for line in response_data.split('\n')
                    if line)
        return data
    except AttributeError:
        raise exceptions.UnexpectedResponse
