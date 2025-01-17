print('Задача 4. Текстовый редактор')

# Продолжаем разрабатывать новый текстовый редактор.
# Теперь нам поручили написать для него код, который считает, сколько раз в тексте встречается любая выбранная буква
# или цифра (а не только буква «ы», как было в задаче 3 урока «Цикл for: итерирование по строке»).

# Что нужно сделать
# Напишите функцию count_letters(), которая принимает на вход текст и подсчитывает, какое в нём количество цифр K и букв N.
# Функция должна вывести на экран информацию о найденных буквах и цифрах в определённом формате.

# Пример
# Введите текст: 100 лет в обед
# Какую цифру ищем? 0
# Какую букву ищем? л
# Количество цифр 0: 2
# Количество букв л: 1


def count_letters():
    count_letter = 0
    count_num = 0

    # Ввод текста и символов для поиска
    text = input('Введите текст: ')
    letter = input('Какую букву ищем? ').lower().strip()
    num = input('Какую цифру ищем? ').strip()

    # Проход по тексту
    for sym in text:
        if sym.lower() == letter:
            count_letter += 1
        if sym == num:
            count_num += 1

    # Вывод результатов
    print('Количество букв "{}": {}'.format(letter, count_letter))
    print('Количество цифр "{}": {}'.format(num, count_num), type())


count_letters()
