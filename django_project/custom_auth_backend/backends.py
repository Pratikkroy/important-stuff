from custom_auth_backend.models import BlogsAuth
from src.utils import Logger,HttpStatus, HttpResponse
from src.constants import LoginType

logger = Logger()

# To create Custom auth backend, use below link
# https://www.pythoncircle.com/post/28/creating-custom-user-model-and-custom-authentication-in-django/
# To use admin functionality like creating superuser, use below link
# https://www.fomfus.com/articles/how-to-use-email-as-username-for-django-authentication-removing-the-username
# While defining authenticate request param is mandatory for django-3.x
# https://stackoverflow.com/a/59442029

class BlogsAuthBackend(object):

    # do not change the params. this authenticate method would not called
    def authenticate(self, request, auth_id, password):
        try:
            login_type = request.data['loginType'].upper()
            if login_type == LoginType.EMAIL:
                login_id = request.data['email']
                users = BlogsAuth.objects.filter(email=request.data['email'])
            else:
                login_id = request.data['phone']
                users = BlogsAuth.objects.filter(phone=request.data['phone'])
                
            if users.count() == 0:
                logger.error("user with login {} does not exists ".format(login_id))
                return HttpResponse(http_status=HttpStatus.HTTP_401_UNAUTHORIZED,
                    data="EMAIL_PHONE_DOES_NOT_EXIST")
            elif users.count() == 1:
                user = users[0]
                if user.check_password(password):
                    return user
                else:
                    return HttpResponse(http_status=HttpStatus.HTTP_401_UNAUTHORIZED,
                        data="PASSWORD_INCORRECT")
            else:
                logger.error("More than one user with login {} exists ".format(login_id))
                return HttpResponse(http_status=HttpStatus.HTTP_401_UNAUTHORIZED,
                        data="MORE_THAN_ONE_USER_EXIST")  
        except Exception as ex:
            logger.exception(ex)
            return None
    
    # this method is used anywhere becuase we are not using session based authentication
    def get_user(self, auth_id):
        try:
            user = BlogsAuth.objects.get(auth_id=auth_id)
            if user.status == "ACTIVE":
                return user
            return HttpResponse(http_status=HttpStatus.HTTP_401_UNAUTHORIZED,
                        data="USER_INACTIVE")
        except BlogsAuth.DoesNotExist:
            logger.error("user with auth_id {} not found".format(auth_id))
            return None   