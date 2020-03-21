from rest_framework.views import APIView
from django.utils.decorators import decorator_from_middleware_with_args
from src.utils import HttpStatus, HttpResponse, MethodNotAllowedException, Logger
from apps.models import BlogsAuth
from custom_middlewares.validator import RequestBodyValidatorMiddleware
from apps.json_schema_validators import refresh_token_json_schema
from custom_auth_backend.jwt.token import Token as JWTToken

logger = Logger()
refresh_token_params_validator = decorator_from_middleware_with_args(RequestBodyValidatorMiddleware)

class Token(APIView):
    
    def get(self, request):
        return HttpResponse(http_status=HttpStatus.HTTP_200_OK,
            data="Kept only for testing using drf view")
        
    @refresh_token_params_validator(refresh_token_json_schema)
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