#!/usr/bin/env python
# coding: utf-8

# In[ ]:



def create_board():
    """
    Создает пустое игровое поле размером 10 на 10.
    """
    board = []
    for _ in range(10):
        row = ['-'] * 10
        board.append(row)
    return board

def display_board(board):
    """
    Отображает текущее состояние игрового поля.
    """
    for row in board:
        print(' '.join(row))

def make_move(board, player, row, col):
    """
    Выставляет отметку игрока в указанной клетке.
    """
    board[row][col] = player

def is_winner(board, player):
    """
    Проверяет, есть ли выигрышное состояние для игрока.
    """
    directions = [(0, 1), (1, 0), (1, 1), (-1, 1)]

    for row in range(10):
        for col in range(10):
            if board[row][col] == player:
                for dir in directions:
                    count = 1
                    dx, dy = dir
                    x, y = row + dx, col + dy

                    while 0 <= x < 10 and 0 <= y < 10 and board[x][y] == player:
                        count += 1
                        x += dx
                        y += dy

                        if count >= 3:
                            return True

    return False

def play_game():
    """
    Запускает игру "Клондайк" для 2 игроков.
    """
    board = create_board()
    players = ['X', 'O']
    curr_player = 0

    while True:
        display_board(board)
        print("Ход игрока", players[curr_player])

        # Ввод координат клетки
        row = int(input("Введите номер строки (от 1 до 10): ")) - 1
        col = int(input("Введите номер столбца (от 1 до 10): ")) - 1

        if 0 <= row < 10 and 0 <= col < 10 and board[row][col] == '-':
            make_move(board, players[curr_player], row, col)

            if is_winner(board, players[curr_player]):
                display_board(board)
                print("Игрок", players[curr_player], "победил!")
                break

            curr_player = (curr_player + 1) % 2
        else:
            print("Введены некорректные координаты или клетка уже занята. Попробуйте еще раз.")

play_game()


# In[ ]:




