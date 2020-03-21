from django.contrib.auth.hashers import make_password
from rest_framework import serializers
from ..models import BlogsAuth

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
        if data['email'] is None and data['phone'] is None:
            raise serializers.ValidationError("Atleast email or phone should be present")
        
        # we are not checking if email or phone is unique because
        # it is already checked checked when the serializer object is created
        return data
    
    # override create method. create_user method hash the password. create method doesn't'
    # unable to override create_user method so hashing the password
    def create(self, validated_data):
        validated_data['password'] = make_password(validated_data.get('password'))
        return super(BlogsAuthSerializer, self).create(validated_data)
    
    # Todo: complete below method
    def update(self, instance, validated_data):
        pass
    
    # Todo: complete below method(Optional)
    # def save(self):
    #     pass