from rest_framework.views import APIView
from django.utils.decorators import decorator_from_middleware_with_args
from src.utils import HttpStatus, HttpResponse, MethodNotAllowedException, Utility, DateTime, Logger
from src.constants import UserStatus, UserGroups, Teams
from middlewares.validator import RequestBodyValidatorMiddleware
from apps.json_schema_validators import register_json_schema
from apps.serializers import BlogsAuthSerializer
from apps.models import BlogsAuthUser, BlogsAuth

logger = Logger()
register_params_validator = decorator_from_middleware_with_args(RequestBodyValidatorMiddleware)


class Register(APIView):

    def __init__(self):
        pass
        
    def get(self, request, validator=None):
        return HttpResponse(http_status=HttpStatus.HTTP_200_OK,
            data="Kept only for testing using drf view")
    
    
    @register_params_validator(register_json_schema)
    def post(self, request):
        self.sanitize_request_data(request.data)
        is_staff= 1 if request.data['isAdmin'] else 0
        request.data.update(auth_id=Utility.generate_uuid())
        request.data.update(status=UserStatus.ACTIVE)
        request.data.update(is_staff=is_staff)
        current_datetime = DateTime.current_datetime()
        request.data.update(last_login=current_datetime)
        request.data.update(register_time=current_datetime)
        serializer = BlogsAuthSerializer(data=request.data)
        if serializer.is_valid():
            auth_obj = serializer.save()
            result = self.create_user_entry_in_auth_user(
                auth_obj=auth_obj,
                name=request.data['name'],
                group= UserGroups.ADMIN if is_staff==1 else UserGroups.MEMBER,
                team=Teams.DEFAULT_TEAM
            )
            if result:
                # todo: add login code here
                logger.info("New user created {}".format(request.data))
                return HttpResponse(http_status=HttpStatus.HTTP_201_CREATED)
            else:
                # deleting the entry from blogs_auth table
                logger.info("deleting the newly created auth obj {}".format(auth_obj))
                BlogsAuth.objects.get(auth_id=auth_obj.auth_id).delete()
                return HttpResponse(http_status=HttpStatus.HTTP_500_INTERNAL_SERVER_ERROR)
        else:
            logger.error("serialization error {}".format(serializer.errors))
            return HttpResponse(http_status=HttpStatus.HTTP_400_BAD_REQUEST,
                                data={'serialization_error':serializer.errors})
        
        
    
    
    def sanitize_request_data(self, data):
        data['email'].lower().strip()
        data['name']['first'].strip()
        data['name']['last'].strip()
    
       
    def create_user_entry_in_auth_user(self, auth_obj, name, group, team=None):
        try:
            BlogsAuthUser.objects.create(
                username=self.create_username(name.get('first'),auth_obj.auth_id),
                auth=auth_obj,
                firstname=name.get('first'),
                lastname=name.get('last'),
                group=group,
                team=team
            )
            return True
        except Exception as ex:
            logger.exception(ex)
            return False
        
    
    def create_username(self, name, auth_id):
        return name.lower() + '-' + auth_id.split('-')[-1]