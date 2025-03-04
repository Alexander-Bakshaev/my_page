from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse

week_days = {'monday': 'в понедельник я жалею себя',
             'tuesday': 'во вторник - глазею в пропасть',
             'wednesday': 'в среду решаю проблему мирового голода (никому не говорите)',
             'thursday': 'в четверг - зарядка',
             'friday': 'ужин с собой, нельзя снова его пропускать',
             'saturday': 'в субботу - борьба с презрением к себе',
             'sunday': 'в воскресенье - иду на рождество'
             }


def greeting(request):
    return render(request, 'week_days/greeting.html')


def get_week_day_info(request, week_day):
    info = week_days.get(week_day, None)
    if info:
        return HttpResponse(info)
    else:
        return HttpResponseNotFound(f"{week_day} такого дня недели не существует")


def get_week_day_info_by_number(request, week_day):
    if 1 <= int(week_day) <= 7:
        day_info = list(week_days.keys())[week_day - 1]
        redirect_url = reverse("week_days_name", args=(day_info,))
        return HttpResponseRedirect(redirect_url)
    else:
        return HttpResponseNotFound(f"{week_day} такого дня недели не существует")


# Позже удалить
def get_beautiful_table(response):
    return render(response, 'week_days/table.html', )
