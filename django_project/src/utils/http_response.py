import json
from rest_framework.response import Response
from . import HttpResponseBadFormatException, ClassShouldNotInstantiateException        
        
class HttpResponse(Response):
    
    # using "*" to enforce named params
    def __init__(self, *, http_status, http_message=None, data=None):
        if type(http_status) is dict:
            super(HttpResponse, self).__init__(
                self.__http_response(http_status.get('status'), http_status.get('message'),data)
            )
        else:
            super(HttpResponse, self).__init__(
                self.__http_response(http_status, http_message, data)
            )
             
    
    def __http_response(self, status_code, message, data=None):
        if status_code is None or message is None:
            print("status_code::{} message::{}".format(status_code,message))
            raise HttpResponseBadFormatException
        
        return {
            'statusCode': status_code,
            'message': message,
            'data': json.dumps(data)
        }