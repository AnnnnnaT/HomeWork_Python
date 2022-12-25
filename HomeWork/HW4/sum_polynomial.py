polynomial1 = '60x⁵ - 9x⁴ + 3x³ + x² + 10x - 7 = 0'
polynomial2 = '-x⁸ + x⁷ + 8x⁶ - 4x⁵ - 23x⁴ - 87x³ + 10x² + 4x = 0'

def create_simple_monomials(polynomial: str):
    sym_dict = {
        0: "\u2070", 1: "\u00B9", 2: "\u00B2", 3: "\u00B3", 4: "\u2074",
        5: "\u2075", 6: "\u2076", 7: "\u2077", 8: "\u2078", 9: "\u2079"
    }

    polynomial = polynomial.replace('+ ', '').replace(' - ', ' -').replace('= 0', '')
    monomials_list = polynomial.split()

    if 'x' in monomials_list[-1]:
        monomials_list[-1] = monomials_list[-1].replace('x', 'x1')
        monomials_list.append('0x0')
    else:
        monomials_list[-1] = monomials_list[-1].replace(monomials_list[-1], (monomials_list[-1] + 'x0'))

    if  monomials_list[-2][-1] == 'x':
        monomials_list[-2] = monomials_list[-2].replace('x', 'x1')

    for i in range(len(monomials_list)-1):
        if monomials_list[i].startswith('-x'):
            monomials_list[i] = '-1' + monomials_list[i][1:]
        elif  monomials_list[i].startswith('x'):
            monomials_list[i] = '1' + monomials_list[i]

    for i in range(len(monomials_list)):
        for j in range(1, len(monomials_list[i])):
            for key, value in sym_dict.items():
                if monomials_list[i][j-1] == 'x':
                    if monomials_list[i][j] == value:
                        monomials_list[i] = monomials_list[i].replace(monomials_list[i][j], str(key))
    return monomials_list

def dict_koef_degree(monomials_list):
    for i in range(len(monomials_list)):
        monomials_list[i] = monomials_list[i].split('x')
        for j in range(len(monomials_list[i])):
            monomials_list[i][j] = int(monomials_list[i][j])
    koef_degree = {}
    for i in range(len(monomials_list)):
        for j in range(len(monomials_list)):
            koef_degree[monomials_list[i][1]] = monomials_list[i][0]
    return koef_degree

def sum_koef(koef_degree1: dict, koef_degree2: dict):
    sum_koef = {}
    if len(koef_degree1) >= len(koef_degree2):
        for i in koef_degree1:
            sum_koef[i] = koef_degree1.get(i, 0) + koef_degree2.get(i, 0)
    else:
        for i in koef_degree2:
            sum_koef[i] = koef_degree1.get(i, 0) + koef_degree2.get(i, 0)
    return sum_koef

def create_sum_polynomial(sum_koef: dict):
    polynomial_list = []
    for i in sum_koef:
        elem = str(sum_koef[i]) + 'x^' + str(i)
        polynomial_list.append(elem)
    for i in range(len(polynomial_list)):
        polynomial_list[i] = polynomial_list[i].replace('x^0', '').replace('-1x', '-x')
        if polynomial_list[i].startswith('1x'):
            polynomial_list[i] = polynomial_list[i].replace('1x', 'x')
        if polynomial_list[i].endswith('x^1'):
            polynomial_list[i] = polynomial_list[i].replace('x^1', 'x')

    polynomial = polynomial_list[0]
    for i in range(1, len(polynomial_list)):
        if polynomial_list[i].startswith('-'):
            polynomial += ' - ' + polynomial_list[i][1::]
        else:
            polynomial += ' + ' + polynomial_list[i]
    polynomial += ' = 0'
    return polynomial


print(polynomial1)
print(polynomial2)
koef_degree1 = dict_koef_degree(create_simple_monomials(polynomial1))
koef_degree2 = dict_koef_degree(create_simple_monomials(polynomial2))
sum_polynomial = create_sum_polynomial(sum_koef(koef_degree1, koef_degree2))
print(sum_polynomial)