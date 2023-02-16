from game import Game

def get_user_menu_choice():
    user_choice = input("For a new game press 1, to see your score press 2, to quit press 3 ")
    while user_choice not in ["1", "2", "3"]:
        print("INVALID CHOICE TRY AGAIN !")
    return user_choice
    

def print_results(results):
    print(f'Game result: WIN {results["WIN"]}, LOOSE{results["LOOSE"]}, DRAW{results["DRAW"]}')
    
def main():
    choice = get_user_menu_choice()
    while choice != "3":
        if choice == "1":
            new_game = Game()
            new_game.play()
        else:
            print_results('results')
    print("Thank you for player goodbye !")

main()





