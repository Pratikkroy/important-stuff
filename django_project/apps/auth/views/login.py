from rest_framework.views import APIView
from custom_decoraters.request_body_validator import request_body_validator
from django.contrib.auth import authenticate, login
from src.utils import HttpStatus, HttpResponse, MethodNotAllowedException, Logger
from src.constants import LoginType
from apps.models import BlogsAuth
from custom_middlewares.validator import RequestBodyValidatorMiddleware
from custom_decoraters import request_body_validator
from apps.json_schema_validators import login_json_schema
from custom_auth_backend.jwt.token import Token

logger = Logger()

class Login(APIView):

    def get(self, request):
        return HttpResponse(http_status=HttpStatus.HTTP_200_OK,
            data="Kept only for testing using drf view")
        
    
    @request_body_validator(login_json_schema)
    def post(self, request):
        self.sanitize_request_data(request.data)
        auth_obj = authenticate(request, auth_id="", password=request.data['password'])
        if isinstance(auth_obj,HttpResponse):
            return auth_obj
        elif auth_obj is not None:
            # login(request, auth_obj)
            # method is invoked to get same method invoked while register
            return self.login_response(auth_obj)
        else:
            return HttpResponse(http_status=HttpStatus.HTTP_500_INTERNAL_SERVER_ERROR,
                data="ERROR_OCCURRED")
            
    
    def sanitize_request_data(self, data):
        if data.get('loginType').upper() == LoginType.EMAIL:
            data['email'].lower()
    
    
    def login_response(self, auth_obj):
        data = {
            'auth_token': Token.get_token(payload=self.create_jwt_payload(auth_obj))
        }
          
        return HttpResponse(
            http_status=HttpStatus.HTTP_200_OK,
            data=data
        )
          
    def create_jwt_payload(self, auth_obj):
        return {
            "auth_id": auth_obj.auth_id,
        }