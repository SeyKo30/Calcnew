from django.shortcuts import render
from .forms import CalculatorForm


def calculate(request):
    if request.method == 'POST':
        form = CalculatorForm(request.POST)
        if form.is_valid():
            calculator = form.save(commit=False)
            vat_amount = calculator.calculate_vat()
            total_price = calculator.calculate_total()

            # Вычисляем цену без НДС
            price_without_vat = total_price - vat_amount

            return render(request, 'result.html', {
                'price_without_vat': price_without_vat,
                'vat_amount': vat_amount,
                'total_price': total_price
            })
    else:
        form = CalculatorForm()
    return render(request, 'index.html', {'form': form})
