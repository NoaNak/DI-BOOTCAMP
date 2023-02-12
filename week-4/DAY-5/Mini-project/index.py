# cells

    ################
    # 1 #  2  #  3 #
    ################
    # 4 #  5  #  6 #
    ################
    # 7 #  8  #  9 #
    ################

# rows and columns

#      1    2    3
    ################
#1  #    #   #     #
    ################
#2  #    #   #     #
    ################
#3  #    #   #     #
    ################

# 9 choices - 
 
# dict I - {1(cell): , 2: , 3: ,4: ...}

# dict II - {1(row): {1(column): ,2(column):, 3(column):},
#            2(row): {1: , 2: , 3:},
#            3(row): {1:, 2:, 3:}}

# list - [1(cell), 2, 3, 4, 5, 6, 7, 8, 9]


choices = [0, 1, 2, 3, 4, 5, 6, 7, 8]


def display_board(choices) -> None:
    board_gui = f"""
    #############
    # {choices[0]} # {choices[1]} # {choices[2]} #
    #############
    # {choices[3]} # {choices[4]} # {choices[5]} #
    #############
    # {choices[6]} # {choices[7]} # {choices[8]} #
    #############
    """
    print(board_gui)



def switch_players(player: str) -> str:
    if player == 'X':
        return 'O'
    else:
        return 'X'

display_board(choices)


def player_input(player: str) -> None:

    player_choice = None

    while player_choice not in choices:
        player_choice = int(input(f"Player {player} Your choice: ")) # 1

    print("Player chose:", player_choice)

    choices[player_choice] = current_player # X/O

    display_board(choices)



################
# 0 #  1  #  2 #
################
# 3 #  4  #  5 #
################
# 6 #  7  #  8 #
################

def player_win(player: str): # X / O
    
    player_win = [player, player, player]

    choices1 = choices[0:3] # first row
    choices2 = choices[3:6] # second row
    choices3 = choices[6:] # third row
    
    choices4 = choices[0::4] # first diagonal
    choices5 = choices[2:7:2] # second diagonal

    choices6 = choices[0:7:3]
    choices7 = choices[1:8:3]
    choices8 = choices[2::3]

    if player_win == choices1 or player_win == choices2 or player_win == choices3 or player_win == choices4 or player_win == choices5 or player_win == choices6 or player_win == choices7 or player_win == choices8:
        print(f'{player}: You win !!')
        return True
    else:
        return None


current_player = 'X'
winner = None

while winner == None:
    player_input(current_player)
    winner = player_win(current_player)
    if winner:
        break
    current_player = switch_players(current_player)
    