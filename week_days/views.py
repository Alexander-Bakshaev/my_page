from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def monday(request):
    return HttpResponse("Понедельник")


def tuesday(request):
    return HttpResponse("Вторник")
