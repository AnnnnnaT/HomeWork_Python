# Задана натуральная степень k. Сформировать случайным образом список коэффициентов
# (значения от 0 до 100) многочлена и записать в файл многочлен степени k
# если k = 2, то многочлены могут быть => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

from random import randint as ri

k = int(input('Введите степень числа: '))

def create_monomials(degree):
    degree_dict = {}
    degree_dict[0] = '1'
    degree_dict[1] = 'x'
    for i in range(2, degree + 1):
        degree_dict[i] = 'x^' + str(i)

    monomials_list = []
    for i in degree_dict:
        koef = ri(-100, 100)
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

monomials_list1 = create_monomials(k)
monomials_list2 = create_monomials(k)
polynomial1 = create_polynomial(monomials_list1)
polynomial2 = create_polynomial(monomials_list2)
print(polynomial1)
print(polynomial2)

with open('file1.txt', 'w', encoding='UTF-8') as polynomial:
    polynomial.write('Созданный многочлен: ')
    polynomial.write(polynomial1)
with open('file2.txt', 'w', encoding='UTF-8') as polynomial:
    polynomial.write('Созданный многочлен: ')
    polynomial.write(polynomial2)

