from django.conf.global_settings import AUTH_USER_MODEL
from rest_framework import serializers, settings
from .models import Author, Book


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ['id', 'name', 'added_by', 'create_by']


class BookSerializer(serializers.ModelSerializer):
    title = serializers.CharField(required=True)
    description = serializers.CharField(required=True)
    author = serializers.PrimaryKeyRelatedField(queryset=Author.objects)
    added_by = serializers.PrimaryKeyRelatedField(queryset=AUTH_USER_MODEL)
    created_date = serializers.DateTimeField(required=True)

    class Meta:
        model = Book
        fields = '__all__'
