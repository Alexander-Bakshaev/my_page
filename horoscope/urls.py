from django.urls import path, register_converter
from . import views, converters

register_converter(converters.FourDigitYearConverter, 'yyyy')
register_converter(converters.MyFloatConverter, 'my_float')
register_converter(converters.MyDateConverter, 'my_date')
register_converter(converters.SplitConverter, 'split')
# register_converter(converters.UpperConvertor, 'upper')
urlpatterns = [
    path('', views.index, name='horoscope_index'),
    path('type', views.get_elements, name='elements'),
    path('type/<str:element>', views.get_tipe_elements, name='element'),
    path('<yyyy:zodiac_sign>', views.get_yyyy_converters),
    path('<int:zodiac_sign>', views.get_zodiac_sign_info_by_number),
    path('<my_float:zodiac_sign>', views.get_my_float_converters),
    path('<my_date:zodiac_sign>', views.get_my_date_converters),
    path('<split:zodiac_sign>', views.get_split_converters),

    path('<str:zodiac_sign>', views.get_zodiac_sign_info, name='horoscope_name'),

    path('<int:month>/<int:day>/', views.get_zodiac_by_date, name='zodiac_by_date'),

]
