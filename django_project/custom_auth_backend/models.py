from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager


class UserManager(BaseUserManager):
    use_in_migrations = False
    
    # python manage.py createsuperuser
    def create_superuser(self, email, is_staff, password):
        user = self.model(
                          email = email,                         
                          is_staff = is_staff,
                          )
        user.set_password(password)
        user.save(using=self._db)
        return user

class BlogsAuth(AbstractBaseUser):
    auth_id = models.CharField(primary_key=True, max_length=20)
    password = models.CharField(max_length=45)
    email = models.CharField(unique=True, max_length=45, blank=True, null=True)
    phone = models.CharField(unique=True, max_length=45, blank=True, null=True)
    status = models.CharField(max_length=45)
    # is_staff = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        app_label = "custom_auth_backend"
        db_table = 'blogs_auth'
    
    objects = UserManager()

    USERNAME_FIELD = "email"
    # REQUIRED_FIELDS must contain all required fields on your User model, 
    # but should not contain the USERNAME_FIELD or password as these fields will always be prompted for.
    # REQUIRED_FIELDS = ['is_staff']


    def __str__(self):
        return self.email

    def get_full_name(self):
        return self.email

    def get_short_name(self):
        return self.email


    # # this methods are require to login super user from admin panel
    # def has_perm(self, perm, obj=None):
    #     return self.is_staff

    # # this methods are require to login super user from admin panel
    # def has_module_perms(self, app_label):
    #     return self.is_staff