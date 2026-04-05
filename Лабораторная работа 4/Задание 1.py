# TODO решите задачу
import json # Импортируем модуль

def task(file_path) -> float: # Задаём функцию
    file_path = "input.json" # Задаём переменную для данных
    with open(file_path, 'r', encoding= 'utf-8') as file: # Открываем файл в формате чтения с кодировкой utf-8
        data = json.load(file)  # Выполняем чтение файла и десериализацию в объект Пайтон
    total = 0 # Зададим переменную для подсчёта суммы
    for item in data:
        total += item['score'] * item['weight'] # прибавляем значение каждого произведения к переменной

    return round(total, 3) # Округляем переменную до третьего знака после запятой

result = task('data.json')
print(result)
