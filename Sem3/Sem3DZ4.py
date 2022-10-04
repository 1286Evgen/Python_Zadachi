# Sem3DZ4

# Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# Пример:
# 45 -> 101101
# 3 -> 11
# 2 -> 10

n = int(input('введите число: '))
binary_number = []
while n > 0:
    x = n%2
    n = int(n/2)
    binary_number.append(x)
binary_number.reverse()
for x in binary_number:
    print(x, end='')

