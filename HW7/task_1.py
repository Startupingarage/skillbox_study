print('Задача 1. Сумма чисел')

# Напишите функцию summa_n, которая принимает одно целое положительное число N и выводит сумму всех чисел от 1 до N включительно.

# Пример работы программы
# Введите число: 5
# Сумма чисел от 1 до 5 равна 15

def summa_n(n):
    count = 0
    for i in range(1, n + 1):
        count += i
    print(f'Сумма чисел от 1 до {n} равна {count}')


n = int(input("Введите число: "))
summa_n(n)