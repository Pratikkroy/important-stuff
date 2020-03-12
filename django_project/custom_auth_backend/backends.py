from accounts.models import BlogsAuth
import logging


class BlogsAuthBackend(object):
    def authenticate(self, email, password):    
        try:
            user = BlogsAuth.objects.get(email=email)
            if user.check_password(password):
                return user
            else:
                return None
        except BlogsAuth.DoesNotExist:
            logging.getLogger("error_logger").error("user with login %s does not exists " % login)
            return None
        except Exception as e:
            logging.getLogger("error_logger").error(repr(e))
            return None

    def get_user(self, auth_id):
        try:
            user = BlogsAuth.objects.get(auth_id=auth_id)
            if user.status == "ACTIVE":
                return user
            return None
        except BlogsAuth.DoesNotExist:
            logging.getLogger("error_logger").error("user with %(auth_id)d not found")
            return None