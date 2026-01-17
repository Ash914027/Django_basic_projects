from django.shortcuts import render, redirect, get_object_or_404
from .models import Todo
from .forms import TodoForm
import datetime
from django.shortcuts import render


def show_date(request):
    today = datetime.date.today()
    context = {
        'today': today
    }
    return render(request, 'todo/show_date.html', context)
def greeting(request):
    context = {"name": "XYZ"}
    return render(request, "todo/greeting.html", context)
def holiday_message(request):
    context = {"is_holiday": True}
    return render(request, "todo/holiday.html", context)

# 4. Uppercase and Lowercase
def city_case(request):
    context = {"city": "Delhi"}
    return render(request, "todo/city.html", context)    

