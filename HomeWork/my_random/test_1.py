import time
import math

def get_c():
    a = time.perf_counter()
    #b = float(str(a)[::-1])
    #c = a / float(str(a)[::-1])
   # c = abs(k * (math.sqrt(a) + math.sqrt(b) + math.sqrt(k)) / (math.log(a) * math.log(b) * math.log(k)))
    return a%1

count_dict = dict()

for _ in range(10000):
    second_digit = str(get_c())[-2]
    # last_digit = int(last_digit)
    count_dict[second_digit] = count_dict.setdefault(second_digit, 0) + 1

for k, v in sorted(count_dict.items(), key=lambda x: x[1]):
    print(f'{k} - {v}')
