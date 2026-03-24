# TODO Напишите функцию find_common_participants
def find_common_participants(group1, group2, separator=','):
    list1 = group1.split(separator) # Создаём списки с  разделителем в виде запятой
    list2 = group2.split(separator)

    intersection_list = list(set(list1).intersection(list2)) # Находим пересечения в списках
    intersection_list.sort() # Сортируем их по алфавиту

    return intersection_list # Возвращаемся к списку


participants_first_group = "Иванов|Петров|Сидоров" # Оставим списки с разделителем отличным от запятой для последующей проверки функции
participants_second_group = "Петров|Сидоров|Смирнов"

participants_first = "Иванов,Петров,Сидоров" # Зададим списки с разделителем в виде запятой
participants_second = "Петров,Сидоров,Смирнов"
common_participants = find_common_participants(participants_first, participants_second) # Используем функцию для нахождения повторяющихся участников
print(f"Общие участники (разделитель ','): {common_participants}")
common_participant = find_common_participants(participants_first_group, participants_second_group, "|") # Проверяем работу функции с помощью другого разделителя и с другим названием переменной
print(f"Общие участники с другим разделителем (|): {common_participant}")
# TODO Провеьте работу функции с разделителем отличным от запятой
