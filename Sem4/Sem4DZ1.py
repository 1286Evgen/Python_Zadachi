
# Sem4DZ1

# Вычислить число c заданной точностью d

# Пример:
# - при $d = 0.001, π = 3.141.$    $10^{-1} ≤ d ≤10^{-10}$

import math

def num_after_comma(x):
    res = 0
    while x % 1 > 0:
        x *= 10
        res += 1
    return res

num_user = float(input("введите необходимую точность при вычислении: "))
res_pi = (round(math.pi, num_after_comma(num_user)))
print(res_pi)