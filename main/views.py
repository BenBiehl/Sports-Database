from django.http import HttpResponse

def index(request):
    return HttpResponse("Erm, does this work?")