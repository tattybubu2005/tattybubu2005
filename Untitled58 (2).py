#!/usr/bin/env python
# coding: utf-8

# In[ ]:




def print_board(board):
    for row in board:
        print(' '.join(row))

def check_winner(board, player):
    for i in range(len(board)):
        if board[0][i] == player and board[4][i] == player:
            return True
    return False

def play_game():
    board = [[' ' for _ in range(5)] for _ in range(5)]
    players = ['X', 'O']
    current_player = 0
    print_board(board)
    
    while True:
        print('Ход игрока', players[current_player])
        row1 = int(input('Введите номер строки первого камня (0-3): '))
        col1 = int(input('Введите номер столбца первого камня (0-4): '))
        row2 = int(input('Введите номер строки второго камня (0-3): '))
        col2 = int(input('Введите номер столбца второго камня (0-4): '))
        
        if row1 == row2 and abs(col1 - col2) == 1:  # Горизонтальный мостик
            board[row1][min(col1, col2)] = '-'
            board[row1][max(col1, col2)] = '-'
        elif col1 == col2 and abs(row1 - row2) == 1:  # Вертикальный мостик
            board[min(row1, row2)][col1] = '|'
            board[max(row1, row2)][col1] = '|'
        else:
            print('Введены некорректные координаты, попробуйте снова.')
            continue
        
        print_board(board)
        
        if check_winner(board, players[current_player]):
            print('Игрок', players[current_player], 'победил!')
            break
        
        current_player = (current_player + 1) % 2

play_game()


# In[ ]:




