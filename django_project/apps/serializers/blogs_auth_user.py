from rest_framework import serializers
from apps.models import BlogsAuthUser
from src.constants import UserGroups, Teams

class BlogsAuthUserSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = BlogsAuthUser
        fields = ['username', 'auth', 'firstname', 'lastname', 'group', 'team']
        extra_kwargs = {
            'username': {'required': True},
            'auth': {'required': True},
            'firstname': {'required': True},
            'group': {'required': True},
            'team': {'required': True},
        }
        
    def validate_group(self, group):
        if group not in dir(UserGroups):
            raise serializers.ValidationError("INVALID_GROUP")
        return group
        
    def validate_team(self, team):
        if team not in dir(Teams):
            raise serializers.ValidationError("INVALID_TEAM")
        return team