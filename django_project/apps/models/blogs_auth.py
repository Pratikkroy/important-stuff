from django.db import models
from . import *

class BlogsAuth(models.Model):
    auth_id = models.CharField(primary_key=True, max_length=20)
    password = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'blogs_auth'


