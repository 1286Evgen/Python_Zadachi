
# Sem5DZ1

# Напишите программу, удаляющую из текста все слова, содержащие ""абв"".

text = input("введите текст: ")

split_line = text.split()

new_text = []

for word in split_line:
    if word.find("абв") == -1:
        new_text.append(word)
         
print("сочетание букв -абв- не содержиться в следующих словах:")
print(' '.join(new_text))

    


