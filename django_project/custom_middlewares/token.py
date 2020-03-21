from django.utils.deprecation import MiddlewareMixin
from settings.base import URIS_TO_IGNORE_FOR_TOKEN_AUTH
from custom_auth_backend.jwt.settings import SIMPLE_JWT
from src.utils import HttpStatus, HttpResponse
from rest_framework.renderers import JSONRenderer

class TokenMiddleware(MiddlewareMixin):
    def __init__(self, get_response=None):
        self.get_response = get_response
        
    def process_request(self, request):
        if request.path not in URIS_TO_IGNORE_FOR_TOKEN_AUTH:
            auth_token = request.META.get('HTTP_AUTHORIZATION')
            if auth_token is None:
                return HttpResponse(http_status=HttpStatus.HTTP_403_FORBIDDEN,
                data="AUTH_TOKEN_REQUIRED")
            
            auth_header_type, auth_token = auth_token.split()
            if auth_header_type in SIMPLE_JWT['AUTH_HEADER_TYPES']:
                request.token = auth_token
            else:
                return HttpResponse(http_status=HttpStatus.HTTP_403_FORBIDDEN,
                data="AUTH_HEADER_TYPE_INVALID")
    
    
    def process_response(self, request, response):
        return response
        
        
        
