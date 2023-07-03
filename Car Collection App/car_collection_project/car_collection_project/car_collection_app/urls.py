from django.urls import path
from .views import *

urlpatterns = [
    path('', index_func, name='index page'),
    # http://localhost:8000/

    path('catalogue/', catalogue_func, name='catalogue page')
    # http://localhost:8000/catalogue/
]
