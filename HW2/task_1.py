print('Задача 1. Должники')

# В базе банка хранятся данные и должников, и законопослушных граждан. Каждому человеку система присваивает свой номер. У нас есть случайная выборка из десяти номеров. Правда, иногда база глючит и выдаёт номер с отрицательным значением. А ещё по статистике, которую собрал наш «МирПрогБанк», каждый второй пользователь брал кредит и не выплатил его вовремя, то есть является должником.

# Напишите программу, которая при вводе десяти чисел определяет, сколько из них являются одновременно чётными и положительными.

plus_customer = 0

for i in range(10):
 customer = int(input('Введите порядковые номера владельцев счетов: '))
 if customer > 0 and customer % 2 == 0:
  plus_customer += 1
  
print(f'Колличество должников: {plus_customer}')