from django.urls import path
from .views import *

urlpatterns = [
    path('', home_func, name='home page'),
    # http://localhost:8000/

    path('add/', add_note_func, name='add note page'),
    # http://localhost:8000/add/

    path('edit/<int:pk>/', edit_note_func, name='edit note page'),
    # http://localhost:8000/edit/<int:pk>/

    path('delete/<int:pk>/', delete_note_func, name='delete note page'),
    # http://localhost:8000/delete/<int:pk>/

    path('details/<int:pk>/', note_details_func, name='note details page'),
    # http://localhost:8000/details/<int:pk>/

    path('profile/', profile_func, name='profile page'),
    # http://localhost:8000/profile/

    path('profile-delete/', profile_delete_func, name='profile delete page'),
    # http://localhost:8000/profile-delete/
]
