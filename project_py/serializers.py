from .models import User, Book
from rest_framework import serializers
from django.db import models

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        exclude = ['password']


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'


# class Book_UserSerializer(serializers.ModelSerializer):
#     user = serializers.SerializerMethodField()
#
#     def get_books(self, user):
#         qs = Book.objects.filter(user_id=user)
#         serializer = Book_UserSerializer(instance=qs, many=True)
#         return serializer.data
#
#     class Meta:
#         model = Book
#         fields = '__all__'
