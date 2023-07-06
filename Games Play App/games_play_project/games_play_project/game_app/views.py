from django.http import HttpRequest
from games_play_project.profile_app.models import ProfileModel
from .forms import CreateGameModelModelForm, EditGameModelModelForm, DeleteGameModelModelForm
from django.shortcuts import render, redirect
from .models import GameModel


def create_game_func(request: HttpRequest):
    template_name = 'game_app/create-game.html'

    profile_object = ProfileModel.objects.first()

    if request.method == 'POST':

        request_data = request.POST.copy()
        request_data['profile'] = profile_object.pk

        model_form = CreateGameModelModelForm(request_data)

        if model_form.is_valid():
            model_form.save()
            return redirect('dashboard page')

    else:   # request.method == 'GET':
        model_form = CreateGameModelModelForm()

    context = {'profile_object': profile_object,
               'model_form': model_form}

    return render(request, template_name, context)


def details_game_func(request: HttpRequest, pk: int):
    template_name = 'game_app/details-game.html'

    profile_object = ProfileModel.objects.first()
    game_object = GameModel.objects.get(pk=pk)

    context = {'profile_object': profile_object,
               'game_object': game_object}

    return render(request, template_name, context)


def edit_game_func(request: HttpRequest, pk: int):
    template_name = 'game_app/edit-game.html'

    profile_object = ProfileModel.objects.first()
    game_object = GameModel.objects.get(pk=pk)

    if request.method == 'POST':
        model_form = EditGameModelModelForm(request.POST, instance=game_object)

        if model_form.is_valid():
            model_form.save()
            return redirect('dashboard page')

    else:   # request.method == 'GET':
        model_form = EditGameModelModelForm(instance=game_object)

    context = {'profile_object': profile_object,
               'game_object': game_object,
               'model_form': model_form}

    return render(request, template_name, context)


def delete_game_func(request: HttpRequest, pk: int):
    template_name = 'game_app/delete-game.html'

    profile_object = ProfileModel.objects.first()
    game_object = GameModel.objects.get(pk=pk)

    if request.method == 'POST':
        game_object.delete()
        return redirect('dashboard page')

    else:   # request.method == 'GET':
        model_form = DeleteGameModelModelForm(instance=game_object)

    context = {'profile_object': profile_object,
               'game_object': game_object,
               'model_form': model_form}

    return render(request, template_name, context)
