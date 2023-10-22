

# Создание игрового поля
board = [[' ' for _ in range(5)] for _ in range(4)]

# Функция для отображения игрового поля
def display_board():
    for row in board:
        print('|'.join(row))
        print('-' * 9)

# Функция для проверки, является ли клетка допустимой
def is_valid_move(row, col):
    if row < 0 or row >= 4 or col < 0 or col >= 5:
        return False
    if board[row][col] != ' ':
        return False
    return True

# Функция для подсчета штрафных очков
def calculate_penalty(player):
    penalty = 0
    for row in range(4):
        for col in range(5):
            if board[row][col] == player:
                if row > 0 and board[row-1][col] == player:
                    penalty += 1
                if row < 3 and board[row+1][col] == player:
                    penalty += 1
                if col > 0 and board[row][col-1] == player:
                    penalty += 1
                if col < 4 and board[row][col+1] == player:
                    penalty += 1
    return penalty

# Основной код игры
players = ['X', 'O', 'Y']
current_player = 0

while True:
    display_board()
    print(f"Ход игрока {players[current_player]}")
    
    # Запрос хода у текущего игрока
    while True:
        row = int(input("Введите номер строки (от 1 до 4): ")) - 1
        col = int(input("Введите номер столбца (от 1 до 5): ")) - 1
        if is_valid_move(row, col):
            break
        else:
            print("Некорректный ход. Попробуйте снова.")
    
    # Заполнение клетки символом текущего игрока
    board[row][col] = players[current_player]
    
    # Проверка окончания игры
    if all(board[row][col] != ' ' for row in range(4) for col in range(5)):
        break
    
    # Переход к следующему игроку
    current_player = (current_player + 1) % 3

# Определение победителя
penalties = [calculate_penalty(player) for player in players]
min_penalty = min(penalties)
winners = [players[i] for i in range(3) if penalties[i] == min_penalty]

# Вывод результатов игры
print("Игра окончена!")
display_board()
if len(winners) == 1:
    print(f"Победитель: Игрок {winners[0]}")
else:
    print("Ничья!")
