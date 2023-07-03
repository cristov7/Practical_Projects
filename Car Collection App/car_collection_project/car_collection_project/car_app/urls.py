from django.urls import path
from .views import *

urlpatterns = [
    path('create/', car_create_func, name='car create page'),
    # http://localhost:8000/car/create/

    path('<int:car_id>/details/', car_details_func, name='car details page'),
    # http://localhost:8000/car/<int:car_id>/details/

    path('<int:car_id>/edit/', car_edit_func, name='car edit page'),
    # http://localhost:8000/car/<int:car_id>/edit/

    path('<int:car_id>/delete/', car_delete_func, name='car delete page'),
    # http://localhost:8000/car/<int:car_id>/delete/
]
