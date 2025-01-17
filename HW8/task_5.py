print('Задача 5. Маятник')

# Известно, что амплитуда качающегося маятника с каждым разом затухает на 8,4% от амплитуды предыдущего колебания.
# Если качнуть маятник, то, строго говоря, он не остановится никогда, просто амплитуда будет постоянно уменьшаться до тех пор,
# пока мы не сочтём такой маятник остановившимся.

# Что нужно сделать
# Напишите программу, определяющую, сколько раз качнётся маятник, прежде чем он, по нашему мнению, остановится.

# Программа получает на вход начальную амплитуду колебания в сантиметрах и конечную амплитуду колебаний, которая считается остановкой маятника.
# Обеспечьте контроль ввода.

# Подсказка: для уменьшения числа можно умножить его на значение, которое меньше единицы.
# Например, уменьшение на 10%: 100 * 0.9 = 90.

# Пример
# Введите начальную амплитуду: 1
# Введите амплитуду остановки: 0.1
# Маятник считается остановившимся через 27 колебаний


def float_input(text, retry_text):
    """
    Запрашивает у пользователя вещественное число.
    """
    while True:
        try:
            return float(input(text))
        except ValueError:
            print(retry_text)

def main():
    """Основная логика программы."""
    retry_text = 'Введите числовое значение повторно'
    initial_amplitude = float_input('Введите начальную амплитуду: ', retry_text)
    final_amplitude = float_input('Введите конечную амплитуду: ', retry_text)

    if final_amplitude > initial_amplitude:
        print("Ошибка: конечная амплитуда не может быть больше начальной.")
        return

    x = initial_amplitude
    count = 0
    while x >= final_amplitude:
        x *= 0.916
        count += 1


    print((
        f"Маятник:\n"
        f"Начальная амплитуда: {initial_amplitude}\n"
        f"Конечная амплитуда: {final_amplitude}\n"
        f"Количество колебаний до остановки: {count}"
    ))

if __name__ == '__main__':
    main()