from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from .serializers import UserSerializer, BookSerializer
from .models import User, Book


def homepage(request):
    print(type(render))
    return render(request, 'homepage.html', {"name": "Django"})


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class BookUserViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.filter(user_id=1)
    serializer_class = BookSerializer