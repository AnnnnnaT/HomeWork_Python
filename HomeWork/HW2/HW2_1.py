# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.

num = input("Введите число: ")
total = 0
for item in num:
    if item != '.' and item != ',':
        total += int(item)
print(f'{num} -> {total}')

