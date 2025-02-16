from django.http import HttpResponse, HttpResponseNotFound

def get_rectangle_area(request, width: int, height: int) -> HttpResponse:
    return HttpResponse(f"Площадь прямоугольника {width} * {height} = {width * height}")

def get_square_area(request, width: int) -> HttpResponse:
    return HttpResponse(f"Площадь квадрата {width} * {width} = {width * width}")

def get_circle_area(request, radius: int) -> HttpResponse:
    return HttpResponse(f"Площадь круга {radius} * {radius} * {3.14} = {radius * radius * 3.14}")

