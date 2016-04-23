class WebViewCameraException(Exception):
    """Base camera exception"""


class ParameterReadOnly(WebViewCameraException, AttributeError):
    """Camera parameter is read only"""


class Unauthorized(WebViewCameraException):
    """Unauthorized"""


class UnexpectedResponse(WebViewCameraException):
    """Unexpected response"""


class NoCameraControlRight(WebViewCameraException):
    """Request denied due to no issuing of the control privilege request."""


class CameraNotAvailable(WebViewCameraException):
    """Camera specified with <Camera> parameter does not exist."""


class CameraNotControllable(WebViewCameraException):
    """Camera cannot be controlled due to a camera abnormality."""


class UnknownOperator(WebViewCameraException):
    """Undefined command specified."""


class InvalidParameterValue(WebViewCameraException):
    """Invalid parameter value specified."""


class OperationTimeout(WebViewCameraException):
    """Command execution not completed even at response time limit."""


class ParameterMissing(WebViewCameraException):
    """Required parameter not specified."""


class InvalidRequest(WebViewCameraException):
    """Invalid session function requested."""


class ExclusiveOperationConflict(WebViewCameraException):
    """Exclusive operation requested."""


class VideoMigrationConflict(WebViewCameraException):
    """Recording stream requested while migrating video to external memory."""


class UnknownSessionID(WebViewCameraException):
    """Specified session does not exist."""


class TooManyClients(WebViewCameraException):
    """Maximum number of connections exceeded."""


class InsufficientPrivilege(WebViewCameraException):
    """Cannot access due to access privilege."""


class RequestRefused(WebViewCameraException):
    """Request denied due to temporary connection limit of camera."""
