from django.http import HttpRequest
from .models import *
from django.shortcuts import render, redirect
from .forms import *


def home_func(request: HttpRequest):
    template_name = 'recipes_app/index.html'

    all_recipe_objects = RecipeModel.objects.all()

    context = {'all_recipe_objects': all_recipe_objects}

    return render(request, template_name, context)


def create_recipe_func(request: HttpRequest):
    template_name = 'recipes_app/create.html'

    if request.method == 'POST':
        model_form = CreateRecipeModelModelForm(request.POST)

        if model_form.is_valid():
            model_form.save()
            return redirect('home page')

    else:   # request.method == 'GET':
        model_form = CreateRecipeModelModelForm()

    context = {'model_form': model_form}

    return render(request, template_name, context)


def edit_recipe_func(request: HttpRequest, pk: int):
    template_name = 'recipes_app/edit.html'

    recipe_object = RecipeModel.objects.get(pk=pk)

    if request.method == 'POST':
        model_form = EditRecipeModelModelForm(request.POST, instance=recipe_object)

        if model_form.is_valid():
            model_form.save()
            return redirect('home page')

    else:  # request.method == 'GET':
        model_form = EditRecipeModelModelForm(instance=recipe_object)

    context = {'model_form': model_form}

    return render(request, template_name, context)


def delete_recipe_func(request: HttpRequest, pk: int):
    template_name = 'recipes_app/delete.html'

    recipe_object = RecipeModel.objects.get(pk=pk)

    if request.method == 'POST':
        recipe_object.delete()
        return redirect('home page')

    else:  # request.method == 'GET':
        model_form = DeleteRecipeModelModelForm(instance=recipe_object)

    context = {'model_form': model_form}

    return render(request, template_name, context)


def recipe_details_func(request: HttpRequest, pk: int):
    template_name = 'recipes_app/details.html'

    recipe_object = RecipeModel.objects.get(pk=pk)
    ingredients_list = recipe_object.ingredients.split(', ')

    context = {'recipe_object': recipe_object,
               'ingredients_list': ingredients_list}

    return render(request, template_name, context)
