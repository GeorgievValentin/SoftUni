import datetime
import random

from django.shortcuts import render


class Person:
    def __init__(self, first_name, last_name, age=None):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"


def index(request):
    context = {
        "title": "Employees list",

        "person_dict": {
            "first_name": "Valio",
            "last_name": "Georgiev",
        },

        "person_obj": Person("Valio", "Georgiev"),

        "names": ["Valio", "Kolyo", "Stamat", "Kircho", "Unufry"],
        "ages": [random.randrange(1, 100) for _ in range(10)],
        "empty_ages": [],

        "date": datetime.date.today(),
        "get_params": request.GET,
    }

    return render(request, "employees/index.html", context)


def employee_details(request, pk):
    context = {
        "pk": pk,
    }
    return render(request, "employees/employees.html", context)
