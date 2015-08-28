from webviewcamera import Camera, exceptions
from webviewcamera.parameters import ZOOM
import pytest
from vcr import VCR
from six import BytesIO
from PIL import Image


URL = 'http://10.109.2.134'
vcr = VCR(cassette_library_dir='tests/fixtures/cassettes')


@pytest.fixture
def camera():
    return Camera(URL)


def test_camera_url(camera):
    assert camera.url('info.cgi') == URL + '/-wvhttp-01-/info.cgi'


@vcr.use_cassette()
def test_info(camera):
    info = camera.info()
    assert isinstance(info['realtime'], float)
    assert 1000000000 < info['realtime'] < 5000000000
    assert isinstance(info['v.list'], list)
    assert 'jpg:320x240:3:30000' in info['v.list']
    assert info[ZOOM] == info['c.1.zoom']


@vcr.use_cassette()
def test_info_with_parameter(camera):
    info = camera.info('s.hardware')
    assert len(info.keys()) == 3
    assert info['s.hardware'].startswith('Canon')


@vcr.use_cassette()
def test_info_with_multiple_parameters(camera):
    info = camera.info(['s.hardware', 's.epoch'])
    assert len(info.keys()) == 4


@vcr.use_cassette()
def test_get(camera):
    hardware = camera.get('s.hardware')
    assert hardware.startswith('Canon')


@vcr.use_cassette()
def test_control(camera):
    response = camera.control({'c.1.zoom': 5000})
    assert response['c.1.zoom'] == 5000


@vcr.use_cassette()
def test_set(camera):
    camera.set('c.1.zoom', 5000)


@vcr.use_cassette()
def test_set_with_invalid_parameter(camera):
    with pytest.raises(exceptions.ParameterMissing):
        camera.set('blerg', 1)


@vcr.use_cassette()
def test_control_without_parameter(camera):
    with pytest.raises(exceptions.ParameterMissing):
        camera.control({})


@vcr.use_cassette()
def test_image(camera):
    image = camera.image()
    assert isinstance(image, bytes)
    assert len(image) > 10000


@vcr.use_cassette()
def test_image_with_format(camera):
    data = camera.image(format='jpg:320x240')
    image = Image.open(BytesIO(data))
    assert image.size == (320, 240)


@vcr.use_cassette()
def test_video(camera):
    video = camera.video(duration=1)
    assert isinstance(video, bytes)
    assert len(video) > 10000
