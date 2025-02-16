from django.shortcuts import render
from django.http import HttpResponse

week_days = {'monday': 'в понедельник я жалею себя',
             'tuesday': 'во вторник - глазею в пропасть',
             'wednesday': 'в среду решаю проблему мирового голода (никому не говорите)',
             'thursday ': 'в четверг - зарядка',
             'friday ': 'ужин с собой, нельзя снова его пропускать',
             'saturday ': 'в субботу - борьба с презрением к себе',
             'sunday ': 'в воскресенье - иду на рождество'
             }


def get_week_day_info(request, week_day):
    return HttpResponse(week_days[week_day])
