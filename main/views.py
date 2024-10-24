from django.http import HttpResponse

from .models import User

def index(request):
    return HttpResponse("Not logged in")