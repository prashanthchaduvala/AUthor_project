from rest_framework.exceptions import AuthenticationFailed

from app1.models import *
from rest_framework import serializers
from django.contrib import auth

class UserSerializer(serializers.ModelSerializer):
    password=serializers.CharField(min_length=6,max_length=10)
    class Meta:
        model=User
        fields=['name','email','password']

class LoginSerializer(serializers.ModelSerializer):
    email=serializers.EmailField()
    password=serializers.CharField(write_only=True,required=True)

    class Meta:
        model=User
        fields=['email','password']

    def validate(self, attrs):
        email=attrs.get('email','')
        password=attrs.get('password','')

        user=User.objects.get(email=email,password=password)
        if not user:
            raise AuthenticationFailed('Invalid credentials, try again')
        if not user.is_active:
            raise AuthenticationFailed('Account disabled , contact admin')
        if not user.is_verified:
            raise AuthenticationFailed('mobile is not verified')

        return {
            'email': user.email,
        }

class NewsSerializer(serializers.ModelSerializer):
    class Meta:
        model=News
        fields=['id','title','story','image']