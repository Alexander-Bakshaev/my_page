from django.shortcuts import render
from django.http import HttpResponse

week_days = {"monday": "Понедельник",
             "tuesday": "Вторник",
             "wednesday": "Среда",
             "thursday": "Четверг",
             "friday": "Пятница",
             "saturday": "Суббота",
             "sunday": "Воскресенье",
             }


def get_week_day_info(request, week_day):
    return HttpResponse(week_days[week_day])
