from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from src.utils.status import Status
from src.api_gateway import ApiGatewayService
# Create your views here.

class Blogs(APIView):

    def get(self, request):
        api_gateway = ApiGatewayService()
        return Response("Hello world")