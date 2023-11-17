board_positions =[[1, 2, 3], 
                [4, 5, 6],
                [7, 8, 9]]

def drawing_board():

    print(board_positions[0][0], '|', board_positions[0][1], '|', board_positions[0][2])
    print('_________')
    print(board_positions[1][0], '|', board_positions[1][1], '|', board_positions[1][2])
    print('_________')
    print(board_positions[2][0], '|', board_positions[2][1], '|', board_positions[2][2])
    


def set_positions():
    select_x = 'O'
    select_o = 'X'
    player1 = str(input('Enter name of player 1: '))
    player2 = str(input('Enter name of player 2: '))

  
    game = True
    current_player = player1
    total_moves = 0

    while game: 
        drawing_board() 
        if current_player == player1:
            symbol = select_x
        else:
            symbol = select_o

        if current_player == player1: 
            position = int(input(player1 + ', Pick a position by entering a number: '))
        else: 
            position = int(input(player2+ ', Pick a position by entering a number: '))

        if position >= 1 and position <= 9: 
            row = (position - 1) // 3
            col = (position - 1) % 3
            if board_positions[row][col] == 'X' or board_positions[row][col] == 'O':
                print('taken. choose other')
            else:
                board_positions[row][col] = symbol
                if total_moves == 9:
                    drawing_board()
                    print('That is a tie!')
                    game = False
                if board_positions[0][0] == board_positions[0][1] == board_positions[0][2] or \
                   board_positions[1][0] == board_positions[1][1] == board_positions[1][2] or \
                   board_positions[2][0] == board_positions[2][1] == board_positions[2][2]:
                    drawing_board()
                    print(f'Congrats, {current_player}! You won!')
                    game = False
                elif board_positions[0][0] == board_positions[1][0] == board_positions[2][0] or \
                     board_positions[0][1] == board_positions[1][1] == board_positions[2][1] or \
                     board_positions[0][2] == board_positions[1][2] == board_positions[2][2]:
                    drawing_board()
                    print(f'Congrats, {current_player}! You won!')
                    game = False
                elif board_positions[0][0] == board_positions[1][1] == board_positions[2][2] or \
                     board_positions[0][2] == board_positions[1][1] == board_positions[2][0]:
                    drawing_board()
                    print(f'Congrats, {current_player}! You won!')
                    game = False
                

                if current_player == player1: 
                    current_player = player2
                else:
                    current_player = player1
        else:
            print('Invalid, choose another')
        
       
set_positions()


