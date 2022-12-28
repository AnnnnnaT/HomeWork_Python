from random import randint as ri

def polynomial(k: int):
    polynomial_list = []
    if k >= 2:
        polynomial_list = [(str(ri(-10, 10)) + 'x^' + str(k))]
        for i in range(k - 1, 1, -1):
            elem = str(ri(-10, 10)) + 'x^' + str(i)
            polynomial_list.append(elem)
        polynomial_list.append(str(ri(-10, 10)) + 'x')
        if (koef := ri(-10, 10)) != 0:
            polynomial_list.append(str(koef))
        polynom_list = [item for item in polynomial_list if not item.startswith('0x')]
        polynom = ' + '.join(polynom_list).replace('1x', 'x') \
                      .replace(' + -', ' - ') + ' = 0'
    elif k == 1:
        if (koef := ri(-10, 10)) != 0:
            polynomial_list.append(str(koef) + 'x')
            if (koef := ri(-10, 10)) != 0:
                polynomial_list.append(str(koef))
            polynom = ' + '.join(polynomial_list).replace('1x', 'x') \
                          .replace(' + -', ' - ') + ' = 0'
        else:
            return None
    else:
        return None
    return polynom

print(polynomial(0))
print(polynomial(1))
print(polynomial(5))

