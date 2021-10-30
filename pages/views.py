# Create your views here.
from django.shortcuts import render

from pages.models import Team


def home(request):
    teams = Team.objects.all()

    data = {
        'team': teams,
    }
    return render(request, 'pages/home.html', data)
