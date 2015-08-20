from webviewcamera.utils import parse_response
from webviewcamera import exceptions
import pytest


class MockResponse(object):
    def __init__(self, headers, content=b''):
        self.headers = headers
        self.content = content

    @property
    def text(self):
        return self.content.decode('utf-8')


def test_parse_response_with_parameters():
    headers={'livescope-status': '0', 'content-type': 'text/plain'}
    response = MockResponse(headers)
    assert parse_response(response) == {}


def test_parse_response_with_bad_status():
    headers={
        'livescope-status': '406 Parameter Missing',
        'content-type': 'text/plain',
    }
    response = MockResponse(headers)
    with pytest.raises(exceptions.ParameterMissing):
        parse_response(response)


def test_parse_response_with_image():
    headers={
        'livescope-status': '0',
        'content-type': 'image/jpeg',
    }
    response = MockResponse(headers, b'image data goes here')
    assert parse_response(response) == b'image data goes here'
