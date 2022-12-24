# Простые множители натурального числа N.

def isPrime(num):
    d = 2
    while d * d <= num and num % d != 0:
        d += 1
    return d * d > num

n = 12376
num_list = []
for i in range(2, int(n ** 0.5) + 1):
    if isPrime(i):
        if n % i == 0:
            num_list.append(i)
print(f'Простые множители числа {n} ->', end=" ")
print(*num_list)


