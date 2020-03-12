from django.db import models
from . import *

class BlogsAuthUser(models.Model):
    email = models.CharField(primary_key=True, max_length=50)
    auth = models.ForeignKey(BlogsAuth, models.DO_NOTHING, blank=True, null=True)
    firstname = models.CharField(max_length=45)
    lastname = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'blogs_auth_user'


