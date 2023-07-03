from django.http import HttpRequest
from .models import *
from .forms import *
from django.shortcuts import render, redirect


def profile_create_func(request: HttpRequest):
    template_name = 'profile_app/profile-create.html'

    if request.method == 'POST':
        model_form = CreateProfileModelModelForm(request.POST)

        if model_form.is_valid():
            model_form.save()
            return redirect('catalogue page')

    else:   # request.method == 'GET':
        model_form = CreateProfileModelModelForm()

    context = {'model_form': model_form}

    return render(request, template_name, context)


def profile_details_func(request: HttpRequest):
    template_name = 'profile_app/profile-details.html'

    profile_object = ProfileModel.objects.first()
    all_car_objects = profile_object.carmodel_set.all()

    total_price_of_all_cars = sum([car_object.price for car_object in all_car_objects])

    context = {'profile_object': profile_object,
               'all_car_objects': all_car_objects,
               'total_price_of_all_cars': total_price_of_all_cars}

    return render(request, template_name, context)


def profile_edit_func(request: HttpRequest):
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


def profile_delete_func(request: HttpRequest):
    template_name = 'profile_app/profile-delete.html'

    profile_object = ProfileModel.objects.first()

    if request.method == 'POST':
        profile_object.delete()
        return redirect('index page')

    context = {'profile_object': profile_object}

    return render(request, template_name, context)
