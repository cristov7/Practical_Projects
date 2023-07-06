from django.urls import path
from .views import create_game_func, details_game_func, edit_game_func, delete_game_func

urlpatterns = [
    path('create/', create_game_func, name='create game page'),
    # http://localhost:8000/game/create/

    path('details/<int:pk>/', details_game_func, name='details game page'),
    # http://localhost:8000/game/details/<int:pk>/

    path('edit/<int:pk>/', edit_game_func, name='edit game page'),
    # http://localhost:8000/game/edit/<int:pk>/

    path('delete/<int:pk>/', delete_game_func, name='delete game page')
    # http://localhost:8000/game/delete/<int:pk>/
]
