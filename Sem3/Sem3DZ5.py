# Sem3DZ5

# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
# Пример:
# для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]
# F−n = (−1)n+1Fn [Негафибоначчи]
# F−1 = 1
# F−2 = -1
# Fn = F(n+2)−F(n+1)

n = (int(input('введите до какого номера числа фибоначи вывести на экран: '))) 

# создадим финкцию для вычисления чисел фибоначчи на положительных позициях

def posfib(n):
    if n == 0:
        return 0
    elif n in [1, 2]:
        return 1
    else:
        return posfib(n-1) + posfib(n-2)
positive_list = []
for e in range (n+1):
    positive_list.append(posfib(e))

# создадим финкцию для вычисления чисел фибоначчи на отрицательных позициях

def negfib(n):
    if n == -1:
        return 1
    elif n == -2:
        return -1 
    else:
        return negfib(n+2) - negfib(n+1)
negative_list = []
y = -1
while y > (-n - 1):
    negative_list.append(negfib(y))
    y = y - 1
list.reverse(negative_list)

# сольем числа фибоначчи на отрицательных позициях с числами фибоначчи на положительных позициях

result_list = negative_list + positive_list
print(result_list)