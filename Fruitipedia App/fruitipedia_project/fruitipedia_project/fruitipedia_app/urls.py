from django.urls import path
from .views import index_func, dashboard_func

urlpatterns = [
    path('', index_func, name='index page'),
    # http://localhost:8000/

    path('dashboard/', dashboard_func, name='dashboard page')
    # http://localhost:8000/dashboard/
]
