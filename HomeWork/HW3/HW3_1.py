# Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму
# элементов списка, стоящих на позиции с нечетным индексом.

from random import randint as ri
# num_list = [2, 3, 5, 9, 3]
num_list = [ri(1, 10) for _ in range(ri(5, 10))]
total = 0
for i in range(1, len(num_list), 2):
    total += num_list[i]
print(f'Созданый список: {num_list}\nСумма элементов на позиции с нечетным индексом: {total}')

