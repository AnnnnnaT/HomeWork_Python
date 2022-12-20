# Напишите программу, которая будет преобразовывать десятичное число в двоичное.

user_n = int(input('Введите число: '))
n = user_n
num_list = []
while n > 0:
    num = n % 2
    num_list.append(str(num))
    n = n // 2
num_list.reverse()
num = int(''.join(num_list))
print(f'Число {user_n} в десятичной системе = {num} в двоичной системе')


