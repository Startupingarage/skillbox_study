print('Задача 2. Коллекторы')

# Напишите робота для коллекторов.
# В самом начале он спрашивает имя должника и сумму долга,
# а затем начинает требовать у него погашения до тех пор, 
# пока он не введёт нужную сумму (равную сумме долга или больше).
# После погашения долга сообщите об этом пользователю и поблагодарите его.
 
# Пример:
# Василий, ваша задолженность составляет 100 рублей.
# Сколько рублей вы внесёте прямо сейчас, чтобы её погасить? 50
 
# Маловато, Василий. Давайте ещё раз.
# Сколько рублей вы внесёте прямо сейчас, чтобы её погасить? 90
# Маловато, Василий. Давайте ещё раз.
 
# Сколько рублей вы внесёте прямо сейчас, чтобы её погасить? 110
# Отлично, Василий! Вы погасили долг. Спасибо!


name = input("Введите ваше имя: ")
debt = int(input(f"{name}, ваша задолженность составляет: "))

while True:
    payment = int(input("Сколько рублей вы внесёте прямо сейчас, чтобы её погасить? "))
    
    if payment >= debt:
        print(f"Отлично, {name}! Вы погасили долг. Спасибо!")
        break
    else:
        print(f"Маловато, {name}. Давайте ещё раз.")