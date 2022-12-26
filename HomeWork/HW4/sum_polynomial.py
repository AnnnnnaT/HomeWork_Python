polynomial1 = '60x⁵ - 9x⁴ + 3x³ + x² + 10x - 7 = 0'
polynomial2 = '4x¹¹ - x⁸ + x⁷ + 8x⁶ - 4x⁵ - 23x⁴ + 10x² = 0'

def create_simple_monomials(polynomial: str):
    sym_dict = {
        0: "\u2070", 1: "\u00B9", 2: "\u00B2", 3: "\u00B3", 4: "\u2074",
        5: "\u2075", 6: "\u2076", 7: "\u2077", 8: "\u2078", 9: "\u2079"
    }

    polynomial = polynomial.replace('x ', 'x1 ').replace(' x', ' 1x')\
        .replace('+ ', '').replace(' - ', ' -').replace('= 0', '')
    monomials_list = polynomial.split()
    if 'x' not in monomials_list[-1]:
        monomials_list[-1] = monomials_list[-1] + 'x0'

    for k in sym_dict:
        for i in range(len(monomials_list)):
            while sym_dict[k] in monomials_list[i]:
                monomials_list[i] = monomials_list[i].replace(sym_dict[k], str(k))
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
    sum_koef_dict = koef_degree1 | koef_degree2
    for i in sum_koef_dict:
        sum_koef_dict[i] = koef_degree1.get(i, 0) + koef_degree2.get(i, 0)
    return sum_koef_dict

def create_pretty_degree(sum_koef: dict):
    sym_dict = {
        0: "\u2070", 1: "\u00B9", 2: "\u00B2", 3: "\u00B3", 4: "\u2074",
        5: "\u2075", 6: "\u2076", 7: "\u2077", 8: "\u2078", 9: "\u2079"
    }
    degree_dict = {}
    for degree in sum_koef.keys():
        if degree < 10:
            degree_dict[degree] = sym_dict[degree]
        elif 10 <= degree < 100:
            degree_dict[degree] = sym_dict[degree // 10] + sym_dict[degree % 10]
    return degree_dict

def create_sum_polynomial(sum_koef: dict):
    polynomial_list = []
    pretty_degree = create_pretty_degree(sum_koef)
    for i in sorted(sum_koef, reverse=True):
        if i != 0:
            elem = str(sum_koef[i]) + 'x' + pretty_degree[i]
            polynomial_list.append(elem)
        elif i == 0 and sum_koef[0] != 0:
            polynomial_list.append(str(sum_koef[0]))
    for i in range(len(polynomial_list)):
        polynomial_list[i] = polynomial_list[i].replace('-1x', '-x')
        if polynomial_list[i].startswith('1x'):
            polynomial_list[i] = polynomial_list[i].replace('1x', 'x')
        if polynomial_list[i].endswith('x' + pretty_degree[1]):
            polynomial_list[i] = polynomial_list[i].replace('x' + pretty_degree[1], 'x')
    
    polynomial = polynomial_list[0]
    for i in range(1, len(polynomial_list)):
        if polynomial_list[i].startswith('-'):
            polynomial += ' - ' + polynomial_list[i][1::]
        else:
            polynomial += ' + ' + polynomial_list[i]
    polynomial += ' = 0'
    return polynomial

sum_koef_dict = {}
print(polynomial1)
print(polynomial2)
koef_degree1 = dict_koef_degree(create_simple_monomials(polynomial1))
koef_degree2 = dict_koef_degree(create_simple_monomials(polynomial2))
sum_polynomial = create_sum_polynomial(sum_koef(koef_degree1, koef_degree2))
print(sum_polynomial)

# 60x⁵ - 9x⁴ + 3x³ + x² + 10x = 0
# 4x¹¹ - x⁸ + x⁷ + 8x⁶ - 4x⁵ - 23x⁴ - 87x³ + 10x² + 4x - 3 = 0
# 4x¹¹ - x⁸ + x⁷ + 8x⁶ + 56x⁵ - 32x⁴ - 84x³ + 11x² + 14x - 3 = 0
