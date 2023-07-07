from django.urls import path
from .views import profile_func, edit_profile_func, delete_profile_func

urlpatterns = [
    path('', profile_func, name='profile page'),
    # http://localhost:8000/profile/

    path('edit/', edit_profile_func, name='edit profile page'),
    # http://localhost:8000/profile/edit/

    path('delete/', delete_profile_func, name='delete profile page'),
    # http://localhost:8000/profile/delete/
]
