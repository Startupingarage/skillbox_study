print('Задача 5. Недоделка')

# Вы пришли на работу в компанию по разработке игр, целевая аудитория — дети и их родители.
# У предыдущего программиста было задание сделать две игры в одном приложении, чтобы пользователь мог выбирать одну из них.
# Однако программист, на место которого вы пришли, перед увольнением не успел выполнить эту задачу и оставил только небольшой шаблон проекта.

# Правила игры «Камень, ножницы, бумага»:
# программа запрашивает у пользователя строку и выводит, победил он или проиграл.
# Камень бьёт ножницы, ножницы режут бумагу, бумага кроет камень.

# Правила игры «Угадай число»:
# программа запрашивает у пользователя число до тех пор, пока он не угадает загаданное.

# Используя этот шаблон проекта, реализуйте игры «Камень, ножницы, бумага» и «Угадай число».
def rock_paper_scissors():
    while True:
        player_1_choice = input('Первый игрок, выберите "Камень", "Ножницы" или "Бумага": ').lower().strip()
        if player_1_choice != 'камень' and player_1_choice != 'ножницы' and player_1_choice != 'бумага':
            print('Неверный выбор! Попробуйте снова.')
        else:
            break

    while True:
        player_2_choice = input('Второй игрок, выберите "Камень", "Ножницы" или "Бумага": ').lower().strip()
        if player_2_choice != 'камень' and player_2_choice != 'ножницы' and player_2_choice != 'бумага':
            print('Неверный выбор! Попробуйте снова.')
        else:
            break

    if player_1_choice == player_2_choice:
        print('Ничья!')
    elif (player_1_choice == 'камень' and player_2_choice == 'ножницы') or \
         (player_1_choice == 'ножницы' and player_2_choice == 'бумага') or \
         (player_1_choice == 'бумага' and player_2_choice == 'камень'):
        print('Игрок 1 победил!')
    else:
        print('Игрок 2 победил!')
    

def guess_the_number():
    guess = int(input('Загадайте число: '))
    req = None
    while req != guess:
        req = int(input('Угадайте число: '))
        if req != guess:
            print('Не угадали, попробуйте снова!')
    print('Вы угадали!')


def main_menu():
    choise = int(input('Выберите игру\n1 — "Камень, ножницы, бумага", 2 — "Угадай число":\n'))
    if choise == 1:
        rock_paper_scissors()
    elif choise == 2:
        guess_the_number()
    else:
        print('Введите корректное значение.')
        main_menu()


main_menu()