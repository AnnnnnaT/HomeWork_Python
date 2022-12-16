# Реализуйте алгоритм перемешивания списка. НЕ ИСПОЛЬЗОВАТЬ ВСТРОЕННЫЕ БИБЛИОТЕКИ SHUFFLE,
# максимум использование библиотеки Random для получения случайного int

from random import randint

# 1. Создаем список рандомно:
# n = int(input('Введите количество элементов списка: '))
# value_min = int(input('Введите минимальный элемент списка: '))
# value_max = int(input('Введите максимальный элемент списка: '))
# first_list = [randint(value_min, value_max) for _ in range(n)]

# 2. Создаем упорядоченный список двузначных элементов (другой способ решения)
# подобное делала на С#
# first_list = list(range(10, 100))
# 3. И еще один вариант, долой ограничения))))
first_list = [randint(1, 100) for _ in range(5, 20)]
second_list = first_list.copy()
for i in range(len(second_list)):
    j = randint(0, (len(second_list) - 1))
    if i != j:
        second_list[i], second_list[j] = second_list[j], second_list[i]
print(f'Созданный список: {first_list}')
print(f'Перемешанный список: {second_list}')
