# Sem2DZ2
# Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N
# Пример:
# - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

# N = int(input('введите число: '))
# result = 1
# for num in range(1, N):
#    result *= (num + 1)
# print(f'факториал числа {N} = {result}')

N = int(input('введите число: '))
result = []
res = 1
for num in range(1, N+1):
    res = res*num
    result.append(str(res))
print('[',', '.join(result), end=' ]')