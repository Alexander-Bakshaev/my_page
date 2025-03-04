from django.urls import path
from . import views

urlpatterns = [
    path('rectangle/<int:width>/<int:height>', views.get_rectangle_area),
    path('square/<int:width>', views.get_square_area),
    path('circle/<int:radius>', views.get_circle_area),
    path('get_rectangle_area/<int:width>/<int:height>', views.get_rectangle_area_redirect, name='rectangle'),
    path('get_square_area/<int:width>', views.get_square_area_redirect, name='square'),
    path('gat_circle_area/<int:radius>', views.get_circle_area_redirect, name='circle'),
]
