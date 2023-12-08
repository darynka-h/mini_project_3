#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
    This is an example of a bot for the 3rd project.
    ...a pretty bad bot to be honest -_-
    СТАИВИТЬ ФІГУРКУ, АЛЕ НЕ ВАЛІДНО
"""

from logging import DEBUG, debug, getLogger


# We use the debugger to print messages to stderr
# You cannot use print as you usually do, the vm would intercept it
# You can hovever do the following:
#
# import sys
# print("HEHEY", file=sys.stderr)

getLogger().setLevel(DEBUG)


def parse_field_info():
    """
    Parse the info about the field.

    However, the function doesn't do anything with it. Since the height of the field is
    hard-coded later, this bot won't work with maps of different height.

    The input may look like this:

    Plateau 15 17:
    """
    l = input()
    size = l.split()
    # debug(f"Description of the field: {int(size[1]), int(size[2][:-1])}")
    return int(size[1]), int(size[2][:-1])


def parse_field(player, size):
    """
    Parse the field.

    First of all, this function is also responsible for determining the next
    move. Actually, this function should rather only parse the field, and return
    it to another function, where the logic for choosing the move will be.

    Also, the algorithm for choosing the right move is wrong. This function
    finds the first position of _our_ character, and outputs it. However, it
    doesn't guarantee that the figure will be connected to only one cell of our
    territory. It can not be connected at all (for example, when the figure has
    empty cells), or it can be connected with multiple cells of our territory.
    That's definitely what you should address.

    Also, it might be useful to distinguish between lowecase (the most recent piece)
    and uppercase letters to determine where the enemy is moving etc.

    The input may look like this:

        01234567890123456
    000 .................
    001 .................
    002 .................
    003 .................
    004 .................
    005 .................
    006 .................
    007 ..O..............
    008 ..OOO............
    009 .................
    010 .................
    011 .................
    012 ..............X..
    013 .................
    014 .................


    The input may look like this:

        01234567890123456
    000 ..............x..
    001 .................
    002 .................
    003 .....oO..........
    004 .................
    005 .................

    # треба повернути прямокутник з крапочками
    :param player int: Represents whether we're the first or second player
    """
    # # move = None
    line = input()     # first row
    signs = ".xXoO"
    field = []
    for i in range(size[0]):
        line = input()
        row = ""
        for element in line:
            if element in signs:
                row += element
        if len(row) > 1:
            field.append(row)
        row = ""
    return field

    #     # if move is None:
    #     #     c = l.lower().find("o" if player == 1 else "x")
    #     #     if c != -1:
    #     #         move = i - 1, c - 4
    # # assert move is not None
    # # return move
    # return field

    # for row in size:
    #     line = ""
    #     for element in row:
    #         if element in signs:
    #             line += element
    #     if len(line) > 1:
    #         field.append(line)
    #         line = ""
    # return field


# print(parse_field(1, [3, 4]))


def parse_figure():
    """
    Parse the figure.

    The function parses the height of the figure (maybe the width would be
    useful as well), and then reads it.
    It would be nice to save it and return for further usage.

    The input may look like this:

    Piece 2 2:
    **
    ..

    # прочитати і зберегти фігуру
    """
    # l = input()
    # debug(f"Piece: {l}")
    # height = int(l.split()[1])
    # for _ in range(height):
    #     l = input()
    #     debug(f"Piece: {l}")
# ============================================
    piece = input()
    debug(f"Piece: {piece}")
    height = int(piece.split()[1])
    figure = []
    for _ in range(height):
        line = input()
        figure.append(line)
        debug(f"Piece: {line}")
    return figure


# print(parse_figure())

# def distance(x_1: float, y_1: float, x_2: float, y_2: float) -> float:
#     """Function parametrs are x and y coordinates of two points
#     Function returns distance between this points.
#     >>> distance(0, 0, 1, 2)
#     2.24
#     """
#     x_difference = x_1 - x_2
#     y_difference = y_1 - y_2
#     distance_ = (pow(x_difference, 2) + pow(y_difference, 2))**0.5
#     return round(distance_, 2)


def step(player: int):
    """
    # move = None
    # size = parse_field_info()
    # debug(f"Info about the field {size}")
    # field = parse_field(size)
    # parse_figure()
    # return (0, 0)
    Perform one step of the game.

    :param player int: Represents whether we're the first or second player
    """
    players_dict = {1: "o", 2: "x"}
    move = None
    size = parse_field_info()
    debug(f"Info about the field {size}")
    field = parse_field(player, size)
    debug(f"The field {field}")
    figure = parse_figure()
    debug(f"The field {figure}")
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
        # якщо елемент == о, то я визначаю його індекс
            if field_element == players_dict[player]:
                return (i, j)
    return 0, 0

# input()
# step(1)


def play(player: int):
    """
    Main game loop.

    :param player int: Represents whether we're the first or second player
    """
    while True:
        move = step(player)
        print(*move)


def parse_info_about_player():
    """
    This function parses the info about the player

    It can look like this:

    $$$ exec p2 : [./player1.py]
    """
    i = input()
    # debug(f"Info about the player: {i}")
    return 1 if "p1 :" in i else 2


def main():
    player = parse_info_about_player()
    try:
        play(player)
    except EOFError:
        debug("Cannot get input. Seems that we've lost ):")


if __name__ == "__main__":
    main()
