# TODO импортировать необходимые модули
import json # Импортируем модули json и csv
import csv

INPUT_FILENAME = "input.csv"
OUTPUT_FILENAME = "output.json"


def task() -> None:
    with open(INPUT_FILENAME, 'r', encoding='utf-8') as csv_file: # Открываем файл в формате чтения в кодировке utf-8
        csv_reader = csv.DictReader(csv_file) # Задаём переменную, которая отвечает за данные полученные из файла
        data = list(csv_reader) # Преобразовываем данные в список
    with open(OUTPUT_FILENAME, 'w', encoding='utf-8') as json_file: # Открываем файл в формате написания в кодировке utf-8
        json.dump(data, json_file, indent=4) # Сериализуем данные в файл с отступами равными 4


if __name__ == '__main__':
    # Нужно для проверки
    task()

    with open(OUTPUT_FILENAME) as output_f:
        for line in output_f:
            print(line, end="")
