print('Задача 4. Отрезок')

# Напишите программу, которая считывает с клавиатуры три числа a, b и c, 
# считает и выводит на консоль среднее арифметическое всех чисел из отрезка [a; b], кратных числу c.

a = int(input('Введите число а: '))
b = int(input('Введите число b: '))
c = int(input('Введите число c: '))

summ_i = 0
i_count = 0
# Алексей, я тестирую свои решения максимально, наткнулся на обработку с 0, прописал обычный условный оператор, 
# и если второй раз ввести 0, то будет ошибка и вылет. Пришла мысль вписать сюда 'while' и все работает как я и представлял в голове. 
# Прошу дать комментарий по этому моменту.
while c == 0: 
        print('Введите корректное значение "с", отличное от 0')
        c = int(input('Введите число c: '))

for i in range(a, b + 1):
       if i % c == 0:
        summ_i += i
        i_count += 1

avarage = summ_i / i_count

print(f'Среднее арифметическое чисел отрезка [{a},{b}] кратных {c} = {avarage}')
