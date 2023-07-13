from django.urls import path
from .views import *

urlpatterns = [
    path('', home_func, name='home page'),
    # http://localhost:8000/

    path('create/', create_recipe_func, name='create recipe page'),
    # http://localhost:8000/create/

    path('edit/<int:pk>/', edit_recipe_func, name='edit recipe page'),
    # http://localhost:8000/edit/<int:pk>/

    path('delete/<int:pk>/', delete_recipe_func, name='delete recipe page'),
    # http://localhost:8000/delete/<int:pk>/

    path('details/<int:pk>/', recipe_details_func, name='recipe details page')
    # http://localhost:8000/details/<int:pk>/
]
