# Sem2DZ1
# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.

# Пример:

# - 6782 -> 23
# - 0,56 -> 11

number = float(input('введите  число: '))
strnum1 = str(number)
strnum2 = strnum1.replace('.','') 
sumnum = 0
for i in range(0, len(strnum2)):
    sumnum = sumnum + int(strnum2[i])
print(sumnum)
