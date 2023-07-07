from django.http import HttpRequest
from .models import ProfileModel
from online_library_project.profile_app.forms import CreateProfileModelModelForm
from django.shortcuts import render, redirect
from .forms import AddBookModelModelForm, EditBookModelModelForm
from online_library_project.online_library_app.models import BookModel


def home_func(request: HttpRequest):
    template_name = 'online_library_app/'

    profile_object = ProfileModel.objects.first()
    context = {'profile_object': profile_object}

    if not profile_object:
        template_name += 'home-no-profile.html'

        if request.method == 'POST':
            model_form = CreateProfileModelModelForm(request.POST)

            if model_form.is_valid():
                model_form.save()
                return redirect('home page')

        else:   # request.method == 'GET':
            model_form = CreateProfileModelModelForm()

    else:
        template_name += 'home-with-profile.html'

        all_book_objects = profile_object.bookmodel_set.all()
        context['all_book_objects'] = all_book_objects

        model_form = None

    context['model_form'] = model_form

    return render(request, template_name, context)


def add_book_func(request: HttpRequest):
    template_name = 'online_library_app/add-book.html'

    profile_object = ProfileModel.objects.first()

    if request.method == 'POST':
        request_post = request.POST.copy()
        request_post['profile'] = profile_object.pk

        model_form = AddBookModelModelForm(request_post)

        if model_form.is_valid():
            model_form.save()
            return redirect('home page')

    else:   # request.method == 'GET':
        model_form = AddBookModelModelForm()

    context = {'profile_object': profile_object,
               'model_form': model_form}

    return render(request, template_name, context)


def edit_book_func(request: HttpRequest, pk: int):
    template_name = 'online_library_app/edit-book.html'

    profile_object = ProfileModel.objects.first()
    book_object = BookModel.objects.get(pk=pk)

    if request.method == 'POST':
        model_form = EditBookModelModelForm(request.POST, instance=book_object)

        if model_form.is_valid():
            model_form.save()
            return redirect('home page')

    else:   # request.method == 'GET':
        model_form = EditBookModelModelForm(instance=book_object)

    context = {'profile_object': profile_object,
               'book_object': book_object,
               'model_form': model_form}

    return render(request, template_name, context)


def book_details_func(request: HttpRequest, pk: int):
    template_name = 'online_library_app/book-details.html'

    profile_object = ProfileModel.objects.first()
    book_object = BookModel.objects.get(pk=pk)

    context = {'profile_object': profile_object,
               'book_object': book_object}

    return render(request, template_name, context)


def delete_book_func(request: HttpRequest, pk: int):
    book_object = BookModel.objects.get(pk=pk)
    book_object.delete()
    return redirect('home page')
