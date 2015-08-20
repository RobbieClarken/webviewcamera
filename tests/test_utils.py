from webviewcamera import utils
from webviewcamera import exceptions
import pytest


def test_urlencode_with_safe_chars():
    assert utils.urlencode_with_safe_chars({'x': 'a,b'}, ',') == 'x=a,b'


def test_exception_from_status_where_status_is_ok():
    assert utils.exception_from_status('0') == None


def test_exception_from_status_where_status_is_bad():
    exception = utils.exception_from_status('302 Camera is not available')
    assert exception == exceptions.CameraNotAvailable


def test_error_message():
    text = ('--- WebView Livescope Http Server Error ---\n'
            'Parameter Missing\n'
            '1 parameter(s)\n')
    assert utils.error_message(text) == 'Parameter Missing 1 parameter(s)'


def test_parse_parameters_response():
    parsed = utils.parse_parameters_response('x:=1\ny==2\nz=3')
    assert parsed['x'] == '1'
    assert parsed['y'] == '2'
    assert parsed['z'] == '3'


def test_parse_parameters_response_raises_exception():
    with pytest.raises(exceptions.UnexpectedResponse):
        utils.parse_parameters_response('blerg')


def test_parse_parameters_response_with_conversions():
    converters = {
        'y': int,
        'z': lambda s: [int(v) for v in s.split(',')]
    }
    parsed = utils.parse_parameters_response('x:=1\ny==2\nz=3,4',
                                             converters=converters)
    assert parsed['x'] == '1'
    assert parsed['y'] == 2
    assert parsed['z'] == [3, 4]


def test_int_converter():
    int_converter = utils.Converter(int)
    assert int_converter('1') == 1


def test_int_list_converter():
    int_converter = utils.Converter(int, list_=True)
    assert int_converter('1,2') == [1, 2]
