from random import choice

class Game:

    def __init__(self):
        self.user = self.get_user_item()
        self.computer = self.get_computer_item()

    def get_user_item(self):
            user_response = input("Select an item: rock, paper or scissors)")
            while user_response not in "rock" | "paper" | "scissors":
                print("Invalid item")
            return user_response

    def get_computer_item(self):
        return choice(["rock", "paper", "scissors"])

    def get_game_result(self):
        if self.user == "rock" and self.computer == "paper" or self.user == "paper" and self.computer == "scissors" or self.user == "scissors" and self.computer == "rock":
            return "YOU WIN"
        elif self.user == self.computer:
            return "DRAW"
        return "COMPUTER WINS"

    def play(self):
        print(f'You choose {self.user} and the computer choose {self.computer} result{self.get_game_result()}')
        return self.get_game_result()


