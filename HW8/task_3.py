print('Задача 3. Число наоборот')

# Пользователь вводит два числа: N и K.
# Напишите программу, которая переворачивает каждое из введённых чисел, то есть записывает эти числа в обратном порядке.

# Пример
# Введите первое число: 102
# Введите второе число: 123

# Первое число наоборот: 201
# Второе число наоборот: 321


def revers_number(num):
    revers_num = 0
    while num!= 0:
        revers_num = revers_num * 10 + (num%10)
        num //= 10
    return revers_num


def int_input(imput_text, retry_text):
    while True:
        try:
            number = int(input(imput_text))
            return number
        except ValueError:
            print(retry_text)


def main():
    retry_text = 'Ошибка ввода! Пожалуйста, введите целое число.'
    num_1 = int_input('Введите первое число: ', retry_text)
    num_2 = int_input('Введите второе число: ', retry_text)

    reversed_1 = revers_number(num_1)
    reversed_2 = revers_number(num_2)

    print(f'Первое число наоборот: {reversed_1}')
    print(f'Второе число наоборот: {reversed_2}')

if __name__ == '__main__':
    main()


