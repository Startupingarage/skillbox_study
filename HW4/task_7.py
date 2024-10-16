print('Задача 7. Метод бутерброда')

# В секретном агентстве Super-Secret-no решили использовать «метод бутерброда» для шифрования переписки своих сотрудников. Сначала буквы слова нумеруются в таком порядке: первая буква получает номер 1, последняя буква — номер 2, вторая — номер 3, предпоследняя — номер 4, потом третья… и так для всех букв (см. рисунок). Затем все буквы записываются в шифр в порядке своих номеров.

# Например, слово «sandwich» зашифруется в «shacnidw».
# К сожалению, программист «Super-Secret-no», написал только программу шифрования и уволился.
# И теперь агенты не могут понять, что же они написали друг другу. Помогите им.

# Пример:
# Введите зашифрованное сообщение: shacnidw
# Расшифрованное сообщение: sandwich
#          1   3   5   7   8   6   4   2
# Слово: | s | a | n | d | w | i | c | h |
# Шифр:  | s | h | a | c | n | i | d | w |


text = input('Введите зашифрованное сообщение: ')
odd_symb = ''
even_sym = ''
rotation = True

for i in text:
    if rotation:
        odd_symb += i
    else:
        even_sym = i + even_sym 

    if rotation:
        rotation = False
    else:
        rotation = True

True_text = odd_symb + even_sym

print(f'Расшифрованное сообщение: {True_text}')