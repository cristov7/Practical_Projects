from django.http import HttpRequest
from my_plant_project.profile_app.models import *
from django.shortcuts import render, redirect
from .forms import *


def home_func(request: HttpRequest):
    template_name = 'my_plant_app/home-page.html'

    profile_object = ProfileModel.objects.first()

    context = {'profile_object': profile_object}

    return render(request, template_name, context)


def catalogue_func(request: HttpRequest):
    template_name = 'my_plant_app/catalogue.html'

    profile_object = ProfileModel.objects.first()
    all_plant_objects = profile_object.plantmodel_set.all()

    context = {'profile_object': profile_object,
               'all_plant_objects': all_plant_objects}

    return render(request, template_name, context)


def plant_create_func(request: HttpRequest):
    template_name = 'my_plant_app/create-plant.html'

    profile_object = ProfileModel.objects.first()

    if request.method == 'POST':
        data = request.POST.copy()
        data['profile'] = profile_object.pk

        model_form = CreatePlantModelModelForm(data)

        if model_form.is_valid():
            model_form.save()
            return redirect('catalogue')

    else:   # request.method == 'GET':
        model_form = CreatePlantModelModelForm()

    context = {'profile_object': profile_object,
               'model_form': model_form}

    return render(request, template_name, context)


def plant_details_func(request: HttpRequest, plant_id: int):
    template_name = 'my_plant_app/plant-details.html'

    profile_object = ProfileModel.objects.first()
    plant_object = PlantModel.objects.get(pk=plant_id)

    context = {'profile_object': profile_object,
               'plant_object': plant_object}

    return render(request, template_name, context)


def plant_edit_func(request: HttpRequest, plant_id: int):
    template_name = 'my_plant_app/edit-plant.html'

    profile_object = ProfileModel.objects.first()
    plant_object = PlantModel.objects.get(pk=plant_id)

    if request.method == 'POST':
        model_form = EditPlantModelModelForm(request.POST, instance=plant_object)

        if model_form.is_valid():
            model_form.save()

            return redirect('catalogue')

    else:   # request.method == 'GET':
        model_form = EditPlantModelModelForm(instance=plant_object)

    context = {'profile_object': profile_object,
               'plant_object': plant_object,
               'model_form': model_form}

    return render(request, template_name, context)


def plant_delete_func(request: HttpRequest, plant_id: int):
    template_name = 'my_plant_app/delete-plant.html'

    profile_object = ProfileModel.objects.first()
    plant_object = PlantModel.objects.get(pk=plant_id)

    if request.method == 'POST':
        plant_object.delete()
        return redirect('catalogue')

    context = {'profile_object': profile_object,
               'plant_object': plant_object,
               'model_form': DeletePlantModelModelForm(instance=plant_object)}

    return render(request, template_name, context)
