from django.urls import path
from .views import home_func, add_book_func, edit_book_func, book_details_func, delete_book_func

urlpatterns = [
    path('', home_func, name='home page'),
    # http://localhost:8000/

    path('add/', add_book_func, name='add book page'),
    # http://localhost:8000/add/

    path('edit/<int:pk>/', edit_book_func, name='edit book page'),
    # http://localhost:8000/edit/<int:pk>/

    path('details/<int:pk>/', book_details_func, name='book details page'),
    # http://localhost:8000/details/<int:pk>/

    path('delete/<int:pk>/', delete_book_func, name='delete book page')
    # http://localhost:8000/delete/<int:pk>/
]
