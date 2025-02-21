from django.http import HttpResponse, HttpResponseRedirect, HttpResponseNotFound
from django.urls import reverse
from django.shortcuts import render

def get_rectangle_area(request, width, height):
    context = {
        "width": width,
        "height": height,
        "area": width * height
    }
    return render(request, "calculate_geometry/rectangle.html", context=context)

def get_square_area(request, width):
    context = {
        "width": width,
        "area": width * width
    }
    return render(request, "calculate_geometry/square.html", context=context)

def get_circle_area(request, radius) :
    context = {
        "radius": radius,
        "area": radius * radius * 3.14
    }
    return render(request, "calculate_geometry/circle.html", context=context)

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