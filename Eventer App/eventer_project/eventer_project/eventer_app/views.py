from django.http import HttpRequest
from eventer_project.profile_app.models import ProfileModel
from django.shortcuts import render


def home_func(request: HttpRequest):
    template_name = 'eventer_app/home-page.html'

    profile_object = ProfileModel.objects.first()

    context = {'profile_object': profile_object}

    return render(request, template_name, context)


def dashboard_func(request: HttpRequest):
    template_name = 'eventer_app/dashboard.html'

    profile_object = ProfileModel.objects.first()
    all_event_objects = profile_object.eventmodel_set.all()

    context = {'profile_object': profile_object,
               'all_event_objects': all_event_objects}

    return render(request, template_name, context)
