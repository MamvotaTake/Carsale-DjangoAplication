# Create your views here.
from django.http import HttpResponse


def home(request):
    return HttpResponse("Hello Takesure, cogratulations you are a backend developer")
