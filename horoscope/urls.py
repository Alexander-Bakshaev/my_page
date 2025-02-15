from django.urls import path
from . import views as views_horoscope

urlpatterns = [
    path('<zodiac_sign>', views_horoscope.get_zodiac_sign_info),
    # path('taurus/', views_horoscope.taurus),
    # path('gemini/', views_horoscope.gemini),
    # path('cancer/', views_horoscope.cancer),
    # path('leo/', views_horoscope.leo),
    # path('virgo/', views_horoscope.virgo),
    # path('libra/', views_horoscope.libra),
    # path('scorpio/', views_horoscope.scorpio),
    # path('sagittarius/', views_horoscope.sagittarius),
    # path('capricorn/', views_horoscope.capricorn),
    # path('aquarius/', views_horoscope.aquarius),
    # path('pisces/', views_horoscope.pisces),
]