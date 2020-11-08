from django.shortcuts import render
from django.http import HttpResponse
from .models import User
from django.template import loader
from .backend.main import get_score
from django.urls import reverse
from django.views import generic


# Create your views here.
def index(request):
    template = loader.get_template('main/user.html')
    return HttpResponse(template.render(request=request))


def leaderboard(request):
    users = User.objects.order_by('-score')
    template = loader.get_template('main/leaderboard.html')
    context = {
        'users': users,
    }
    return HttpResponse(template.render(context, request))


def submit(request):
    source = "A team of physicists at a university in the Netherlands have 3D-printed a microscopic version of the USS Voyager, an Intrepid-class starship from Star Trek. The miniature Voyager, which measures 15 micrometers (0.015 millimeters) long, is part of a project researchers at Leiden University conducted to understand how shape affects the motion and interactions of microswimmers. Microswimmers are small particles that can move through liquid on their own by interacting with their environment through chemical reactions. The platinum coating on the microswimmers reacts to a hydrogen peroxide solution they are placed in, and that propels them through the liquid."
    s = get_score(request.POST.get('Answer', False), source,
                  {'FKGL': (1, 0.4, 'intermediate'),
                   'sentiment': (1, 0.4, 'neutral'),
                   'keyword': (1, 0.2, True),
                   'plagiarism': (0, 0.2, True)})
    print(s)
    user = User(username=request.POST.get('Username', False),
                room=request.POST.get('RoomCode', False), score=s)
    user.save()
    return leaderboard(request)
