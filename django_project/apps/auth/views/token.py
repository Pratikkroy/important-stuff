from rest_framework.views import APIView
from src.utils import HttpStatus, HttpResponse, MethodNotAllowedException, Logger
from apps.models import BlogsAuth
from custom_middlewares.validator import RequestBodyValidatorMiddleware
from custom_decoraters.request_body_validator import request_body_validator
from apps.json_schema_validators import refresh_token_json_schema
from custom_auth_backend.jwt.token import Token as JWTToken

logger = Logger()

class Token(APIView):
    
    def get(self, request):
        return HttpResponse(http_status=HttpStatus.HTTP_200_OK,
            data="Kept only for testing using drf view")
        
    @request_body_validator(refresh_token_json_schema)
    def post(self, request):
        data = {
            'auth_token': JWTToken.refresh_token(
                            access_token=request.token,
                            refresh_token=request.data.get('refresh_token')
                        )
        }
          
        return HttpResponse(
            http_status=HttpStatus.HTTP_200_OK,
            data=data
        )