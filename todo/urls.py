

from django.urls import path
from . import views

urlpatterns = [
    
     path('date/', views.show_date, name='show_date'),
     path('greet/', views.greeting, name='greet'),
     path('holiday/', views.holiday_message, name='holiday'),
    path('city/', views.city_case, name='city'),
]

