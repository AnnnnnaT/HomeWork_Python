# Задана натуральная степень k. Сформировать случайным образом список коэффициентов
# (значения от -100 до 100) многочлена и записать в файл многочлен степени k
# если k = 2, то многочлены могут быть => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

# Основной способ решения:

from random import randint as ri

def create_pretty_degree(degree):
    sym_dict = {
        0: "\u2070", 1: "\u00B9", 2: "\u00B2", 3: "\u00B3", 4: "\u2074",
        5: "\u2075", 6: "\u2076", 7: "\u2077", 8: "\u2078", 9: "\u2079"
    }
    pretty_degree = ''
    while degree:
        pretty_degree = sym_dict[degree % 10] + pretty_degree
        degree //= 10
    return pretty_degree

def create_monomials(degree):
    degree_dict = {}
    degree_dict[0] = '1'
    degree_dict[1] = 'x'
    for i in range(2, degree + 1):
        degree_dict[i] = 'x' + create_pretty_degree(i)

    monomials_list = []
    for i in degree_dict:
        koef = ri(-10, 10)
        if i == 0 and koef not in [-1, 0, 1]:
            elem = str(koef)
            monomials_list.append(elem)
        else:
            if koef not in [-1, 0, 1]:
                elem = str(koef) + degree_dict[i]
                monomials_list.append(elem)
            elif koef == -1:
                elem = '-' + degree_dict[i]
                monomials_list.append(elem)
            elif koef == 1:
                elem = degree_dict[i]
                monomials_list.append(elem)
    monomials_list.reverse()
    return monomials_list

def create_polynomial(monomials_list):
    polynomial = monomials_list[0]
    for i in range(1, len(monomials_list)):
        if monomials_list[i].startswith('-'):
            polynomial += ' - ' + monomials_list[i][1::]
        else:
            polynomial += ' + ' + monomials_list[i]
    polynomial += ' = 0'
    return polynomial

while True:
    try:
        k1, k2 = map(int, input('Введите степени числа для первого и второго многочленов через пробел: ').split())
        if k1 <= 0 or k2 <= 0:
            print('Введите степени числа больше 0!')
        else:
            break
    except:
        print('Конвертация невозможна! Введите числа больше 0.')

monomials_list1 = create_monomials(k1)
monomials_list2 = create_monomials(k2)
polynomial1 = create_polynomial(monomials_list1)
polynomial2 = create_polynomial(monomials_list2)
print(f'Первый многочлен: {polynomial1}')
print(f'Второй многочлен: {polynomial2}')

with open('file1.txt', 'w', encoding='UTF-8') as polynomial:
    polynomial.write('Первый многочлен: ')
    polynomial.write(polynomial1)
with open('file2.txt', 'w', encoding='UTF-8') as polynomial:
    polynomial.write('Второй многочлен: ')
    polynomial.write(polynomial2)
