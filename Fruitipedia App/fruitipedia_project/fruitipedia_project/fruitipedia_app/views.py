from django.http import HttpRequest
from fruitipedia_project.profile_app.models import ProfileModel
from django.shortcuts import render


def index_func(request: HttpRequest):
    template_name = 'fruitipedia_app/index.html'

    profile_object = ProfileModel.objects.first()

    context = {'profile_object': profile_object}

    return render(request, template_name, context)


def dashboard_func(request: HttpRequest):
    template_name = 'fruitipedia_app/dashboard.html'

    profile_object = ProfileModel.objects.first()
    all_fruit_objects = profile_object.fruitmodel_set.all()

    context = {'profile_object': profile_object,
               'all_fruit_objects': all_fruit_objects}

    return render(request, template_name, context)
