from django.urls import path
from . import views

urlpatterns = [
    path('<week_day>', views.get_week_day_info),
]