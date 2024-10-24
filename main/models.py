from django.db import models

# Create your models here.
class User(models.Model):
    userName = models.CharField(max_length=20, primary_key=True)
    passWord = models.CharField(max_length=20)
    isAdmin = models.BooleanField(default=False)
    teamName = models.CharField(max_length=20)
    userView = models.IntegerField(default=1)