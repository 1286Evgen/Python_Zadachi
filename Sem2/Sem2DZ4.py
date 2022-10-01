# Sem2DZ4
# Реализуйте алгоритм перемешивания списка.

import random

# Перемешиваем список чисел

# numbers = [1, 2, 3, 4, 5]
# N = list(range(0,5))
# random.shuffle(N)
#for i in N:
#    num = numbers[i]
#    print(num)

# Перемешиваем список имен

names = ["Tom", "Sam", "Bob"]
N = list(range(0,3))
random.shuffle(N)
for i in N:
    name = names[i]
    print(name)