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

def exception_from_status(status):
    if status == '0':
        return None
    elif status == '302 Camera is not available':
        return CameraNotAvailable
    elif status == '303 Camera is not controllable':
        return CameraNotControllable
    elif status == '401 Unknown Operator':
        return UnknownOperator
    elif status == '403 Invalid Parameter Value':
        return InvalidParameterValue
    elif status == '404 Operation Timeout':
        return OperationTimeout
    elif status == '406 Parameter Missing':
        return ParameterMissing
    elif status == '407 Invalid Request':
        return InvalidRequest
    elif status == '408 Conflict':
        return ExclusiveOperationConflict
    elif status == '409 Conflict':
        return VideoMigrationConflict
    elif status == '501 Unknown Connection ID':
        return UnknownSessionID
    elif status == '503 Too many clients':
        return TooManyClients
    elif status == '507 Insufficient Privilege':
        return InsufficientPrivilege
    elif status == '508 Request Refused':
        return RequestRefused
    else:
        return WebViewCameraException
