print('Задача 5. Великий и могучий')

# Паоло изучает русский язык: занимается по учебникам, читает книги, слушает музыку. 
# Ему особенно понравилась книга «Преступление и наказание». Паоло решил найти самое длинное слово в этой книге, 
# чтобы сравнить его с аналогом на своём языке.

# Что нужно сделать

# Напишите программу, которая получает на вход текст и находит длину самого длинного слова в нём. 
# Слова в тексте разделяются одним пробелом.

# Пример:

# Введите текст: Меня зовут Пётр.
# Самое длинное слово, букв: 5.

# Введите текст: Меня зовут Василий
# Самое длинное слово, 7 букв

text = input('Введите текст: ')
count_w = 0
count_max = 0

for i in text:
    if i != ' ':
        count_w += 1
    else:
        if count_w > count_max:
            count_max = count_w
        count_w = 0

if count_w > count_max:
            count_max = count_w

print(f'Самое длинное слово, букв: {count_max}.')
