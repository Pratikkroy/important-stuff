from django.shortcuts import render
from rest_framework.views import APIView
from src.utils import HttpResponse, HttpStatus
# Create your views here.

class Blogs(APIView):

    def get(self, request):
        res = HttpResponse(http_status=HttpStatus.HTTP_200_OK,
            data="hello world from blogs")
        
        return res