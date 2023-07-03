from django.http import HttpRequest
from car_collection_project.profile_app.models import *
from .forms import *
from django.shortcuts import render, redirect


def car_create_func(request: HttpRequest):
    template_name = 'car_app/car-create.html'

    profile_object = ProfileModel.objects.first()

    if request.method == 'POST':
        request_post = request.POST.copy()
        request_post['profile'] = profile_object.pk

        model_form = CreateCarModelModelForm(request_post)

        if model_form.is_valid():
            model_form.save()
            return redirect('catalogue page')

    else:   # request.method == 'GET':
        model_form = CreateCarModelModelForm()

    context = {'profile_object': profile_object,
               'model_form': model_form}

    return render(request, template_name, context)


def car_details_func(request: HttpRequest, car_id: int):
    template_name = 'car_app/car-details.html'

    profile_object = ProfileModel.objects.first()
    car_object = CarModel.objects.get(pk=car_id)

    context = {'profile_object': profile_object,
               'car_object': car_object}

    return render(request, template_name, context)


def car_edit_func(request: HttpRequest, car_id: int):
    template_name = 'car_app/car-edit.html'

    profile_object = ProfileModel.objects.first()
    car_object = CarModel.objects.get(pk=car_id)

    if request.method == 'POST':
        model_form = EditCarModelModelForm(request.POST, instance=car_object)

        if model_form.is_valid():
            model_form.save()
            return redirect('catalogue page')

    else:   # request.method == 'GET':
        model_form = EditCarModelModelForm(instance=car_object)

    context = {'profile_object': profile_object,
               'car_object': car_object,
               'model_form': model_form}

    return render(request, template_name, context)


def car_delete_func(request: HttpRequest, car_id: int):
    template_name = 'car_app/car-delete.html'

    profile_object = ProfileModel.objects.first()
    car_object = CarModel.objects.get(pk=car_id)

    if request.method == 'POST':
        car_object.delete()
        return redirect('catalogue page')

    else:   # request.method == 'GET':
        model_form = DeleteCarModelModelForm(instance=car_object)

    context = {'profile_object': profile_object,
               'car_object': car_object,
               'model_form': model_form}

    return render(request, template_name, context)
