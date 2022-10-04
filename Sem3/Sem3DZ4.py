# Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# Пример:
# 45 -> 101101
# 3 -> 11
# 2 -> 10

n = int(input('введите число: '))
didgin = []
while n > 0:
    x = n%2
    n = int(n/2)
    didgin.append(x)
didgin.reverse()
for x in didgin:
    print(x, end='')

