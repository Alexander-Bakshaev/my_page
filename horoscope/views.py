from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from enum import Enum
from datetime import datetime
from django.template.loader import render_to_string


# Определяем класс для знаков зодиака
class ZodiacSign:
    def __init__(self, name: str, symbol: str, description: str, element: 'Element', start_date: tuple,
                 end_date: tuple):
        self.name = name
        self.symbol = symbol
        self.description = description
        self.element = element
        self.start_date = start_date  # (месяц, день)
        self.end_date = end_date  # (месяц, день)

    def __str__(self):
        return f"{self.symbol} - {self.description}"

    def is_in_range(self, month: int, day: int) -> bool:
        """
        Проверяет, находится ли дата (month, day) в диапазоне этого знака зодиака.

        :param month: Номер месяца (1-12).
        :param day: Номер дня (1-31).
        :return: True, если дата попадает в диапазон, иначе False.
        """
        input_date = datetime(year=2000, month=month, day=day)
        start_date = datetime(year=2000, month=self.start_date[0], day=self.start_date[1])
        end_date = datetime(year=2000, month=self.end_date[0], day=self.end_date[1])

        if start_date > end_date:
            return input_date >= start_date or input_date <= end_date
        else:
            return start_date <= input_date <= end_date


# Определяем Enum для элементов с символами
class Element(Enum):
    FIRE = ("fire", "🔥")
    EARTH = ("earth", "🌍")
    AIR = ("air", "🌬️")
    WATER = ("water", "🌊")

    def __init__(self, value, symbol):
        self._value_ = value
        self.symbol = symbol

    def __str__(self):
        return f"{self.symbol} {self.value.capitalize()}"


# Создаем список знаков зодиака
zodiac_signs = [
    ZodiacSign("aries", "♈", "Овен - первый знак зодиака, планета Марс.", Element.FIRE, (3, 21), (4, 19)),
    ZodiacSign("taurus", "♉", "Телец - второй знак зодиака, планета Венера.", Element.EARTH, (4, 20), (5, 20)),
    ZodiacSign("gemini", "♊", "Близнецы - третий знак зодиака, планета Меркурий.", Element.AIR, (5, 21), (6, 20)),
    ZodiacSign("cancer", "♋", "Рак - четвёртый знак зодиака, Луна.", Element.WATER, (6, 21), (7, 22)),
    ZodiacSign("leo", "♌", "Лев - пятый знак зодиака, солнце.", Element.FIRE, (7, 23), (8, 22)),
    ZodiacSign("virgo", "♍", "Дева - шестой знак зодиака, планета Меркурий.", Element.EARTH, (8, 23), (9, 22)),
    ZodiacSign("libra", "♎", "Весы - седьмой знак зодиака, планета Венера.", Element.AIR, (9, 23), (10, 22)),
    ZodiacSign("scorpio", "♏", "Скорпион - восьмой знак зодиака, планета Марс.", Element.WATER, (10, 23), (11, 21)),
    ZodiacSign("sagittarius", "♐", "Стрелец - девятый знак зодиака, планета Юпитер.", Element.FIRE, (11, 22), (12, 21)),
    ZodiacSign("capricorn", "♑", "Козерог - десятый знак зодиака, планета Сатурн.", Element.EARTH, (12, 22), (1, 19)),
    ZodiacSign("aquarius", "♒", "Водолей - одиннадцатый знак зодиака, планеты Уран и Сатурн.", Element.AIR, (1, 20),
               (2, 18)),
    ZodiacSign("pisces", "♓", "Рыбы - двенадцатый знак зодиака, планеты Юпитер.", Element.WATER, (2, 19), (3, 20)),
]


# Функция для создания HTML-списка
def generate_html_list(items, revers_name, item_name_attr=None):
    """
    Генерирует HTML-список из переданных элементов.

    :param items: Список элементов (может быть список объектов или строк).
    :param revers_name: Имя URL-маршрута для генерации ссылок.
    :param item_name_attr: Атрибут объекта, который содержит название элемента (если None, используется сам элемент).
    :return: HTML-строка с ul-списком.
    """
    if item_name_attr:
        bata = ''.join(
            f'<li><a href="{reverse(revers_name, args=[getattr(item, item_name_attr)])}">{getattr(item, item_name_attr).title()}</a></li>'
            for item in items
        )
    else:
        bata = ''.join(
            f'<li><a href="{reverse(revers_name, args=[item])}">{item.title()}</a></li>'
            for item in items
        )
    result = f'<h2><ul>{bata}</ul></h2>'
    return result


# Главная страница
def index(request) -> HttpResponse:
    zodiacs = [sign.name for sign in zodiac_signs]
    context = {
        'zodiacs': zodiacs
    }
    return render(request, 'horoscope/index.html', context=context)


# Страница со списком элементов
def get_elements(request) -> HttpResponse:
    elements_list = [str(e) for e in Element]
    return HttpResponse(generate_html_list(elements_list, 'element'))


# Страница с знаками зодиака по элементу
def get_tipe_elements(request, element: str) -> HttpResponse:
    try:
        selected_element = Element[element.upper()]
        signs_by_element = [sign for sign in zodiac_signs if sign.element == selected_element]
        if not signs_by_element:
            return HttpResponseNotFound(f"Элемента '{element}' не существует.")
        return HttpResponse(generate_html_list(signs_by_element, 'horoscope_name', item_name_attr='name'))
    except KeyError:
        return HttpResponseNotFound(f"Элемента '{element}' не существует.")


def get_yyyy_converters(request, zodiac_sign: int) -> HttpResponse:
    return HttpResponse(f"Вы передали число из четырех цифр: {zodiac_sign}")


def get_my_float_converters(request, zodiac_sign: int) -> HttpResponse:
    return HttpResponse(f"Вы передали вещественное число: {zodiac_sign}")


def get_my_date_converters(request, zodiac_sign: int) -> HttpResponse:
    return HttpResponse(f"Вы передали дату: {zodiac_sign}")


def get_split_converters(request, zodiac_sign: int) -> HttpResponse:
    return HttpResponse(f"Вы передали строку: {zodiac_sign}")


# Информация о знаке зодиака
def get_zodiac_sign_info(request, zodiac_sign: str) -> HttpResponse:
    description = next((s for s in zodiac_signs if s.name == zodiac_sign), None)
    zodiacs = [sign.name for sign in zodiac_signs]
    dict_eng_rus_name = {sign.name: sign.description.split('-')[0] for sign in zodiac_signs}

    # Форматируем даты для отображения
    if description:
        start_month = description.start_date[0]
        start_day = description.start_date[1]
        end_month = description.end_date[0]
        end_day = description.end_date[1]

        # Преобразуем номера месяцев в названия
        month_names = [
            "января", "февраля", "марта", "апреля", "мая", "июня",
            "июля", "августа", "сентября", "октября", "ноября", "декабря"
        ]

        start_date_str = f"{start_day} {month_names[start_month - 1]}"
        end_date_str = f"{end_day} {month_names[end_month - 1]}"
        date_range = f"{start_date_str} - {end_date_str}"
    else:
        date_range = "Неизвестно"

    data = {
        'description_zodiac': description.description if description else 'Неизвестно',
        'element_zodiac': str(description.element) if description else 'Неизвестно',
        'zodiac_name': description.element,
        'zodiac_symbol': description.symbol if description else '',
        'zodiacs': zodiacs,
        'dict_eng_rus_name': dict_eng_rus_name,
        'date_range': date_range,  # Добавляем диапазон дат в контекст
    }
    return render(request, 'horoscope/info_zodiac.html', context=data)


# Информация о знаке зодиака по номеру
def get_zodiac_sign_info_by_number(request, zodiac_sign: int) -> HttpResponse:
    if 1 <= zodiac_sign <= len(zodiac_signs):
        sign = zodiac_signs[zodiac_sign - 1]
        redirect_url = reverse("horoscope_name", args=(sign.name,))
        return HttpResponseRedirect(redirect_url)
    else:
        return HttpResponseNotFound(f"{zodiac_sign} такого знака зодиака не существует")


# Определение знака зодиака по дате
def get_zodiac_by_date(request, month: int, day: int) -> HttpResponse:
    # Проверка корректности месяца
    if not (1 <= month <= 12):
        return HttpResponseNotFound(f"Неверный номер месяца: {month}")

    # Проверка корректности дня
    days_in_month = {
        1: 31, 2: 29, 3: 31, 4: 30, 5: 31, 6: 30,
        7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31
    }
    if not (1 <= day <= days_in_month.get(month, 0)):
        return HttpResponseNotFound(f"Неверный день для месяца {month}: {day}")

    # Находим подходящий знак зодиака
    for sign in zodiac_signs:
        if sign.is_in_range(month, day):
            redirect_url = reverse("horoscope_name", args=(sign.name,))
            return HttpResponseRedirect(redirect_url)

    # Если дата не найдена (что маловероятно), возвращаем ошибку
    return HttpResponseNotFound(f"Не удалось определить знак зодиака для {month}/{day}")