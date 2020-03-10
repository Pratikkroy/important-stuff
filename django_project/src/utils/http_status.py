from . import ClassShouldNotInstantiateException

class HttpStatus:

    def __init__(self):
        raise ClassShouldNotInstantiateException
    
    
    HTTP_100_CONTINUE= {'status': 100, 'message': 'CONTINUE '}
    HTTP_101_SWITCHING_PROTOCOLS= {'status': 101, 'message': 'SWITCHING_PROTOCOLS '}
    HTTP_200_OK= {'status': 200, 'message': 'OK '}
    HTTP_201_CREATED= {'status': 201, 'message': 'CREATED '}
    HTTP_202_ACCEPTED= {'status': 202, 'message': 'ACCEPTED '}
    HTTP_203_NON_AUTHORITATIVE_INFORMATION= {'status': 203, 'message': 'NON_AUTHORITATIVE_INFORMATION '}
    HTTP_204_NO_CONTENT= {'status': 204, 'message': 'NO_CONTENT '}
    HTTP_205_RESET_CONTENT= {'status': 205, 'message': 'RESET_CONTENT '}
    HTTP_206_PARTIAL_CONTENT= {'status': 206, 'message': 'PARTIAL_CONTENT '}
    HTTP_207_MULTI_STATUS= {'status': 207, 'message': 'MULTI_STATUS '}
    HTTP_300_MULTIPLE_CHOICES= {'status': 300, 'message': 'MULTIPLE_CHOICES '}
    HTTP_301_MOVED_PERMANENTLY= {'status': 301, 'message': 'MOVED_PERMANENTLY '}
    HTTP_302_FOUND= {'status': 302, 'message': 'FOUND '}
    HTTP_303_SEE_OTHER= {'status': 303, 'message': 'SEE_OTHER '}
    HTTP_304_NOT_MODIFIED= {'status': 304, 'message': 'NOT_MODIFIED '}
    HTTP_305_USE_PROXY= {'status': 305, 'message': 'USE_PROXY '}
    HTTP_306_RESERVED= {'status': 306, 'message': 'RESERVED '}
    HTTP_307_TEMPORARY_REDIRECT= {'status': 307, 'message': 'TEMPORARY_REDIRECT '}
    HTTP_400_BAD_REQUEST= {'status': 400, 'message': 'BAD_REQUEST '}
    HTTP_401_UNAUTHORIZED= {'status': 401, 'message': 'UNAUTHORIZED '}
    HTTP_402_PAYMENT_REQUIRED= {'status': 402, 'message': 'PAYMENT_REQUIRED '}
    HTTP_403_FORBIDDEN= {'status': 403, 'message': 'FORBIDDEN '}
    HTTP_404_NOT_FOUND= {'status': 404, 'message': 'NOT_FOUND '}
    HTTP_405_METHOD_NOT_ALLOWED= {'status': 405, 'message': 'METHOD_NOT_ALLOWED '}
    HTTP_406_NOT_ACCEPTABLE= {'status': 406, 'message': 'NOT_ACCEPTABLE '}
    HTTP_407_PROXY_AUTHENTICATION_REQUIRED= {'status': 407, 'message': 'PROXY_AUTHENTICATION_REQUIRED '}
    HTTP_408_REQUEST_TIMEOUT= {'status': 408, 'message': 'REQUEST_TIMEOUT '}
    HTTP_409_CONFLICT= {'status': 409, 'message': 'CONFLICT '}
    HTTP_410_GONE= {'status': 410, 'message': 'GONE '}
    HTTP_411_LENGTH_REQUIRED= {'status': 411, 'message': 'LENGTH_REQUIRED '}
    HTTP_412_PRECONDITION_FAILED= {'status': 412, 'message': 'PRECONDITION_FAILED '}
    HTTP_413_REQUEST_ENTITY_TOO_LARGE= {'status': 413, 'message': 'REQUEST_ENTITY_TOO_LARGE '}
    HTTP_414_REQUEST_URI_TOO_LONG= {'status': 414, 'message': 'REQUEST_URI_TOO_LONG '}
    HTTP_415_UNSUPPORTED_MEDIA_TYPE= {'status': 415, 'message': 'UNSUPPORTED_MEDIA_TYPE '}
    HTTP_416_REQUESTED_RANGE_NOT_SATISFIABLE= {'status': 416, 'message': 'REQUESTED_RANGE_NOT_SATISFIABLE '}
    HTTP_417_EXPECTATION_FAILED= {'status': 417, 'message': 'EXPECTATION_FAILED '}
    HTTP_422_UNPROCESSABLE_ENTITY= {'status': 422, 'message': 'UNPROCESSABLE_ENTITY '}
    HTTP_423_LOCKED= {'status': 423, 'message': 'LOCKED '}
    HTTP_424_FAILED_DEPENDENCY= {'status': 424, 'message': 'FAILED_DEPENDENCY '}
    HTTP_428_PRECONDITION_REQUIRED= {'status': 428, 'message': 'PRECONDITION_REQUIRED '}
    HTTP_429_TOO_MANY_REQUESTS= {'status': 429, 'message': 'TOO_MANY_REQUESTS '}
    HTTP_431_REQUEST_HEADER_FIELDS_TOO_LARGE= {'status': 431, 'message': 'REQUEST_HEADER_FIELDS_TOO_LARGE '}
    HTTP_451_UNAVAILABLE_FOR_LEGAL_REASONS= {'status': 451, 'message': 'UNAVAILABLE_FOR_LEGAL_REASONS '}
    HTTP_500_INTERNAL_SERVER_ERROR= {'status': 500, 'message': 'INTERNAL_SERVER_ERROR '}
    HTTP_501_NOT_IMPLEMENTED= {'status': 501, 'message': 'NOT_IMPLEMENTED '}
    HTTP_502_BAD_GATEWAY= {'status': 502, 'message': 'BAD_GATEWAY '}
    HTTP_503_SERVICE_UNAVAILABLE= {'status': 503, 'message': 'SERVICE_UNAVAILABLE '}
    HTTP_504_GATEWAY_TIMEOUT= {'status': 504, 'message': 'GATEWAY_TIMEOUT '}
    HTTP_505_HTTP_VERSION_NOT_SUPPORTED= {'status': 505, 'message': 'HTTP_VERSION_NOT_SUPPORTED '}
    HTTP_507_INSUFFICIENT_STORAGE= {'status': 507, 'message': 'INSUFFICIENT_STORAGE '}
    HTTP_511_NETWORK_AUTHENTICATION_REQUIRED= {'status': 511, 'message': 'NETWORK_AUTHENTICATION_REQUIRED '}

    
    @staticmethod
    def is_informational(code):
        return 100 <= code <= 199

    @staticmethod
    def is_success(code):
        return 200 <= code <= 299

    @staticmethod
    def is_redirect(code):
        return 300 <= code <= 399

    @staticmethod
    def is_client_error(code):
        return 400 <= code <= 499

    @staticmethod
    def is_server_error(code):
        return 500 <= code <= 599
