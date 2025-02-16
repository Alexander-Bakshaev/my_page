from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound

week_days = {'monday': 'в понедельник я жалею себя',
             'tuesday': 'во вторник - глазею в пропасть',
             'wednesday': 'в среду решаю проблему мирового голода (никому не говорите)',
             'thursday': 'в четверг - зарядка',
             'friday': 'ужин с собой, нельзя снова его пропускать',
             'saturday': 'в субботу - борьба с презрением к себе',
             'sunday': 'в воскресенье - иду на рождество'
             }


def get_week_day_info_by_number(request, week_day):
    dey_name = week_days.get(list(week_days.keys())[week_day - 1], None)
    if dey_name:
        return HttpResponse(dey_name)
    else:
        return HttpResponseNotFound(f"{week_day} неверный номер дня")


def get_week_day_info(request, week_day):
    info = week_days.get(week_day, None)
    if info:
        return HttpResponse(info)
    else:
        return HttpResponseNotFound(f"{week_day} такого дня недели не существует")
