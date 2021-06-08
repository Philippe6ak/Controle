from rest_framework.views import APIView

from .models import User, Post, Like
from rest_framework import serializers


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('description', 'content')
        model = Post


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username']


class LikeSerializer(serializers.ModelSerializer):
    likes = UserSerializer(many=True, read_only=True)

    class Meta:
        model = Post
        fields = ['likes', ]
