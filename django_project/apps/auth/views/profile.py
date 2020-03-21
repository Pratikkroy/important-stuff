from rest_framework.views import APIView
from django.utils.decorators import decorator_from_middleware_with_args
from django.contrib.auth import authenticate, login
from src.utils import HttpStatus, HttpResponse, MethodNotAllowedException, Logger
from apps.models import BlogsAuth, BlogsAuthUser

logger = Logger()

class Profile(APIView):

    def get(self, request):
        try:
            auth_obj = BlogsAuth.objects.get(auth_id=request.auth_id)
        except BlogsAuth.DoesNotExist as ex:
            return HttpResponse(
                http_status=HttpStatus.HTTP_403_FORBIDDEN,
                data='AUTH_ID_DOES_NOT_EXIST'
            )
        return HttpResponse(http_status=HttpStatus.HTTP_200_OK,
            data="Kept only for testing using drf view")
        
    def post(self, request):
        pass