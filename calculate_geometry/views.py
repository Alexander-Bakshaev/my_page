from django.http import HttpResponse, HttpResponseRedirect, HttpResponseNotFound

def get_rectangle_area(request, width: int, height: int) -> HttpResponse:
    return HttpResponse(f"Площадь прямоугольника {width} * {height} = {width * height}")

def get_square_area(request, width: int) -> HttpResponse:
    return HttpResponse(f"Площадь квадрата {width} * {width} = {width * width}")

def get_circle_area(request, radius: int) -> HttpResponse:
    return HttpResponse(f"Площадь круга {radius} * {radius} * {3.14} = {radius * radius * 3.14}")

def get_rectangle_area_redirect(request, width: int, height: int) -> HttpResponse:
    """Перенаправление на rectangle"""
    return HttpResponseRedirect(f"/calculate_geometry/rectangle/{width}/{height}")

def get_square_area_redirect(request, width: int) -> HttpResponse:
    """Перенаправление на square"""
    return HttpResponseRedirect(f"/calculate_geometry/square/{width}")

def get_circle_area_redirect(request, radius: int) -> HttpResponse:
    """Перенаправление на circle"""
    return HttpResponseRedirect(f"/calculate_geometry/circle/{radius}")