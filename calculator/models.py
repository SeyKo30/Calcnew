from django.db import models


class Calculator(models.Model):
    price = models.DecimalField(max_digits=10, decimal_places=2)
    vat_rate = models.DecimalField(max_digits=5, decimal_places=2)

    def calculate_vat(self):
        return self.price * (self.vat_rate / 100)

    def calculate_total(self):
        return self.price + self.calculate_vat()
