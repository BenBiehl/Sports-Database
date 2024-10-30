from django.db import models

# Create your models here.
class GlobalStats(models.Model):
    numUsers = models.IntegerField()

class User(models.Model):
    userName = models.CharField(max_length=20, primary_key=True)
    passWord = models.CharField(max_length=20)
    isAdmin = models.BooleanField(default=False)
    teamName = models.CharField(max_length=20, blank=True)
    userView = models.IntegerField(default=1, blank=True)

    def __str__(self):
        return self.userName

class Athlete(models.Model):
    id = models.AutoField(primary_key=True)
    height = models.CharField(max_length=5, blank=True)
    weight = models.CharField(max_length=10, blank=True)
    firstName = models.CharField(max_length=20)
    mInit = models.CharField(max_length=1)
    lastName = models.CharField(max_length=20)
    birthDate = models.DateField(blank=True)
    age = models.IntegerField()
    wins = models.IntegerField()
    losses = models.IntegerField()
    joinYear = models.IntegerField()
    teamName = models.CharField(max_length=20)