# Sem4Grup2

# Найдите корни квадратного уравнения Ax² + Bx + C = 0 двумя способами:
# 1) с помощью математических формул нахождения корней квадратного уравнения
# 2) с помощью дополнительных библиотек Python (например, numpy.roots)

# 1)

#import math

#a = int(input("Введите значение переменной A: "))
#b = int(input("Введите значение переменной B: "))
#c = int(input("Введите значение переменной C: "))

#D = b**2 - 4*a*c
#print(f"Дискриминант равен: {D}")

#if D > 0:
#    x1 = (-b + math.sqrt(D)) / (2 * a)
#    x2 = (-b - math.sqrt(D)) / (2 * a)
#    print(f"если переменные: A= {a}, B= {b}, C= {c}, то квадратное уравнение Ax² + Bx + C = 0 имеет 2 корня: {x1} и {x2}")
#elif D == 0:
#    x1 = -b / 2 * a
#    print(f"если переменные: A= {a}, B= {b}, C= {c}, то квадратное уравнение Ax² + Bx + C = 0 имеет 1 корнь: {x1}")
#elif D < 0:
#    print(f"если переменные: A= {a}, B= {b}, C= {c}, то квадратное уравнение не имеет корней")

# 2)

import math
import numpy

a = int(input("Введите значение переменной A: "))
b = int(input("Введите значение переменной B: "))
c = int(input("Введите значение переменной C: "))

p = [a, b, c]

print(f"{numpy.roots(p)}")