from django.shortcuts import render
from rest_framework import generics, status, permissions
from app1.serializers import *
from app1.models import User
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny

class UserRegistartionApi(generics.CreateAPIView):
    serializer_class = UserSerializer
    queryset = User


class UserLoginApi(generics.GenericAPIView):
    serializer_class =LoginSerializer

    def post(self,request):
        serializer=self.serializer_class(data=request.data)
        if serializer.is_valid():
            return Response(serializer.data,status=status.HTTP_200_OK)
        else:
            return Response(serializer.data,status=status.HTTP_400_BAD_REQUEST)


class CreatePostApi(generics.ListCreateAPIView):
    serializer_class = NewsSerializer
    queryset = News.objects.all()

    # permission_classes = (permissions.IsAuthenticated,IsAuthor) login author token only created this api

    # def perform_create(self, serializer):
    #     return serializer.save(user=self.request.user)

    # def get_queryset(self):
    #     return self.queryset.filter(user=self.request.user)

class ViewPostApiView(generics.ListAPIView):
    serializer_class = NewsSerializer
    queryset = News.objects.all()

    permission_classes = (permissions.AllowAny,)

class AuthorNewsUpdateView(generics.RetrieveUpdateAPIView):
    serializer_class = NewsSerializer
    queryset = News.objects.all()
    # permission_classes = (permissions.IsAuthenticated,IsAuthor)
    lookup_field = 'id'