from django.urls import path
from . import views

urlpatterns = [
    path('monday/', views.monday, name='monday'),
    path('tuesday/', views.tuesday, name='tuesday'),
    path('wednesday/', views.wednesday, name='wednesday'),
    path("cities/", views.city_view, name="city_view"),
    path("products/", views.product_list, name="product_list"),

]
