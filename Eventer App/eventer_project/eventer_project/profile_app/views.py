from django.http import HttpRequest
from .forms import CreateProfileModelModelForm, ProfileModel, EditProfileModelModelForm
from django.shortcuts import render, redirect


def create_profile_func(request: HttpRequest):
    template_name = 'profile_app/profile-create.html'

    if request.method == 'POST':
        model_form = CreateProfileModelModelForm(request.POST)

        if model_form.is_valid():
            model_form.save()

            return redirect('dashboard page')

    else:   # request.method == 'GET':
        model_form = CreateProfileModelModelForm()

    context = {'model_form': model_form}

    return render(request, template_name, context)


def profile_details_func(request: HttpRequest):
    template_name = 'profile_app/profile-details.html'

    profile_object = ProfileModel.objects.first()
    count_event_objects = profile_object.eventmodel_set.count()

    context = {'profile_object': profile_object,
               'count_event_objects': count_event_objects}

    return render(request, template_name, context)


def edit_profile_func(request: HttpRequest):
    template_name = 'profile_app/profile-edit.html'

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


def delete_profile_func(request: HttpRequest):
    template_name = 'profile_app/profile-delete.html'

    profile_object = ProfileModel.objects.first()

    if request.method == 'POST':
        profile_object.delete()

        return redirect('home page')

    context = {'profile_object': profile_object}

    return render(request, template_name, context)
