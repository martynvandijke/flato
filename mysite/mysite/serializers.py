from django.contrib.auth.models import User, Group
from rest_framework import serializers
from django.db import models


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')

class CustomUserSerializer(serializers.ModelSerializer):
    user  = UserSerializer()
    class Meta:
            model = models.Profile
            fields = ('room_status')


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')