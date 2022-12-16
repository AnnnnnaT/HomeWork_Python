# Задайте список из n чисел последовательности (1 + 1/n)^n, выведеите его на экран, а так же
# сумму элементов списка.

n = int(input('Введите число: '))
total = 0
num_list = []
for i in range(1, n + 1):
    num = (1 + 1 / i) ** i
    if num - int(num) == 0: # данную проверку сделала, чтобы вывод был 2, а не 2.0
        num = int(num)
    else:
        num = round(num, 2)
    num_list.append(num)
    total += num
print(f'n = {n} -> {num_list}\nСумма {total}')
