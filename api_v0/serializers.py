from rest_framework import serializers
from articles.models import Article
from django.contrib.auth.models import User


class ArticlePreviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = [
            'id',
            'title',
            'created_at',
            'announce',
            'url',
        ]


class ArticleDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = [
            'title',
            'created_at',
            'text',
        ]


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'id',
            'username',
            'email',
            'first_name',
            'last_name',
            'is_staff'
        ]
