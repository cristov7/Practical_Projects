from django.http import HttpRequest
from .models import ProfileModel, FruitModel
from .forms import CreateFruitModelModelForm, EditFruitModelModelForm, DeleteFruitModelModelForm
from django.shortcuts import render, redirect


def fruit_create_func(request: HttpRequest):
    template_name = 'fruit_app/create-fruit.html'

    profile_object = ProfileModel.objects.first()

    if request.method == 'POST':
        request_post = request.POST.copy()
        request_post['profile'] = profile_object.pk

        model_form = CreateFruitModelModelForm(request_post)

        if model_form.is_valid():
            model_form.save()

            return redirect('dashboard page')

    else:   # request.method == 'GET':
        model_form = CreateFruitModelModelForm()

    context = {'profile_object': profile_object,
               'model_form': model_form}

    return render(request, template_name, context)


def fruit_details_func(request: HttpRequest, pk: int):
    template_name = 'fruit_app/details-fruit.html'

    profile_object = ProfileModel.objects.first()
    fruit_object = FruitModel.objects.get(pk=pk)

    context = {'profile_object': profile_object,
               'fruit_object': fruit_object}

    return render(request, template_name, context)


def fruit_edit_func(request: HttpRequest, pk: int):
    template_name = 'fruit_app/edit-fruit.html'

    profile_object = ProfileModel.objects.first()
    fruit_object = FruitModel.objects.get(pk=pk)

    if request.method == 'POST':
        model_form = EditFruitModelModelForm(request.POST, instance=fruit_object)

        if model_form.is_valid():
            model_form.save()

            return redirect('dashboard page')

    else:   # request.method == 'GET':
        model_form = EditFruitModelModelForm(instance=fruit_object)

    context = {'profile_object': profile_object,
               'fruit_object': fruit_object,
               'model_form': model_form}

    return render(request, template_name, context)


def fruit_delete_func(request: HttpRequest, pk: int):
    template_name = 'fruit_app/delete-fruit.html'

    profile_object = ProfileModel.objects.first()
    fruit_object = FruitModel.objects.get(pk=pk)

    if request.method == 'POST':
        fruit_object.delete()

        return redirect('dashboard page')

    else:   # request.method == 'GET':
        model_form = DeleteFruitModelModelForm(instance=fruit_object)

    context = {'profile_object': profile_object,
               'fruit_object': fruit_object,
               'model_form': model_form}

    return render(request, template_name, context)
