from rest_framework.views import APIView
from django.utils.decorators import decorator_from_middleware_with_args
from src.utils import HttpStatus, HttpResponse, MethodNotAllowedException
from middlewares.validators import LoginMiddleware
from ..validators.login import json_schema

login_params_validator = decorator_from_middleware_with_args(LoginMiddleware)

class Login(APIView):

    def get(self, request, validator=None):
        return HttpResponse(http_status=HttpStatus.HTTP_200_OK,
            data="hello world from login")
    
    @login_params_validator(json_schema)
    def post(self, request):
        return HttpResponse(http_status=HttpStatus.HTTP_200_OK,
            data="hello world from login post")
        