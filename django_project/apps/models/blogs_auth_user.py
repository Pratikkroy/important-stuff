from django.db import models
from . import *

class BlogsAuthUser(models.Model):
    username = models.CharField(primary_key=True, max_length=50)
    auth = models.ForeignKey(BlogsAuth, models.DO_NOTHING)
    firstname = models.CharField(max_length=30)
    lastname = models.CharField(max_length=30, blank=True, null=True)
    group = models.CharField(max_length=45)
    team = models.CharField(max_length=45)
    
    class Meta:
        managed = False
        db_table = 'blogs_auth_user'


