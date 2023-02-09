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
def display_board(choices):
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
def switch_players(player: str):
    if player == 'X':
        return 'O'
    else:
        return 'X'
def player_input(player):
    player_choice = None
    while player_choice not in choices:
        player_choice = int(input(f"Player {player} Your choice: "))
    print("Player chose:", player_choice)
    choices[player_choice] = current_player
    display_board(choices)
while "i" not in "":
    current_player = 'X'
    player_input(current_player)
    current_player = switch_players(current_player)
    player_input(current_player)









