from django.urls import path
from .views import fruit_create_func, fruit_details_func, fruit_edit_func, fruit_delete_func

urlpatterns = [
    path('create/', fruit_create_func, name='fruit create page'),
    # http://localhost:8000/create/

    path('<int:pk>/details/', fruit_details_func, name='fruit details page'),
    # http://localhost:8000/<int:pk>/details/

    path('<int:pk>/edit/', fruit_edit_func, name='fruit edit page'),
    # http://localhost:8000/<int:pk>/edit/

    path('<int:pk>/delete/', fruit_delete_func, name='fruit delete page')
    # http://localhost:8000/<int:pk>/delete/
]
