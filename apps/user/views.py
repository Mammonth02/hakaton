from django.shortcuts import render
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from apps.user.models import User
from apps.user.permissions import *
from apps.user.serializers import *
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination




# Create your views here.

class UserCreatAPI(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserCreatSerializer

class UserUpdateAPI(generics.RetrieveUpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserUpdateSerializer
    permission_classes = (UpdateProfile,)

class UserDeleteAPI(generics.RetrieveDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserDeleteSerializer
    permission_classes = (DeleteProfile,)

class UserDetailAPI(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserDetailSerializerToDeveloper
    permission_classes = (IsAuthenticated,)

    def get(self, request, *args, **kwargs):
        pk = kwargs.get('pk', None)
        user = User.objects.get(id = pk)

        if user.group == 'developer':
            return Response(UserDetailSerializerToDeveloper(user).data)
        else:
            return Response(UserDetailSerializerToCustomer(user).data)


class UserDetailAPI(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserDetailSerializerToDeveloper
    permission_classes = (IsAuthenticated,)

    def get(self, request, *args, **kwargs):
        pk = kwargs.get('pk', None)
        user = User.objects.get(id = pk)

        if user.group == 'developer':
            return Response(UserDetailSerializerToDeveloper(user).data)
        else:
            return Response(UserDetailSerializerToCustomer(user).data)


class Pagination(PageNumberPagination):
    page_size = 6
    page_size_query_param = 'page_size'
    max_page_size = 1000

class UserListAPIView(generics.ListAPIView):
    queryset = User.objects.filter(group = 'developer')
    serializer_class = UserListSerializerToDeveloper
    pagination_class = Pagination






    