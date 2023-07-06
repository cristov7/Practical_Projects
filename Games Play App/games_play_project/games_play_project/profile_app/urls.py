from django.urls import path
from .views import create_profile_func, details_profile_func, edit_profile_func, delete_profile_func

urlpatterns = [
    path('create/', create_profile_func, name='create profile page'),
    # http://localhost:8000/profile/create/

    path('details/', details_profile_func, name='details profile page'),
    # http://localhost:8000/profile/details/

    path('edit/', edit_profile_func, name='edit profile page'),
    # http://localhost:8000/profile/edit/

    path('delete/', delete_profile_func, name='delete profile page')
    # http://localhost:8000/profile/delete/
]
