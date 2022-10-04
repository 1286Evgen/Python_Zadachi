# Sem3DZ3

# Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и
# минимальным значением дробной части элементов.
# Пример: [1.1, 1.2, 3.1, 5, 10.01] => 0.19

numbers = [1.1, 1.2, 3.1, 5, 10.01]
fractional_parts = []
for i in range(len(numbers)):
    fractional_parts.append(numbers[i] - int(numbers[i]))
print(max(fractional_parts) - min(fractional_parts))