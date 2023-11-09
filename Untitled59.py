#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import random


def create_board():
    board = [[' ' for _ in range(10)] for _ in range(10)]
    return board


def place_ships(board):
    ships = [4, 3, 3, 2, 2, 2, 1, 1, 1, 1] # количество кораблей каждой длины
    directions = [(0, 1), (1, 0)] # направления расстановки (горизонталь и вертикаль)

    for ship_length in ships:
        while True:
            x = random.randint(0, 9)
            y = random.randint(0, 9)
            direction = random.choice(directions)

            if can_place_ship(board, x, y, direction, ship_length):
                place_ship(board, x, y, direction, ship_length)
                break


def can_place_ship(board, x, y, direction, length):
    for i in range(length):
        new_x = x + i * direction[0]
        new_y = y + i * direction[1]

        if not is_valid_position(board, new_x, new_y) or board[new_x][new_y] != ' ':
            return False

    return True


def place_ship(board, x, y, direction, length):
    for i in range(length):
        new_x = x + i * direction[0]
        new_y = y + i * direction[1]
        board[new_x][new_y] = '@'


def is_valid_position(board, x, y):
    return x >= 0 and x < 10 and y >= 0 and y < 10


def update_board(board, x, y):
    if board[x][y] == '@':
        board[x][y] = 'X'
        print("Попадание!")
        if is_ship_sunk(board, x, y):
            print("Корабль потоплен!")
    elif board[x][y] == ' ':
        board[x][y] = '-'
        print("Промах!")
    else:
        print("Вы уже стреляли в эту клетку!")


def is_ship_sunk(board, x, y):
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    for direction in directions:
        length = get_ship_length(board, x, y, direction)
        if length >= 4:
            return True

    return False


def get_ship_length(board, x, y, direction):
    length = 1
    new_x = x + direction[0]
    new_y = y + direction[1]

    while is_valid_position(board, new_x, new_y) and board[new_x][new_y] == '@':
        length += 1
        new_x += direction[0]
        new_y += direction[1]

    return length


def print_board(board):
    print("  A B C D E F G H I J")
    print(" ┌─" + "─┬─" * 9 + "─┐")

    for i in range(10):
        row = str(i) + '│'
        for j in range(10):
            row += ' ' + board[i][j] + '│'
        print(row)
        print(" ├─" + "─┼─" * 9 + "─┤")

    print(" └─" + "─┴─" * 9 + "─┘")


def play_game():
    board = create_board()
    place_ships(board)

    while True:
        print_board(board)
        coordinates = input("Введите координаты выстрела (например, A5): ")
        x, y = convert_coordinates(coordinates)

        if not is_valid_position(board, x, y):
            print("Некорректные координаты!")
            continue

        update_board(board, x, y)

        if is_game_over(board):
            print("Игра окончена!")
            break


def is_game_over(board):
    for row in board:
        if '@' in row:
            return False
    return True


def convert_coordinates(coordinates):
    x = int(coordinates[1])
    y = ord(coordinates[0].upper()) - ord('A')
    return x, y

# Запуск игры
play_game()


# In[ ]:




