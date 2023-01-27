from django.db import models


class User(models.Model):
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255, unique=True)
    username = models.CharField(max_length=255, unique=True)
    password = models.CharField(max_length=255)

    def __str__(self):
        return '%s' % self.name


class Book(models.Model):
    book_name = models.CharField(max_length=255)
    book_no_pages = models.IntegerField()
    book_page = models.IntegerField()
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
