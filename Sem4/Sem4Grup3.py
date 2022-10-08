
# Sem4Grup3

# Задайте два числа. Напишите программу, которая найдёт НОК (наименьшее общее кратное)
# этих двух чисел.

a = int(input("введите число а: "))
b = int(input("введите число b: "))

ia, ib = a, b
while ia != ib:
    if ia > ib: ia = ia - ib
    else: ib = ib - ia

print("НОД", ia)

print("НОК", a * b // ia)
