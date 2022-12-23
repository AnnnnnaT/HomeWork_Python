# a, b, c = map(int, input().split())
#
# if a >= b >= c:
#     max_num, mid_num, min_num = a, b, c
# elif a >= c >= b:
#     max_num, mid_num, min_num = a, c, b
# elif b >= a >= c:
#     max_num, mid_num, min_num = b, a, c
# elif b >= c >= a:
#     max_num, mid_num, min_num = b, c, a
# elif c >= b >= a:
#     max_num, mid_num, min_num = c, b, a
#
# print(f'{max_num}\n{min_num}\n{mid_num}')

# def isPrime(num):
#     d = 2
#     while d * d <= num and num % d != 0:
#         d += 1
#     return d * d > num
#
# n = int(input('Введите натуральное число: '))
# num_list = []
# for i in range(2, int(n ** 0.5) + 1):
#     if isPrime(i):
#         if n % i == 0:
#             num_list.append(i)
# print(f'Простые множители числа {n} -> {num_list}')

# num_list = [1, 2, 3, 4, 3, 2, 1]
# print(list(set(num_list)))

