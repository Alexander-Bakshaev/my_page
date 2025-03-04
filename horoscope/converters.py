from datetime import datetime


class FourDigitYearConverter:
    regex = '[0-9]{4}'

    def to_python(self, value):
        return int(value)

    def to_url(self, value):
        return '%04d' % value


class MyFloatConverter:
    regex = '[+-]?(\d*\.)?\d+'

    def to_python(self, value):
        return float(value)

    def to_url(self, value):
        return str(value)


class MyDateConverter:
    regex = '^(0[1-9]|[12][0-9]|3[01])[-](0[1-9]|1[012])[-](19|20)\d\d$'

    def to_python(self, value):
        return datetime.strptime(value, '%d-%m-%Y')

    def to_url(self, value):
        return value.strftime('%d-%m-%Y')

class SplitConverter:
    regex = '(\w+,)+\w+'

    def to_python(self, value):
        return value.split(',')

    def to_url(self, value):
        return ','.join(value)

class UpperConvertor:
    regex = '\w+'

    def to_python(self, value):
        return value.upper()

    def to_url(self, value):
        return value
