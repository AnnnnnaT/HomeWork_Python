# Многочлен 2 способ (без словаря и без функций):

from random import randint as ri

k = int(input('Введите степень числа: '))
polynomial_list = []
for i in range(k + 1, 1, -1):
    koef = ri(-100, 100)
    if koef not in [-1, 0, 1] and i != 2:
        value = str(koef) + 'x^' + str(i - 1)
        polynomial_list.append(value)
    elif koef not in [-1, 0, 1] and i == 2:
        value = str(koef) + 'x'
        polynomial_list.append(value)
    elif koef == 1 and i != 2:
        value = 'x^' + str(i - 1)
        polynomial_list.append(value)
    elif koef == 1 and i == 2:
        value = 'x'
        polynomial_list.append(value)
    elif koef == -1 and i != 2:
        value = '-x^' + str(i - 1)
        polynomial_list.append(value)
    elif koef == -1 and i == 2:
        value = '-x'
        polynomial_list.append(value)
last_koef = ri(-100, 100)
if last_koef != 0:
    polynomial_list.append(str(last_koef))
polynomial_list.append(' = 0')
polynomial = polynomial_list[0]
for i in range(1, len(polynomial_list)):
    if 0 < i < len(polynomial_list) - 1:
        if polynomial_list[i].startswith('-'):
            polynomial += ' - ' + polynomial_list[i][1::]
        else:
            polynomial += ' + ' + polynomial_list[i]
    else:
        polynomial += polynomial_list[i]
print(polynomial)