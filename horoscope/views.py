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


def index(request) -> HttpResponse:
    zodiacs = list(zodiac.keys())
    li_elements = ''
    for sign in zodiacs:
        redirect_path = reverse("horoscope_name", args=(sign,))
        li_elements += f"<li><a href='{redirect_path}'>{sign.title()}</a></li>"
    response = f"""
    <ul>
        {li_elements}
    </ul>
    """
    return HttpResponse(response)

def type_sign(request) -> HttpResponse:
    type_zodiac = list(elements.keys())
    li_elements = ''
    for sign in type_zodiac:
        redirect_path = reverse("horoscope_name", args=(sign,))
        li_elements += f"<li><a href='{redirect_path}'>{sign.title()}</a></li>"
    response = f"""
    <ul>
        {li_elements}
    </ul>
    """
    return HttpResponse(response)

def get_elements(request) -> HttpResponse:
    li_elements = ''
    for element in elements:
        li_elements += f"<li><a href='{element}'>{element.title()}</a></li>"
    return HttpResponse(f"<ul>{li_elements}</ul>")


def get_tipe_elements(request, element: str) -> HttpResponse:
    li_elements = ''
    for sign in elements[element]:
        redirect_path = reverse("horoscope_name", args=(sign,))
        li_elements += f"<li><a href='{redirect_path}'>{sign.title()}</a></li>"
    return HttpResponse(f"<ul>{li_elements}</ul>")


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
