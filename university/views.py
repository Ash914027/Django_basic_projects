from django.shortcuts import render

# Create your views here.
from datetime import datetime

from django.shortcuts import render

def monday(request):
    classes = [
        {"time": "9:00 - 10:00 AM", "subject": "Math"},
        {"time": "10:15 - 11:15 AM", "subject": "Physics"},
        {"time": "11:30 - 12:30 PM", "subject": "Computer Science"},
    ]
    return render(request, "university/monday.html", {"day": "Monday", "classes": classes})


def tuesday(request):
    classes = [
        {"time": "9:00 - 10:00 AM", "subject": "English"},
        {"time": "10:15 - 11:15 AM", "subject": "Biology"},
        {"time": "11:30 - 12:30 PM", "subject": "History"},
    ]
    return render(request, "university/tuesday.html", {"day": "Tuesday", "classes": classes})


def wednesday(request):
    classes = [
        {"time": "9:00 - 10:00 AM", "subject": "Chemistry"},
        {"time": "10:15 - 11:15 AM", "subject": "Mathematics"},
        {"time": "11:30 - 12:30 PM", "subject": "Literature"},
    ]
    return render(request, "university/wednesday.html", {"day": "Wednesday", "classes": classes})


def city_view(request):
    cities = ["Delhi", "Mumbai", "Chennai"]
    name = "xyz"
    students = [
        {"name": "Rahul", "marks": 95},
        {"name": "Priya", "marks": 48},
        {"name": "Karan", "marks": 76},
    ]
    today = datetime.now()

    return render(request, "university/city_template.html", {
        "cities": cities,
        "name": name,
        "students": students,
        "today": today
    })
def product_list(request):
    products = [
        {"name": "Notebook", "price": 15, "category": "Stationery"},
        {"name": "Laptop", "price": 750, "category": "Electronics"},
        {"name": "Pen", "price": 5, "category": "Stationery"},
        {"name": "Headphones", "price": 40, "category": "Electronics"},
        {"name": "Mug", "price": 12, "category": "Kitchen"},
    ]
    return render(request, "university/products.html", {"products": products})

