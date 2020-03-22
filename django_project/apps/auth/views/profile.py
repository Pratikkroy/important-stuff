from rest_framework.views import APIView
from django.contrib.auth import authenticate, login
from src.utils import HttpStatus, HttpResponse, MethodNotAllowedException, Logger
from apps.models import BlogsAuth, BlogsAuthUser
from . import AuthServices
logger = Logger()

class Profile(APIView):

    def get(self, request):
        auth_obj = AuthServices.get_auth_obj(request.auth_id)
        if isinstance(auth_obj, HttpResponse):
            return auth_obj
        else:
            pass
        
    def post(self, request):
        pass