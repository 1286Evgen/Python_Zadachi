# Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N

N = int(input('введите число: '))
result = 1
for num in range(1, N):
    result *= (num + 1)
print(f'факториал числа {N} = {result}')
