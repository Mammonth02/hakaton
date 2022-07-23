from rest_framework import serializers
from apps.user.models import *


class UserCreatSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'group', 'last_name', 'first_name']

    def create(self, validated_data):
        password = validated_data['password']
        user = super().create(validated_data)
        user.set_password(password)
        user.save()
        return user

class UserUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'image', 'phone', 'password', 'direction']


class UserDeleteSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'image',]


class UserDetailSerializerToDeveloper(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'image', 'phone', 'direction', 'city']


class UserDetailSerializerToCustomer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'image', 'phone', 'city']


class UserListSerializerToDeveloper(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'image', 'phone', 'direction', 'city']