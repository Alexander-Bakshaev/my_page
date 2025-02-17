from django.http import HttpResponse, HttpResponseRedirect, HttpResponseNotFound
from django.urls import reverse

def get_rectangle_area(request, width: int, height: int) -> HttpResponse:
    return HttpResponse(f"Площадь прямоугольника {width} * {height} = {width * height}")

def get_square_area(request, width: int) -> HttpResponse:
    return HttpResponse(f"Площадь квадрата {width} * {width} = {width * width}")

def get_circle_area(request, radius: int) -> HttpResponse:
    return HttpResponse(f"Площадь круга {radius} * {radius} * {3.14} = {radius * radius * 3.14}")

def get_rectangle_area_redirect(request, width: int, height: int) -> HttpResponse:
    """Перенаправление на rectangle"""
    redirect_url = reverse("rectangle", args=(width, height))
    return HttpResponseRedirect(redirect_url)

def get_square_area_redirect(request, width: int) -> HttpResponse:
    """Перенаправление на square"""
    redirect_url = reverse("square", args=(width,))
    return HttpResponseRedirect(redirect_url)

def get_circle_area_redirect(request, radius: int) -> HttpResponse:
    """Перенаправление на circle"""
    redirect_url = reverse("circle", args=(radius,))
    return HttpResponseRedirect(redirect_url)