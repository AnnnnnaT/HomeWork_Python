while True:
    try:
        k1, k2 = map(int, input('Введите степени числа для первого и второго многочленов через пробел: ').split())
        if k1 <= 0 or k2 <= 0:
            print('Введите степени числа больше 0!')
        else:
            break
    except:
        print('Конвертация невозможна! Введите числа больше 0.')

x = k1+k2
print(x)

# def create_degree(degree):
#     sym_dict = {1: "\u00B9", 2: "\u00B2", 3: "\u00B3", 4: "\u2074", 5: "\u2075", 6: "\u2076", 7: "\u2077", 8: "\u2078",
#                 9: "\u2079"}
#     pretty_degree = ''
#     while degree:
#         pretty_degree = sym_dict[degree % 10] + pretty_degree
#         degree //= 10
#     return pretty_degree
#
#
# x = 'x' + create_degree(3)
# print(x)

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
