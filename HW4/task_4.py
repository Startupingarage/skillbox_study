print('Задача 4. Марсоход 2')

# К роботу Валли отправили «коллегу» Билли. Это его первая высадка на Марс, 
# поэтому его тестируют в прямоугольном помещении размером 15 × 20 м. 
# Марсоход высаживается в центре комнаты (в точке 8, 10), затем управление им передаётся оператору, 
# то есть пользователю вашей программы. 

# Программа спрашивает, в какую сторону оператор хочет направить робота: 
# север (клавиша W), юг (клавиша S), запад (клавиша A) или восток (клавиша D). 
# Оператор делает выбор, марсоход перемещается в эту сторону на один метр, а программа сообщает новую позицию робота. 
# Если марсоход упёрся в стену, он не должен пытаться переместиться в сторону стены — в этом случае его позиция не меняется. 

# Что нужно сделать
# Создайте программу для управления роботом Билли.

# Пример:
# 
# [Программа]: Марсоход находится на позиции 6, 19, введите команду:
# [Оператор]: A
# [Программа]: Марсоход находится на позиции 5, 19, введите команду:
# [Оператор]: W
# [Программа]: Марсоход находится на позиции 5, 20, введите команду:
# [Оператор]: W
# [Программа]: Марсоход находится на позиции 5, 20, введите команду:


x, y = 14, 10

for i in range(100):
    command = input(f'Марсоход находится на позиции {x}, {y}, введите команду (W, A, S, D):')
    if command == 'W':
        y += 1
        if y>= 20:
            y = 20
    if command == 'S':
        y -= 1
        if y<= 0:
            y = 0
    if command == 'A':
        x -= 1
        if x <= 0:
            x = 0
    if command == 'D':
        x += 1
        if x >= 15:
            x = 15

    if command == 'STOP':
        break