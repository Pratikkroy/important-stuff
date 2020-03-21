from rest_framework.views import APIView
from django.utils.decorators import decorator_from_middleware_with_args
from src.utils import HttpStatus, HttpResponse, Logger
from src.constants import UpdateCredentialsType
from apps.models import BlogsAuth
from apps.serializers import BlogsAuthSerializer
from custom_middlewares.validator import RequestBodyValidatorMiddleware
from apps.json_schema_validators import update_credentials_json_schema
from . import AuthServices


logger = Logger()
update_credentials_params_validator = decorator_from_middleware_with_args(RequestBodyValidatorMiddleware)

class Credentials(APIView):
    
    @update_credentials_params_validator(update_credentials_json_schema)
    def post(self, request):
        data = request.data
        if len(data) != 1:
            return HttpResponse(
                http_status=HttpStatus.HTTP_400_BAD_REQUEST,
                data="MORE_THAN_ONE_UPDATE_DATA"
            )
            
        for key, val in data.items():
            credential_type = key
            updated_data = val
            
        if credential_type.upper() not in dir(UpdateCredentialsType):
            return HttpResponse(
                http_status=HttpStatus.HTTP_400_BAD_REQUEST,
                data="INVALID_DATA_TO_UPDATE"
            )
        
        if credential_type.upper() == UpdateCredentialsType.PASSWORD:
            updated_data = BlogsAuthSerializer.make_password(updated_data)
        
        return self.update_credentials(
            request.auth_id, 
            credential_type.lower(),
            updated_data
        )  
        
    
    def update_credentials(self, auth_id, type, updated_data):
        auth_obj = AuthServices.get_auth_obj(auth_id)
        if isinstance(auth_obj, HttpResponse):
            return auth_obj
        else:
            serializer = BlogsAuthSerializer(
                auth_obj,
                data={ type: updated_data },
                partial=True
            )
            if serializer.is_valid():
                serializer.save()
                return HttpResponse(http_status=HttpStatus.HTTP_200_OK)
            else:
                logger.error("serialization error {}".format(serializer.errors))
                return HttpResponse(http_status=HttpStatus.HTTP_400_BAD_REQUEST,
                                data={'serialization_error':serializer.errors})

       
# unable to use function views because csrf error was raised.
# Class views set the csrf 
# def update_email(request):
#     pass

# def update_phone(request):
#     pass

# def update_password(request):
#     pass