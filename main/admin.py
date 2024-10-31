from django.contrib import admin

# Register your models here.
from .models import User, Athlete, GlobalStat, BaseballStat, BasketballStat, SoccerStat, FootballStat

admin.site.register(User)
admin.site.register(Athlete)
admin.site.register(GlobalStat)
admin.site.register(BaseballStat)
admin.site.register(BasketballStat)
admin.site.register(SoccerStat)
admin.site.register(FootballStat)