import datetime
from datetime import datetime

from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return HttpResponse(f"Response from {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")


def index2(request, *args, **kwargs):
    return HttpResponse(f"Response with {args} and {kwargs}")


def department_1_details(request):
    return HttpResponse("Department 1")


def department_2_details(request):
    return HttpResponse("Department 2")


def department_details_by_id(request, pk):
    return HttpResponse(f"Department with ID: {pk}")


def department_details_by_name(request, name):
    return HttpResponse(f"Department with name: {name}")
