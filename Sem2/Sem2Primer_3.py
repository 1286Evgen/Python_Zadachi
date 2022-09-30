# 3. Напишите программу, в которой пользователь будет задавать две строки, 
# а программа - определять количество вхождений одной строки в другой.

text1 = str(input('введите строку 1: '))
text2 = str(input('введите строку 2: '))

# string = ''
# substring = ''

# if len(text1) > len(text2):
#    string = text1
#    substring = text2
# else:
#    string = text2
#    substring = text1
# print(string.count(substring))


# ИЛИ

if len(text1) > len(text2):
    print(text1.count(text2))
else:
    print(text2.count(text1))





