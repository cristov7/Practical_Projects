from django.http import HttpRequest
from .forms import *
from django.shortcuts import render, redirect
from my_plant_project.my_plant_app.models import *


def profile_create_func(request: HttpRequest):
    template_name = 'profile_app/create-profile.html'

    if request.method == 'POST':
        model_form = CreateProfileModelModelForm(request.POST)

        if model_form.is_valid():
            model_form.save()
            return redirect('catalogue')

    else:   # request.method == 'GET':
        model_form = CreateProfileModelModelForm()

    context = {'model_form': model_form}

    return render(request, template_name, context)


def profile_details_func(request: HttpRequest):
    template_name = 'profile_app/profile-details.html'

    profile_object = ProfileModel.objects.first()
    all_plant_objects = profile_object.plantmodel_set.all()

    context = {'profile_object': profile_object,
               'all_plant_objects': all_plant_objects}

    return render(request, template_name, context)


def profile_edit_func(request: HttpRequest):
    template_name = 'profile_app/edit-profile.html'

    profile_object = ProfileModel.objects.first()

    if request.method == 'POST':
        model_form = EditProfileModelModelForm(request.POST, instance=profile_object)

        if model_form.is_valid():
            model_form.save()
            return redirect('profile details page')

    else:   # request.method == 'GET':
        model_form = EditProfileModelModelForm(instance=profile_object)

    context = {'profile_object': profile_object,
               'model_form': model_form}

    return render(request, template_name, context)


def profile_delete_func(request: HttpRequest):
    template_name = 'profile_app/delete-profile.html'

    profile_object = ProfileModel.objects.first()

    if request.method == 'POST':
        profile_object.delete()
        return redirect('home page')

    context = {'profile_object': profile_object}

    return render(request, template_name, context)
