from django.shortcuts import render
from rest_framework import viewsets
from .serializers import UserSerializer, BookSerializer, BookSerializeruser1, BookSerializeruser2
from .models import User, Book


def homepage(request):
    users = User.objects.all()
    print(type(render))
    return render(request, 'homepage.html', {"name": "Django", "users": users})


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class BookUser1ViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.filter(user_id=1)
    serializer_class = BookSerializeruser1


class BookUser2ViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.filter(user_id=2)
    serializer_class = BookSerializeruser2

