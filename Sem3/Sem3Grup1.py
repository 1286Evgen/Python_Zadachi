# Sem3Grup1

# Задайте список. Напишите программу, которая определит, присутствует ли в заданном списке
# строк некое число.

n = (input('введите число: '))

list_num = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
for x in list_num:
    if x == n:
        print(f'ура!!! В списке {list_num}, есть {n}')
    break
print(f'нет!!! В списке {list_num}, нет {n}')