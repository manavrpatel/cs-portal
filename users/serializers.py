from rest_framework import serializers
from users.models import User
from django.contrib import auth
from rest_framework.exceptions import AuthenticationFailed

class UserCreateSerializer(serializers.ModelSerializer) :
    class Meta:
        model=User
        fields = ['userID', 'username', 'email', 'role']

    def create(self, validated_data):
        return User.objects.create(**validated_data)
    