from webviewcamera import Camera
import pytest
import vcr

URL = 'http://10.109.2.134'

@pytest.fixture
def camera():
    return Camera(URL)


def test_camera_url(camera):
    assert camera.url('info.cgi') == URL + '/-wvhttp-01-/info.cgi'


def test_info(camera):
    with vcr.use_cassette('tests/fixtures/vcr_cassettes/info.yaml'):
        info = camera.info()
    assert info['s.epoch'] == 'Mon, 22 Jun 2015 13:05:42 +1000'
