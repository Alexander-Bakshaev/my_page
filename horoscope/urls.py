from django.urls import path
from . import views as views_horoscope

urlpatterns = [
    path('<zodiac_sign>', views_horoscope.get_zodiac_sign_info),
]
