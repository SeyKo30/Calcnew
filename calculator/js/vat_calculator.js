$(document).ready(function() {
    // Функция для форматирования числа с разделителями тысяч
    function formatNumber(number) {
        return number.toString().replace(/\B(?=(\d{3})+(?!\d))/g, " ");
    }

    // Обработчик события изменения поля ввода
    $('#id_price').on('input', function() {
        let value = $(this).val().replace(/\s/g, ''); // Удаляем все пробелы из значения поля
        if (!isNaN(value)) {
            $(this).val(formatNumber(value)); // Форматируем число с разделителями тысяч и устанавливаем новое значение поля
        }
    });

    // Обработчик события отправки формы
    $('form').on('submit', function(event) {
        event.preventDefault(); // Предотвращаем отправку формы по умолчанию

        // Получаем значения из полей
        let price = $('#id_price').val().replace(/\s/g, ''); // Удаляем все пробелы из значения поля
        let vatRate = $('#id_vat_rate').val();

        // Выполняем расчет
        let vatAmount = (price * vatRate) / 100;
        let totalPrice = parseFloat(price) + vatAmount;
        let priceWithoutVat = parseFloat(price);

        // Выводим результат на страницу
        $('#result').html('<p>Цена без НДС: ' + priceWithoutVat.toFixed(2) + '</p>' +
                          '<p>Сумма НДС: ' + vatAmount.toFixed(2) + '</p>' +
                          '<p>Общая сумма с НДС: ' + totalPrice.toFixed(2) + '</p>');
    });
});
