from rest_framework.views import APIView
from django.utils.decorators import decorator_from_middleware_with_args
from django.contrib.auth import authenticate, login
from src.utils import HttpStatus, HttpResponse, MethodNotAllowedException, Logger
from src.constants import LoginType
from apps.models import BlogsAuth
from middlewares.validator import RequestBodyValidatorMiddleware
from apps.json_schema_validators import login_json_schema

logger = Logger()
login_params_validator = decorator_from_middleware_with_args(RequestBodyValidatorMiddleware)

class Login(APIView):

    def get(self, request):
        return HttpResponse(http_status=HttpStatus.HTTP_200_OK,
            data="Kept only for testing using drf view")
        
    
    @login_params_validator(login_json_schema)
    def post(self, request):
        self.sanitize_request_data(request.data)
        user = authenticate(request, auth_id="", password=request.data['password'])
        if isinstance(user,HttpResponse):
            return user
        elif user is not None:
            login(request, user)
            return HttpResponse(http_status=HttpStatus.HTTP_200_OK)
        else:
            return HttpResponse(http_status=HttpStatus.HTTP_500_INTERNAL_SERVER_ERROR,
                data="ERROR_OCCURRED")
            
    
    def sanitize_request_data(self, data):
        if data.get('loginType').upper() == LoginType.EMAIL:
            data['email'].lower()
        