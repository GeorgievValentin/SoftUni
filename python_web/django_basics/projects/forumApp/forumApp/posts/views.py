from datetime import datetime

from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    context = {
        "current_time": datetime.now(),
    }

    return render(request, "base.html", context)


def dashboard(request):
    context = {
        "posts": [
            {
                "title": "How to become a junior developer?",
                "author": "",
                "content": "I am still working on it, when I become, will tell **you**!",
                "date": datetime.now(),
            },
            {
                "title": "How to become a senior developer?",
                "author": "Valentin Georgiev",
                "content": "",
                "date": datetime.now(),
            },
            {
                "title": "How to become a master developer?",
                "author": "Valentin Georgiev",
                "content": "### I am still working on it, when I become, will tell you!",
                "date": datetime.now(),
            },
        ]
    }

    return render(request, "posts/dashboard.html", context)