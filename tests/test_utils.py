from webviewcamera import utils
from webviewcamera import exceptions
import pytest


def test_parse_response():
    parsed = utils.parse_response('x:=1\ny==2\nz=3')
    assert parsed['x'] == '1'
    assert parsed['y'] == '2'
    assert parsed['z'] == '3'


def test_parse_response_raises_exception():
    with pytest.raises(exceptions.UnexpectedResponse):
        utils.parse_response('blerg')
