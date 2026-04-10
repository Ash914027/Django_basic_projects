from django.urls import path
from . import views

urlpatterns = [
    path('', views.evenodd_checker, name='evenodd_checker'),
]
