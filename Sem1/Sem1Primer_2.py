# Напишите программу, которая на вход принимает 5 чисел и находит максимальное из них.
# Примеры:
# 1. 1, 4, 8, 7, 5 -> 8
# 78, 55, 36, 90, 2 -> 90

a = int(input('Введите 1 число '))
b = int(input('Введите 2 число '))
c = int(input('Введите 3 число '))
d = int(input('Введите 4 число '))
e = int(input('Введите 5 число '))
m = a
for i in a,b,c,d,e:
    if i > m:
        m = i
print(m)