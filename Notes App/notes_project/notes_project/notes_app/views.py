from django.http import HttpRequest
from .models import *
from .forms import *
from django.shortcuts import render, redirect


def home_func(request: HttpRequest):
    template_name = 'notes_app/'

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

        context['model_form'] = model_form

    else:
        template_name += 'home-with-profile.html'

        note_objects_all = profile_object.notemodel_set.all()
        context['note_objects_all'] = note_objects_all

    return render(request, template_name, context)


def add_note_func(request: HttpRequest):
    template_name = 'notes_app/note-create.html'

    profile_object = ProfileModel.objects.first()
    context = {'profile_object': profile_object}

    if request.method == 'POST':
        request_method = request.POST.copy()
        request_method['profile'] = profile_object.pk

        model_form = AddNoteModelModelForm(request_method)

        if model_form.is_valid():
            model_form.save()
            return redirect('home page')

    else:   # request.method == 'GET':
        model_form = AddNoteModelModelForm()

    context['model_form'] = model_form

    return render(request, template_name, context)


def edit_note_func(request: HttpRequest, pk: int):
    template_name = 'notes_app/note-edit.html'

    profile_object = ProfileModel.objects.first()
    note_object = NoteModel.objects.get(pk=pk)

    context = {'profile_object': profile_object,
               'note_object': note_object}

    if request.method == 'POST':
        model_form = EditNoteModelModelForm(request.POST, instance=note_object)

        if model_form.is_valid():
            model_form.save()
            return redirect('home page')

    else:   # request.method == 'GET':
        model_form = EditNoteModelModelForm(instance=note_object)

    context['model_form'] = model_form

    return render(request, template_name, context)


def delete_note_func(request: HttpRequest, pk: int):
    template_name = 'notes_app/note-delete.html'

    profile_object = ProfileModel.objects.first()
    note_object = NoteModel.objects.get(pk=pk)

    context = {'profile_object': profile_object,
               'note_object': note_object}

    if request.method == 'POST':
        note_object.delete()
        return redirect('home page')

    else:   # request.method == 'GET':
        model_form = DeleteNoteModelModelForm(instance=note_object)
        context['model_form'] = model_form

    return render(request, template_name, context)


def note_details_func(request: HttpRequest, pk: int):
    template_name = 'notes_app/note-details.html'

    profile_object = ProfileModel.objects.first()
    note_object = NoteModel.objects.get(pk=pk)

    context = {'profile_object': profile_object,
               'note_object': note_object}

    return render(request, template_name, context)


def profile_func(request: HttpRequest):
    template_name = 'notes_app/profile.html'

    profile_object = ProfileModel.objects.first()
    note_objects_all = profile_object.notemodel_set.all()

    context = {'profile_object': profile_object,
               'note_objects_all': note_objects_all}

    return render(request, template_name, context)


def profile_delete_func(request: HttpRequest):
    profile_object = ProfileModel.objects.first()
    profile_object.delete()
    return redirect('home page')
