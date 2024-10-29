from django.contrib import admin

# Register your models here.
from .models import User
from .models import Athlete
from .models import GlobalStats

admin.site.register(User)
admin.site.register(Athlete)
admin.site.register(GlobalStats)
