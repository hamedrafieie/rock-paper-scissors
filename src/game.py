import random


class RockPaperScissors:
    """
    Main class for the game Rock, Paper, Scissors
    """
    def __init__(self):
        self.choices = ['Rock', 'Paper', 'Scissors']
    
    def get_user_choice(self) ->str:
        '''
        This method takes the user's choice using a simple 
        input function and passes it to user_choice variable
        '''
        
        user_choice = input(f"Please enter your choice from {self.choices}").capitalize()
        
        if user_choice not in self.choices:
            print("invalid")
        else:
            return user_choice
    
    def get_computer_choice(self):
        '''uses choice method from random library to get computers choice'''
        return random.choice(self.choices)
        
    def dicide_winner(self, computer_choice: str, user_choice: str) -> str:
        '''Method to decide game winner based on the rules.

        :param user_choice: The user's choice
        :param computer_choice: The computer's choice
        :return: Game outcome as a string
        '''
        winner_combinations = [('Rock', 'Scissors'), ('Paper', 'Rock'), ('Scissors', 'Paper')]

        if computer_choice == user_choice:
            return "tie"
        
        else:
            for winner_comb in winner_combinations:
                if user_choice == winner_comb[0] and computer_choice == winner_comb[1]:
                    return "you win"

                else:
                    return "you lose"
            
    def play(self):
        '''The main method to play the game'''
        computer_choice = self.get_computer_choice()
        user_choice = self.get_user_choice()
        result = self.dicide_winner(computer_choice, user_choice)
        print(f"Computer chose {computer_choice}. {result}")


game = RockPaperScissors()


while True:
        game.play()
        continue_game = input("Do you want to play again? (Enter any key to continue or 'q' to quit): ")
        if continue_game.lower() == 'q':
            break


if __name__ == "__main__":
    play()