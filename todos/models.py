from django.db import models


class User(models.Model):
    username = models.CharField(max_length=30)
    password = models.CharField(max_length=255)
    email = models.CharField(max_length=50)
    createdat = models.DateTimeField(auto_now_add=True)
    updatedat = models.DateTimeField(None)

    REQUIRED_FIELDS = [username, password, email, createdat]


# Create your models here.

class Todo(models.Model):
    name = models.CharField(max_length=50)
    status = models.BooleanField(default=False)
    priority = models.IntegerField(default=0)
    description = models.TextField()
    createdat = models.DateTimeField(auto_now_add=True)
    updatedat = models.DateTimeField(null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    REQUIRED_FIELDS = [name, status, priority, createdat, user]

# Create your models here.
