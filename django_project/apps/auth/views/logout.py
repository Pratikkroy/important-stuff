from rest_framework.views import APIView
from src.utils import HttpStatus, HttpResponse, MethodNotAllowedException, Utility, DateTime, Logger
from django.contrib.auth import logout

logger = Logger()
class Logout(APIView):

    def get(self, request):
        return HttpResponse(http_status=HttpStatus.HTTP_200_OK,
            data="Kept only for testing using drf view")
        
        
    def post(self, request):
        try:
            logout(request)
            return HttpResponse(http_status=HttpStatus.HTTP_200_OK)
        except Exception as ex:
            logger.exception(ex)
            return HttpResponse(http_status=HttpStatus.HTTP_500_INTERNAL_SERVER_ERROR)
        