# Sem3Primer_1 

# Задайте список из N элементов, заполненных числами из промежутка [-N, N]. Найдите произведение элементов 
# на указанных позициях. Позиции хранятся в файле file.txt в одной строке одно число.

N = int(input('введите число: '))
list_N = []
for num in range(-N, N+1):
    list_N.append(int(num))
print(list_N)

with open('numbers.txt') as file:
    x = int(file.readline())
    y = int(file.readline())
print(list_N[x]*list_N[y]) # перемножили 2 и 6 элемент


