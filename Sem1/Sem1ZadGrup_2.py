# Напишите программу, которая будет принимать на вход дробь и 
# показывать первую цифру дробной части числа.
# Примеры: 6,72 -> 7 ; 5 -> нет; 0,34 -> 3.

x = float(input('введите число  ')) # запрашиваем число
y = x - int(x)                      # вычитаем из заданного числа его целую часть
if y!=0:                            
    print(int(y*10))
else:
    print('у заданного числа нет дробной части')
