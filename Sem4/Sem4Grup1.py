
# Sem4Grup1

# Задайте строку из набора чисел. Напишите программу, которая покажет большее и меньшее
# число. В качестве символа-разделителя используйте пробел.

# в одной строке перебираем for -ом то что вводим с клавиатуры, преобразовываем в целое число int, 
# .split делит строку по пробелам и записывает через запятую
#str_min_max = [int(n) for n in input("введите целые числа: ").split()]
#print(str_min_max)

# первый способ решения:

#minima = str_min_max[0]
#maxima = str_min_max[1]

#for x in str_min_max:
#    if x > maxima:
#        maxima = x
#    elif x < minima:
#        minima = x
#print(f'минимальное число списка: {minima}, максимальное число списка: {maxima}')

# второй способ решения через функции -min- и -max-:

str_min_max = [int(n) for n in input("введите целые числа: ").split()]
print(str_min_max)

minima = min(str_min_max)
maxima = max(str_min_max)

print(f'минимальное число списка: {minima}, максимальное число списка: {maxima}')