from django.urls import path
from .views import *

urlpatterns = [
    path('create/', profile_create_func, name='profile create page'),
    # http://localhost:8000/profile/create/

    path('details/', profile_details_func, name='profile details page'),
    # http://localhost:8000/profile/details/

    path('edit/', profile_edit_func, name='profile edit page'),
    # http://localhost:8000/profile/edit/

    path('delete/', profile_delete_func, name='profile delete page')
    # http://localhost:8000/profile/delete/
]
