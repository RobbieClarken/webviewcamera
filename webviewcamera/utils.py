import re
from six.moves.urllib.parse import urlencode, quote
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


def parse_response(response, converters=None):
    exception = exception_from_status(response.headers['livescope-status'])
    if exception is not None:
        raise exception(error_message(response.text))
    content_type = response.headers['content-type']
    if content_type.startswith('text/'):
        return parse_parameters_response(response.text, converters)
    else:
        return response.content


def exception_from_status(status):
    if status == '0':
        return None
    elif status == '301 No Camera Control Right':
        return exceptions.NoCameraControlRight
    elif status == '302 Camera is not available':
        return exceptions.CameraNotAvailable
    elif status == '303 Camera is not controllable':
        return exceptions.CameraNotControllable
    elif status == '401 Unknown Operator':
        return exceptions.UnknownOperator
    elif status == '403 Invalid Parameter Value':
        return exceptions.InvalidParameterValue
    elif status == '404 Operation Timeout':
        return exceptions.OperationTimeout
    elif status == '406 Parameter Missing':
        return exceptions.ParameterMissing
    elif status == '407 Invalid Request':
        return exceptions.InvalidRequest
    elif status == '408 Conflict':
        return exceptions.ExclusiveOperationConflict
    elif status == '409 Conflict':
        return exceptions.VideoMigrationConflict
    elif status == '501 Unknown Connection ID':
        return exceptions.UnknownSessionID
    elif status == '503 Too many clients':
        return exceptions.TooManyClients
    elif status == '507 Insufficient Privilege':
        return exceptions.InsufficientPrivilege
    elif status == '508 Request Refused':
        return exceptions.RequestRefused
    else:
        return exceptions.WebViewCameraException


def error_message(response_text):
    if '--- WebView Livescope Http Server Error ---' in response_text:
        return ' '.join(response_text.splitlines()[1:])
    else:
        return ''


def parse_parameters_response(response_text, converters=None):
    if converters is None:
        converters = {}
    regex = re.compile(r'([^:=]+)(?::=|==|=)(.*)')
    try:
        data = {}
        for line in response_text.split('\n'):
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
