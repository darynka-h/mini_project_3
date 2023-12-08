field = ['.....',   #0
         '.....', 
         '...XX', #2
         '..X..', 
         '.....'] 
player = 2
figure = ['**']
players_dict = {1: "o", 2: "x"}
player_figure = []
for row in figure:
    line = ""
    for element in row:
        if element == "*":
            line += players_dict[player]
        else:
            line += element
player_figure.append(line)
line = ""
for i, field_row in enumerate(field):
    # проходжусь по кожному елемену поля
        for j, field_element in enumerate(field_row.lower()):
        # якщо елемент == значку, яким грає гравець, то я визначаю його індекс
            if field_element == players_dict[player] and field_element in field_row:
                # debug(f"Info about the field УДУЬУТЕ{field_element}")
                # якщо довжина шматку від цього елементу до кінця ігрового поля
                # менше за довжину одного рядка фігури, то нікого не ставимо, продовжуємо далі
            # коунтер для прорахунку кількості співпадінь з ноликом чи одиничкою
                counter = 0
                try:
                    # проходжусь по елементам фігури
                    for k, row in enumerate(figure):
                        for l_, element in enumerate(row):
                            # якщо відповідний елемент поля == відповідному елементу фігкри
                            # та цей елемент == фігурі, якою грає гравець, 
                            # то збільшуємо цей каунтер
                            if field[i + k][j + l_] == figure[k][l_] and field[i + k] == players_dict[player]:
                                # debug(f"Info about the field {field[i + k][j + l_]}{figure[k][l_]}")
                                counter += 1
                    # якщо співпадінь білше, ніж одне, фдемо далі
                    if counter > 1:
                        continue
                    # якщо співданяння рівно одне, то повертаємо цю координату 
                    elif counter == 1:
                        print(i, j)
                except IndexError:
                    continue
                if field_element == players_dict[player]:
                    print(i, j)