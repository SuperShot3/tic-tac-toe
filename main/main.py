import random


empty_cell = '~'
game_board = [empty_cell for x in range(0, 9)]
current_player = "X"
winner = None
game_running = True


# create board
def print_board(board):
    if game_running and winner is None:
        print(f'Now Move of {current_player}')
    print("–" * 20)
    print(board[0] + '   |   ' + board[1] + '   |   ' + board[2])
    print(board[3] + '   |   ' + board[4] + '   |   ' + board[5])
    print(board[6] + '   |   ' + board[7] + '   |   ' + board[8])
    print("–" * 20)


# take input
def user_move(board):
    global game_running
    try:
        inp = int(input("Please enter number from 1 to 9: "))
        if inp in range(0, 10) and board[inp - 1] == empty_cell:
            board[inp - 1] = current_player
            check_winner()
            check_tie()
            switch_player()
        else:
            print('Cell is occupied try again\n')
    except ValueError:
        print("Value Error Try Again")


# check if winning combination exist on game_board Vertical Horizontal Diagonal
def horizontal(board):
    global winner
    if all([cell == current_player for cell in [board[0], board[1], board[2]]]):
        winner = current_player
        return True
    elif all([cell == current_player for cell in [board[3], board[4], board[5]]]):
        winner = current_player
        return True
    elif all([cell == current_player for cell in [board[6], board[7], board[8]]]):
        winner = current_player
        return True


def vertical(board):
    global winner
    if all([cell == current_player for cell in [board[0], board[3], board[6]]]):
        winner = current_player
        return True
    elif all([cell == current_player for cell in [board[1], board[4], board[7]]]):
        winner = current_player
        return True
    elif all([cell == current_player for cell in [board[2], board[5], board[8]]]):
        winner = current_player
        return True


def diagonal(board):
    global winner
    if all([cell == current_player for cell in [board[0], board[4], board[8]]]):
        winner = current_player
        return True
    elif all([cell == current_player for cell in [board[2], board[4], board[6]]]):
        winner = current_player
        return True


# check Tie
def check_tie():
    global game_running
    if empty_cell not in game_board and game_running:
        print('Is a Tie')
        game_running = False


# Check Winner
def check_winner():
    global game_running
    if vertical(game_board) or horizontal(game_board) or diagonal(game_board):
        game_running = False
        print_board(game_board) # Print board to display last move
        print(f'Winner is {current_player}')


# switch player
def switch_player():
    global current_player
    if current_player == 'X':
        current_player = '0'
    else:
        current_player = 'X'


# computer
def computer(board):
    corners = [0, 2, 6, 8]
    center = 4
    first_move = True
    second_move = True

    while current_player == '0':
        position = random.randint(0, 8)
        random_conner = random.choice(corners)
        # First move always corner
        if empty_cell in board[random_conner] and first_move:
            board[random_conner] = '0'
            first_move = False
            switch_player()
        elif second_move and board[center] == empty_cell:
            board[center] = '0'
            switch_player()
        else:
            board[position] = empty_cell
            board[position] = '0'


# Run a  game
while game_running:
    print_board(game_board)
    user_move(game_board)
    computer(game_board)
    check_winner()
    check_tie()
