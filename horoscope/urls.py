from django.urls import path
from . import views as views_horoscope

urlpatterns = [
    path('', views_horoscope.index),
    path('type', views_horoscope.get_elements, name='elements'),
    path('type/<str:element>', views_horoscope.get_tipe_elements, name='element'),
    path('<int:zodiac_sign>', views_horoscope.get_zodiac_sign_info_by_number),
    path('<str:zodiac_sign>', views_horoscope.get_zodiac_sign_info, name='horoscope_name'),
    path('<int:month>/<int:day>/', views_horoscope.get_zodiac_by_date, name='zodiac_by_date'),
]