from django.urls import path
from .views import create_event_func, event_details_func, edit_event_func, delete_event_func

urlpatterns = [
    path('create/', create_event_func, name='create event page'),
    # http://localhost:8000/create/

    path('details/<int:pk>/', event_details_func, name='event details page'),
    # http://localhost:8000/details/<int:pk>/

    path('edit/<int:pk>/', edit_event_func, name='edit event page'),
    # http://localhost:8000/edit/<int:pk>/

    path('delete/<int:pk>/', delete_event_func, name='delete event page')
    # http://localhost:8000/delete/<int:pk>/
]
