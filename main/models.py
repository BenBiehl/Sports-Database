from django.db import models

# Create your models here.
class User(models.Model):
    userName = models.CharField(max_length=20, primary_key=True)
    passWord = models.CharField(max_length=20)
    isAdmin = models.BooleanField(default=False)
    teamName = models.CharField(max_length=20)
    userView = models.IntegerField(default=1)

class Athlete(models.Model):
    id = models.IntegerField(primary_key=True)
    height = models.CharField(max_length=5)
    weight = models.CharField(max_length=10)
    firstName = models.CharField(max_length=20)
    mInit = models.CharField(max_length=1)
    lastName = models.CharField(max_length=20)
    birthDate = models.DateField()
    age = models.IntegerField()
    wins = models.IntegerField()
    losses = models.IntegerField()
    joinYear = models.IntegerField()
    teamName = models.CharField(max_length=20)