print('Задача 5. Отрезок')

# Напишите программу,
# которая считывает с клавиатуры два числа a и b,
# считает и выводит на консоль 
# среднее арифметическое всех чисел из отрезка [a; b], которые кратны числу 3.

# (среднее арифметическое можно посчитать поделив сумму подходящих чисел на их количество)


a = int(input('Введите чило а: '))
b = int(input('Введите чило b: '))

summ_num = 0
count = 0

for i in range(a,b+1):
 if i % 3 == 0:
  summ_num += i
  count += 1
if count == 0:
    print('Отрезок от а до b не выполняет условия задания')
else:
 print(summ_num / count)