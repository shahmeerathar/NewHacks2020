from django.shortcuts import render
from django.http import HttpResponse
from .models import User
from django.template import loader


# Create your views here.
def index(request):
    template = loader.get_template('main/room.html')
    return HttpResponse(template.render(request=request))


def user(request):
    template = loader.get_template('main/user.html')
    return HttpResponse(template.render(request=request))


def main(request):
    template = loader.get_template('main/main.html')
    return HttpResponse(template.render(request=request))


def leaderboard(request):
    users = User.objects.order_by('-score')
    template = loader.get_template('main/leaderboard.html')
    context = {
        'users': users,
    }
    return HttpResponse(template.render(context, request))
