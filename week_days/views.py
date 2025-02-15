from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def monday(request):
    return HttpResponse("Понедельник")


def tuesday(request):
    return HttpResponse("Вторник")

def wednesday(request):
    return HttpResponse("Среда")

def thursday(request):
    return HttpResponse("Четверг")

def friday(request):
    return HttpResponse("Пятница")

def saturday(request):
    return HttpResponse("Суббота")

def sunday(request):
    return HttpResponse("Воскресенье")
