"""
URL configuration for my_page project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from week_days import views as views_todo_week
from horoscope import views as views_horoscope

urlpatterns = [
    path('horoscope/admin/', admin.site.urls),
    path('horoscope/aries/', views_horoscope.aries),
    path('horoscope/taurus/', views_horoscope.taurus),
    path('horoscope/gemini/', views_horoscope.gemini),
    path('horoscope/cancer/', views_horoscope.cancer),
    path('horoscope/leo/', views_horoscope.leo),
    path('horoscope/virgo/', views_horoscope.virgo),
    path('horoscope/libra/', views_horoscope.libra),
    path('horoscope/scorpio/', views_horoscope.scorpio),
    path('horoscope/sagittarius/', views_horoscope.sagittarius),
    path('horoscope/capricorn/', views_horoscope.capricorn),
    path('horoscope/aquarius/', views_horoscope.aquarius),
    path('horoscope/pisces/', views_horoscope.pisces),
    path('todo_week/mondev', views_todo_week.monday),
    path('todo_week/tuesday', views_todo_week.tuesday),
]
