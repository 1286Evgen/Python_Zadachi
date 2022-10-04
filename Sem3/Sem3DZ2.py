# Sem3DZ2

# Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний
# элемент, второй и предпоследний и т.д.
# Пример:
# 2 -> [2, 3, 4, 5, 6] => [12, 15, 16];
# 3 -> [2, 3, 5, 6] => [12, 15]

numbers = [2, 3, 4, 5, 6] 
composition_num = []
for i in range(len(numbers)):
    if i < len(numbers)/2:
        composition_num.append(numbers[i] * (numbers[len(numbers)-1- i]))
print(composition_num)
