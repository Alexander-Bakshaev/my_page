from django.urls import path
from . import views as views_horoscope

urlpatterns = [
    path('<int:zodiac_sign>', views_horoscope.get_zodiac_sign_info_by_number),
    path('<str:zodiac_sign>', views_horoscope.get_zodiac_sign_info, name='horoscope_name'),
]
