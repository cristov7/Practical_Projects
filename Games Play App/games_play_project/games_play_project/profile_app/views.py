from django.http import HttpRequest
from .forms import CreateProfileModelModelForm, EditProfileModelModelForm
from django.shortcuts import render, redirect
from .models import ProfileModel


def create_profile_func(request: HttpRequest):
    template_name = 'profile_app/create-profile.html'

    if request.method == 'POST':
        model_form = CreateProfileModelModelForm(request.POST)

        if model_form.is_valid():
            model_form.save()
            return redirect('home page')

    else:   # request.method == 'GET':
        model_form = CreateProfileModelModelForm()

    context = {'model_form': model_form}

    return render(request, template_name, context)


def details_profile_func(request: HttpRequest):
    template_name = 'profile_app/details-profile.html'

    profile_object = ProfileModel.objects.first()
    all_game_objects = profile_object.gamemodel_set.all()

    total_games = all_game_objects.count()

    if total_games:
        total_ranking = sum([game_object.rating for game_object in all_game_objects])
        average_rating = total_ranking / total_games
    else:
        average_rating = '0.0'

    context = {'profile_object': profile_object,
               'total_games': total_games,
               'average_rating': average_rating}

    return render(request, template_name, context)


def edit_profile_func(request: HttpRequest):
    template_name = 'profile_app/edit-profile.html'

    profile_object = ProfileModel.objects.first()

    if request.method == 'POST':
        model_form = EditProfileModelModelForm(request.POST, instance=profile_object)

        if model_form.is_valid():
            model_form.save()
            return redirect('details profile page')

    else:   # request.method == 'GET':
        model_form = EditProfileModelModelForm(instance=profile_object)

    context = {'profile_object': profile_object,
               'model_form': model_form}

    return render(request, template_name, context)


def delete_profile_func(request: HttpRequest):
    template_name = 'profile_app/delete-profile.html'

    profile_object = ProfileModel.objects.first()

    if request.method == 'POST':
        profile_object.delete()
        return redirect('home page')

    context = {'profile_object': profile_object}

    return render(request, template_name, context)
