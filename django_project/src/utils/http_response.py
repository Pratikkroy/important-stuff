import json
from . import HttpResponseBadFormatException, ClassShouldNotInstantiateException

class HttpResponse:
    
    def __init__(self):
        raise ClassShouldNotInstantiateException
    
    @staticmethod
    def http_response(status_code, message, body=None):
        if status_code is None or message is None:
            print("status_code::{} message::{}".format(status_code,message))
            raise HttpResponseBadFormatException
        
        return {
            'statusCode': status_code,
            'message': message,
            'body': json.dumps(body)
        }
        
        
