from django.http import HttpRequest
from car_collection_project.profile_app.models import *
from django.shortcuts import render


def index_func(request: HttpRequest):
    template_name = 'car_collection_app/index.html'

    profile_object = ProfileModel.objects.first()

    context = {'profile_object': profile_object}

    return render(request, template_name, context)


def catalogue_func(request: HttpRequest):
    template_name = 'car_collection_app/catalogue.html'

    profile_object = ProfileModel.objects.first()
    all_car_objects = profile_object.carmodel_set.all()

    context = {'profile_object': profile_object,
               'all_car_objects': all_car_objects}

    return render(request, template_name, context)
