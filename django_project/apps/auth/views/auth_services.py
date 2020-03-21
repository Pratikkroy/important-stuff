from apps.models import BlogsAuth
from src.utils import HttpStatus, HttpResponse

class AuthServices:
    
    @staticmethod
    def get_auth_obj(auth_id):
        try:
            auth_obj = BlogsAuth.objects.get(auth_id=auth_id)
        except BlogsAuth.DoesNotExist:
            return HttpResponse(
                http_status=HttpStatus.HTTP_403_FORBIDDEN,
                data='AUTH_ID_DOES_NOT_EXIST'
            )
        return auth_obj