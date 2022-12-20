# Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем
# первый и последний элемент, второй и предпоследний и т.д.

from random import randint as ri

# num_list = [2, 3, 4, 5, 6]
# num_list = [2, 3, 5, 6]
num_list = [ri(1, 10) for _ in range(ri(5, 10))]
product_num = []
for i in range((len(num_list) // 2 + len(num_list) % 2)):
    new_num = num_list[i] * num_list[-i-1]
    product_num.append(new_num)
print(f'Созданный массив: {num_list} => произведение пар чисел: {product_num}')
