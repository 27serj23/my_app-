from django.shortcuts import render
from django.http import HttpResponse
import datetime


def artwork_detail(request, artwork):
    # Проверка времени доступа
    current_time = datetime.datetime.now().time()
    start_time = datetime.time(hour=9, minute=0, second=0)
    end_time = datetime.time(hour=17, minute=0, second=0)

    if current_time < start_time or current_time > end_time:
        return HttpResponse("Доступ к странице разрешен только с 9:00 до 17:00")

    # Ваш код для отображения страницы произведения искусства
    # Здесь можно выполнить запрос к базе данных, чтобы получить информацию о произведении по его имени

    return render(request, 'artwork_detail.html', {'artwork': artwork})
