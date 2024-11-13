from django.db import models

# Create your models here.
class GlobalStat(models.Model):
    numUsers = models.IntegerField()

class Athlete(models.Model):
    SPORT_CHOICES = [
        ('Baseball', 'Baseball'),
        ('Basketball', 'Basketball'),
        ('Soccer', 'Soccer'),
        ('Football', 'Football'),
    ]

    id = models.AutoField(primary_key=True)
    firstName = models.CharField(max_length=20, default='N/A')
    lastName = models.CharField(max_length=20, default='N/A')
    height = models.CharField(max_length=5, default='N/A',blank=True, null=True)
    weight = models.IntegerField(blank=True, null=True)
    birthDate = models.DateField(blank=True, null=True)
    age = models.IntegerField(blank=True, null=True)
    wins = models.IntegerField(blank=True, null=True)
    losses = models.IntegerField(blank=True, null=True)
    joinYear = models.IntegerField(blank=True, null=True)
    sport = models.CharField(max_length=20, choices=SPORT_CHOICES, default='Baseball')
    teamName = models.CharField(max_length=20, default='N/A')
    position = models.CharField(max_length=20, default='N/A', blank=True, null=True)
    gamesPlayed = models.IntegerField(default=0, blank=True, null=True)
    
    def winRate(self):
        if self.wins + self.losses == 0:
            return 0
        return self.wins / (self.wins + self.losses)

    def __str__(self):
        return f"{self.firstName} {self.lastName}"
    
class User(models.Model):
    userName = models.CharField(max_length=20, primary_key=True)
    passWord = models.CharField(max_length=20)
    isAdmin = models.BooleanField(default=False)
    teamName = models.CharField(max_length=20, blank=True)
    userView = models.IntegerField(default=1, blank=True)
    favAthlete = models.ForeignKey(Athlete, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.userName
    
class BaseballStat(models.Model):
    athlete = models.OneToOneField(Athlete, on_delete=models.CASCADE, primary_key=True)
    battingAvg = models.FloatField(blank=True)
    homeRuns = models.IntegerField(blank=True)
    era = models.FloatField(blank=True)
    rbi = models.IntegerField(blank=True)
    stolenBases = models.IntegerField(blank=True)

class BasketballStat(models.Model):
    athlete = models.OneToOneField(Athlete, on_delete=models.CASCADE, primary_key=True)
    pointsPG = models.FloatField(blank=True)
    assistsPG = models.FloatField(blank=True)
    reboundsPG = models.FloatField(blank=True)
    threePPerc = models.FloatField(blank=True)
    freeThrowPerc = models.FloatField(blank=True)

class SoccerStat(models.Model):
    athlete = models.OneToOneField(Athlete, on_delete=models.CASCADE, primary_key=True)
    goalsScored = models.IntegerField(blank=True)
    shots = models.IntegerField(blank=True)
    saves = models.IntegerField(blank=True)
    fouls = models.IntegerField(blank=True)
    minutesPlayed = models.IntegerField(blank=True)

class FootballStat(models.Model):
    athlete = models.OneToOneField(Athlete, on_delete=models.CASCADE, primary_key=True)
    passingYards = models.IntegerField(blank=True)
    rushingYards = models.IntegerField(blank=True)
    tackles = models.IntegerField(blank=True)
    sacks = models.IntegerField(blank=True)
    interceptions = models.IntegerField(blank=True)

