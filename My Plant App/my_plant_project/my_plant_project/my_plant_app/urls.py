from django.urls import path
from .views import *

urlpatterns = [
    path('', home_func, name='home page'),
    # http://localhost:8000/

    path('catalogue/', catalogue_func, name='catalogue'),
    # http://localhost:8000/catalogue/

    path('create/', plant_create_func, name='plant create page'),
    # http://localhost:8000/create/

    path('details/<int:plant_id>/', plant_details_func, name='plant details page'),
    # http://localhost:8000/details/<int:plant_id>/

    path('edit/<int:plant_id>/', plant_edit_func, name='plant edit page'),
    # http://localhost:8000/edit/<int:plant_id>/

    path('delete/<int:plant_id>/', plant_delete_func, name='plant delete page')
    # http://localhost:8000/delete/<int:plant_id>/
]
