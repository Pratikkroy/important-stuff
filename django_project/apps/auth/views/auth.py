from rest_framework.views import APIView
from rest_framework.response import Response
from src.utils import HttpStatus, HttpResponse

class Auth(APIView):

    def get(self, request):
        print(request.user.auth_id)
        print(request.auth)
        return HttpResponse(http_status=HttpStatus.HTTP_200_OK,
            data="hello world from auth")
        
        