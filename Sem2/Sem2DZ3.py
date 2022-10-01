# Sem2DZ3
# Задайте список из n чисел последовательности $(1+\frac 1 n)^n$ и выведите на экран их сумму.
# Пример:   n = 6 -> 14.071722992112484
#           n = 3 -> 6.62037037037037


n = int(input('введите целое число: '))

sumnum = 0 
for i in range(1, n+1):
    stringnum = (1+1/i)**i
    sumnum = sumnum + stringnum
print(sumnum)