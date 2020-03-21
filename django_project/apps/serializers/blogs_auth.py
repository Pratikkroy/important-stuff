from django.contrib.auth.hashers import make_password
from rest_framework import serializers
from ..models import BlogsAuth
from src.utils import HttpStatus, HttpResponse
from src.constants import UserStatus

class BlogsAuthSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogsAuth
        fields = ['auth_id', 'password', 'email', 'phone', 'status', 'is_staff', 'last_login', 'register_time']
        extra_kwargs = {
            'auth_id': {'required': True},
            'password': {'required': True},
            'status': {'required': True},
            'is_staff': {'required': True},
            'last_login': {'required': True},
            'register_time': {'required': True}
        }
    
    def validate(self, data):        
        if self.instance:
            if (self.instance.email is None and self.instance.phone is None 
            and data.get('email') is None and data.get('phone') is None):
                raise serializers.ValidationError("Atleast email or phone should be present")
        elif data.get('email') is None and data.get('phone') is None:
            raise serializers.ValidationError("Atleast email or phone should be present")
                
                
        # we are not checking if email or phone is unique because
        # it is already checked checked when the serializer object is created
        return data
    
    def validate_status(self, status):
        if status not in dir(UserStatus):
            raise serializers.ValidationError("INVALID_STATUS")
        return status
    
    def validate_is_staff(self, is_staff):
        if is_staff not in [0,1]:
            raise serializers.ValidationError("INVALID_IS_STAFF")
        return is_staff
    
    # override create method. create_user method hash the password. create method doesn't'
    # unable to override create_user method so hashing the password
    def create(self, validated_data):
        validated_data['password'] = self.make_password(validated_data.get('password'))
        return super(BlogsAuthSerializer, self).create(validated_data)
    
    @staticmethod
    def make_password(password):
        return make_password(password)
    
    def update(self, instance, validated_data):
        for key,val in validated_data.items():
            if key not in self.Meta.fields:
                raise serializers.ValidationError(str(key)+" is not in the database fields")
            setattr(instance,key,val)
        instance.save()
        return instance
    
    @staticmethod
    def check_auth_id(auth_id):
        try:
            auth_obj = BlogsAuth.objects.get(auth_id=auth_id)
        except BlogsAuth.DoesNotExist:
            return HttpResponse(
                http_status=HttpStatus.HTTP_403_FORBIDDEN,
                data='AUTH_ID_DOES_NOT_EXIST'
            )