from rest_framework.views import APIView
from django.utils.decorators import decorator_from_middleware_with_args
from src.utils import HttpStatus, HttpResponse, MethodNotAllowedException
from middlewares.validator import RequestBodyValidatorMiddleware
from ..validators.login import json_schema

register_params_validator = decorator_from_middleware_with_args(RequestBodyValidatorMiddleware)

class Register(APIView):

    def get(self, request, validator=None):
        return HttpResponse(http_status=HttpStatus.HTTP_200_OK,
            data="Kept only for testing using drf view")
    
    @register_params_validator(json_schema)
    def post(self, request):
        return HttpResponse(http_status=HttpStatus.HTTP_200_OK,
            data="hello world from register post")
        