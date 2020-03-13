from django.db import models
from . import *

class BlogsAuth(models.Model):
    auth_id = models.CharField(primary_key=True, max_length=50)
    password = models.CharField(max_length=100)
    email = models.CharField(unique=True, max_length=45, blank=True, null=True)
    phone = models.CharField(unique=True, max_length=45, blank=True, null=True)
    status = models.CharField(max_length=45)
    is_staff = models.IntegerField()
    last_login = models.DateTimeField()
    register_time = models.DateTimeField()
    
    class Meta:
        managed = False
        db_table = 'blogs_auth'


