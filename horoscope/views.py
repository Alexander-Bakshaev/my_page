from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse

zodiac = {
    'aries': ["♈", "Овен - первый знак зодиака, планета Марс (с 21 марта по 20 апреля)."],
    'taurus': ["♉", "Телец - второй знак зодиака, планета Венера (с 21 апреля по 21 мая)."],
    'gemini': ["♊", "Близнецы - третий знак зодиака, планета Меркурий (с 22 мая по 21 июня)."],
    'cancer': ["♋", "Рак - четвёртый знак зодиака, Луна (с 22 июня по 22 июля)."],
    'leo': ["♌", "Лев - пятый знак зодиака, солнце (с 23 июля по 21 августа)."],
    'virgo': ["♍", "Дева - шестой знак зодиака, планета Меркурий (с 22 августа по 23 сентября)."],
    'libra': ["♎", "Весы - седьмой знак зодиака, планета Венера (с 24 сентября по 23 октября)."],
    'scorpio': ["♏", "Скорпион - восьмой знак зодиака, планета Марс (с 24 октября по 22 ноября)."],
    'sagittarius': ["♐", "Стрелец - девятый знак зодиака, планета Юпитер (с 23 ноября по 22 декабря)."],
    'capricorn': ["♑", "Козерог - десятый знак зодиака, планета Сатурн (с 23 декабря по 20 января)."],
    'aquarius': ["♒", "Водолей - одиннадцатый знак зодиака, планеты Уран и Сатурн (с 21 января по 19 февраля)."],
    'pisces': ["♓", "Рыбы - двенадцатый знак зодиака, планеты Юпитер (с 20 февраля по 20 марта)."]
}

elements = {
    'fire': ['aries', 'leo', 'sagittarius'],
    'earth': ['taurus', 'virgo', 'capricorn'],
    'air': ['gemini', 'libra', 'aquarius'],
    'water': ['cancer', 'pisces', 'scorpio']
}


def get_html_list(by, revers_name):
    bata = ''.join(f'<li><a href="{reverse(revers_name, args=[s])}">{s.title()}</a></li>' for s in by)
    result = f'<h2><ul>{bata}</ul></h2>'
    return result


def index(request) -> HttpResponse:
    return HttpResponse(get_html_list(zodiac.keys(), 'horoscope_name'))


def get_elements(request) -> HttpResponse:
    return HttpResponse(get_html_list(elements.keys(), 'element'))


def get_tipe_elements(request, element: str) -> HttpResponse:
    result = elements.get(element, None)
    if result is None:
        return HttpResponseNotFound(f"Элемента '{element}' не существует.")
    return HttpResponse(get_html_list(result, 'horoscope_name'))


def get_zodiac_sign_info(request, zodiac_sign: str) -> HttpResponse:
    result = zodiac.get(zodiac_sign, None)
    if result is None:
        return HttpResponseNotFound(f"Знака зодиака '{zodiac_sign}' не существует.")
    return HttpResponse(f"{result[0]} - {result[1]}")


def get_zodiac_sign_info_by_number(request, zodiac_sign: int) -> HttpResponse:
    if 1 <= zodiac_sign <= len(zodiac):
        sign_name = list(zodiac.keys())[zodiac_sign - 1]
        redirect_url = reverse("horoscope_name", args=(sign_name,))
        return HttpResponseRedirect(redirect_url)
    else:
        return HttpResponseNotFound(f"{zodiac_sign} такого знака зодиака не существует")
