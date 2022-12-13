# Задача 2. Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z
# для всех значений предикат.
# ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z -> not(x or y or z) == not x and not y and not z
# x_y_z = [
#     [0, 0, 1],
#     [1, 1, 1],
#     [1, 0, 0],
#     [0, 1, 0],
#     [0, 0, 1],
#     [1, 1, 0],
#     [1, 0, 1],
#     [0, 1, 1]
# ]
# for i in range(8):
#     a = not (x_y_z[i][0] or x_y_z[i][1] or x_y_z[i][2])
#     b = not (x_y_z[i][0] or x_y_z[i][1] or x_y_z[i][2])
#     if a != b:
#         print('Выражение: ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z - False')
#         break
# else:
#     print('Выражение: ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z - True')

for x in [False, True]:
    for y in [False, True]:
        for z in [False, True]:
            if (not x or y or z) != (not x or y or z):
                print('Выражение: ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z - False')
                break
else:
    print('Выражение: ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z - True')
