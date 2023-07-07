from django.http import HttpRequest
from .models import ProfileModel
from django.shortcuts import render, redirect
from .forms import EditProfileModelModelForm, DeleteProfileModelModelForm


def profile_func(request: HttpRequest):
    template_name = 'profile_app/profile.html'

    profile_object = ProfileModel.objects.first()

    context = {'profile_object': profile_object}

    return render(request, template_name, context)


def edit_profile_func(request: HttpRequest):
    template_name = 'profile_app/edit-profile.html'

    profile_object = ProfileModel.objects.first()

    if request.method == 'POST':
        model_form = EditProfileModelModelForm(request.POST, instance=profile_object)

        if model_form.is_valid():
            model_form.save()
            return redirect('profile page')

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

    else:   # request.method == 'GET':
        model_form = DeleteProfileModelModelForm(instance=profile_object)

    context = {'profile_object': profile_object,
               'model_form': model_form}

    return render(request, template_name, context)
