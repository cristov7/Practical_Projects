from django.http import HttpRequest
from games_play_project.profile_app.models import ProfileModel
from games_play_project.game_app.models import GameModel
from django.shortcuts import render


def home_func(request: HttpRequest):
    template_name = 'games_play_app/home-page.html'

    profile_object = ProfileModel.objects.first()

    context = {'profile_object': profile_object}

    return render(request, template_name, context)


def dashboard_func(request: HttpRequest):
    template_name = 'games_play_app/dashboard.html'

    profile_object = ProfileModel.objects.first()
    all_game_objects = GameModel.objects.all()

    context = {'profile_object': profile_object,
               'all_game_objects': all_game_objects}

    return render(request, template_name, context)
