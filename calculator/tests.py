from django.test import TestCase
from django.urls import reverse
from .forms import CalculatorForm
from .models import Calculator

#Проверка корректности ответа на запрос к главной странице
class YourViewTestCase(TestCase):
    def test_index_view(self):
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')


class CalculatorFormTestCase(TestCase):
    #Проверка что форма считается валидной при вводе правильных данных
    def test_calculator_form_valid_data(self):
        form_data = {
            'price': 100,
            'vat_rate': 20,
        }
        form = CalculatorForm(data=form_data)
        self.assertTrue(form.is_valid())

    #Проверка что форма считается невалидной при вводе неправильных данных
    def test_calculator_form_invalid_data(self):
        form_data = {
            'price': 'not_a_number',
            'vat_rate': -10,
        }
        form = CalculatorForm(data=form_data)
        self.assertFalse(form.is_valid())


class CalculatorModelTestCase(TestCase):
    # Создание  модели для тестирования
    def setUp(self):
        self.calculator = Calculator.objects.create(price=100, vat_rate=20)

    # Проверка что  calculate_vat() возвращает правильное значение НДС
    def test_calculate_vat(self):

        expected_vat = 20
        self.assertEqual(self.calculator.calculate_vat(), expected_vat)

    def test_calculate_total(self):
        # Проверка что  calculate_total() возвращает правильное значение общей суммы
        expected_total = 120
        self.assertEqual(self.calculator.calculate_total(), expected_total)
