
# Sem5DZ2 

# Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга. 
# Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет. 
# Все конфеты оппонента достаются сделавшему последний ход. 
# Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?
# a) Добавьте игру против бота
# b) Подумайте как наделить бота ""интеллектом""

from random import randint

while True:
    try:
        all_candies = int(input('Введите количество конфет больше 50: '))
        if all_candies > 50:
            break
        else:
            print('Мало конфет для игры')
    except:
            print("Ошибка - это не число")
print()

lot = randint(1, 2)

print(f"первый ход выпал игроку № {lot}")
print()

num_cand = all_candies

while num_cand > 0:
    if lot == 1:
        while True:
            try:
                cand_1_pl = int(input('Игрок № 1, возьмите от 1 до 28 конфет: '))
                if 0 < cand_1_pl < 29:
                    break
                else:
                    print('Игрок № 1, попробуйте еще раз: ')
            except:
                print("Ошибка - это не число")
        num_cand = num_cand - cand_1_pl
        lot = 2
        print()

    else:
        while True:
            try:
                cand_2_pl = int(input('Игрок № 2, возьмите от 1 до 28 конфет: '))
                if 0 < cand_2_pl < 29:
                    break
                else:
                    print('Игрок № 2, попробуйте еще раз: ')
            except:
                print("Ошибка - это не число")
        num_cand = num_cand - cand_2_pl
        lot = 1
        print()
print(f"Выиграл игрок № {lot}, ему достается все {all_candies} конфет")
