from django.test import TestCase
from django.urls import reverse
from . import views


class TestHoroscope(TestCase):
    def test_index_page(self):
        response = self.client.get('/horoscope/')
        self.assertEqual(response.status_code, 200)

    def test_zodiac_signs(self):
        for sign in views.zodiac_signs:
            url = reverse('horoscope_name', args=[sign.name])
            response = self.client.get(url)
            self.assertEqual(response.status_code, 200)
            expected_text = f"{sign.symbol} - {sign.description}"
            self.assertIn(expected_text, response.content.decode('utf-8'))

    def test_zodiac_number_redirect(self):
        for count, sign in enumerate(views.zodiac_signs, start=1):
            response = self.client.get(f'/horoscope/{count}')
            self.assertEqual(response.status_code, 302)
            expected_redirect_url = reverse('horoscope_name', args=[sign.name])
            self.assertEqual(response.url, expected_redirect_url)  # Проверяем корректность редиректа
