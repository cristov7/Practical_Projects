from django.urls import path
from .views import home_func, dashboard_func

urlpatterns = [
    path('', home_func, name='home page'),
    # •	http://localhost:8000/

    path('dashboard/', dashboard_func, name='dashboard page')
    # •	http://localhost:8000/dashboard/
]
