from django.urls import path
from . import views

urlpatterns = [
    path('<int:week_day>', views.get_week_day_info_by_number),
    path('<str:week_day>', views.get_week_day_info, name='week_day_name'),
]
