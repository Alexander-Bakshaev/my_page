from django.urls import path
from . import views

urlpatterns = [
    path('', views.greeting),
    # path('<int:week_day>/<int:month>/<int:day>', views.get_week_day_info_by_date),
    path('<int:week_day>', views.get_week_day_info_by_number),
    path('<str:week_day>', views.get_week_day_info, name='week_day_name'),
]
