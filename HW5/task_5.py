print('Задача 5. Наибольшая сумма цифр')

# Вводится N чисел. 
# Среди натуральных чисел, которые были введены, 
# найдите наибольшее по сумме цифр. Выведите на экран это число и сумму его цифр.
N = int(input('Введите кол-во чисел: '))

num_max_sum = 0
max_sum = 0

for i in range(N):
    num = int(input('Введите числа: '))
    if num <= 0:
        continue
    temp_num = num
    iter_sum = 0

    while temp_num > 0:
        iter_sum += temp_num % 10
        temp_num //=10

    if iter_sum > max_sum:
        max_sum = iter_sum
        num_max_sum = num
if max_sum == 0:
    print('Не было введено ни одного натурального числа.')
else:
    print(f'Число с наибольшей суммой цифр: {num_max_sum}\nСумма его цифр: {max_sum}')