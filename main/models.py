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
    height = models.CharField(max_length=5, default='N/A')
    weight = models.CharField(max_length=10, default='N/A')
    firstName = models.CharField(max_length=20, default='N/A')
    mInit = models.CharField(max_length=1, default='N/A')
    lastName = models.CharField(max_length=20, default='N/A')
    birthDate = models.DateField(blank=True)
    age = models.IntegerField(blank=True)
    wins = models.IntegerField(blank=True)
    losses = models.IntegerField(blank=True)
    joinYear = models.IntegerField(blank=True)
    sport = models.CharField(max_length=20, choices=SPORT_CHOICES, default='Baseball')
    teamName = models.CharField(max_length=20, default='N/A')
    position = models.CharField(max_length=20, default='N/A')
    gamesPlayed = models.IntegerField(default=0)
    
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
    battingAvg = models.IntegerField(blank=True)
    homeRuns = models.IntegerField(blank=True)
    era = models.FloatField(blank=True)
    rbi = models.IntegerField(blank=True)
    stolenBases = models.IntegerField(blank=True)

class BasketballStat(models.Model):
    athlete = models.OneToOneField(Athlete, on_delete=models.CASCADE, primary_key=True)
    pointsPG = models.IntegerField(blank=True)
    assistsPG = models.IntegerField(blank=True)
    reboundsPG = models.IntegerField(blank=True)
    threePPerc = models.IntegerField(blank=True)
    freeThrowPerc = models.IntegerField(blank=True)

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

