from django.utils.deprecation import MiddlewareMixin
from src.api_gateway import ApiGatewayService

class RequestBodyValidatorMiddleware(MiddlewareMixin):
    def __init__(self, json_schema):
        self.json_schema = json_schema
        
    def process_request(self, request):
        response = ApiGatewayService.validate_request_body(
            json_schema=self.json_schema, body=request.request.data)
        
        if response is not None:
            return response
        
        
