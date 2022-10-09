
# Sem4DZ3

# Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов 
# исходной последовательности.

#                   первый способ:

num_array = [int(n) for n in input("введите целые числа: ").split()]
print()
print(f"задана следующая последовательность чисел: {num_array}")

for x in num_array:
    count = 0
    for y in num_array:
        if x == y:
            count += 1
            if count > 1:
                num_array.remove(y)
                count = 1
print()                  
print(f"список не повторяющихся элементов исходной последовательности: {num_array}")
print()

#                   второй способ:

num_array = [int(n) for n in input("введите целые числа: ").split()]
print()
print(f"задана следующая последовательность чисел: {num_array}")
print()                  
print(f"список не повторяющихся элементов исходной последовательности: {set(num_array)}")
print()
