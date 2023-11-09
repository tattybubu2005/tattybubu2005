#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from random import randint

# функция для создания игрового поля
def create_board():
    board = []
    for _ in range(3):
        row = [randint(1, 9) for _ in range(3)]
        board.append(row)
    return board

# функция для вывода игрового поля
def print_board(board):
    for row in board:
        print(row)

# функция для проверки возможности хода
def check_move(board, move, last_move):
    if move == "row":
        for i in range(3):
            if board[last_move[0]][i] != 0:
                return True
    elif move == "column":
        for i in range(3):
            if board[i][last_move[1]] != 0:
                return True
    return False

# функция для выполнения хода
def make_move(board, move, last_move, player_sum):
    if move == "row":
        options = [board[last_move[0]][i] for i in range(3) if board[last_move[0]][i] != 0]
    elif move == "column":
        options = [board[i][last_move[1]] for i in range(3) if board[i][last_move[1]] != 0]
    
    print("Available options:", options)
    chosen_number = int(input("Choose a number: "))
    
    if chosen_number not in options:
        print("Invalid choice. Please choose a valid number.")
        make_move(board, move, last_move, player_sum)
    else:
        options.remove(chosen_number)
        if move == "row":
            board[last_move[0]][options.index(chosen_number)] = 0
        elif move == "column":
            board[options.index(chosen_number)][last_move[1]] = 0
        player_sum += chosen_number
    
    return player_sum

# основная функция игры
def play_maxit():
    board = create_board()
    print("Initial board:")
    print_board(board)
    
    player1_sum = 0
    player2_sum = 0
    last_move = [-1, -1]  # начинаем с пустого хода
    
    while True:
        player1_sum = make_move(board, "row", last_move, player1_sum)
        print("Player 1 sum:", player1_sum)
        
        if not check_move(board, "column", last_move):
            print("Player 2 has no valid moves. Player 1 wins!")
            break
        
        player2_sum = make_move(board, "column", last_move, player2_sum)
        print("Player 2 sum:", player2_sum)
        
        if not check_move(board, "row", last_move):
            print("Player 1 has no valid moves. Player 2 wins!")
            break
        
        last_move = [options.index(chosen_number), last_move[1]] if len(options) > 0 else [last_move[0], options.index(chosen_number)]
    
    if player1_sum == player2_sum:
        print("It's a tie!")
    elif player1_sum > player2_sum:
        print("Player 1 wins with a sum of", player1_sum)
    else:
        print("Player 2 wins with a sum of", player2_sum)

# запуск игры
play_maxit()


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




