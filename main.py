import random


# Create a game that allows players to choose between multiple characters
# and fight against each other. The game should have a simple combat system
# where characters can deal damage to each other. The game should also have
# a way to display the current health of each character.

# The game should have turned based combat where each player takes turns
# Players should have an attack, defense, and health stat

# Combat should involve a level of randomness.

# The game should have a way to display the current health of each character after each turn.

# Combat should continue until one of the characters health reaches 0.

# The game should have a way to display the winner of the game.

# The game should have a way to restart the game.

# The game should have a way to exit the game.

from player import jacob
from player import demon
from player import warden
from player import angel

class Game:
    def __init__(self):
        """Initializes the game,
        It should give the game a list of at least 4 characters to choose from
        It should also give the game a list of moves for each character
        It should show player a list of characters to choose from
        and allow them to select a character,
        then have the computer choose a character at random
        It should randomly select a player to go first"""

    def turn(self):
        """This method should show the current health of both players, 
        and allow the player to select a move to use on the opponent
        If it is the computer player's turn, it should select a move at random"""
        
        if self.player_turn:
            for attack in self.player.move_list.keys():
                print(attack)
            move = input("Pick your attack! : ")

        else:
            move = None
            #move = input("Pick your attttack")
        for attack in self.player.move_list.keys():
            print(attack)

        if move == "quit":
            self.exit()
        elif move == "r":
            self.playing = False

        self.player_turn = not self.player_turn

    def check_winner(self):
        """This method should check if either player's health has reached 0
        If a player's health has reached 0, it should display the winner"""
        pass

    def restart(self):
        """This method should allow the player to restart the game"""
        pass

    def exit(self):
        """This method should allow the player to exit the game"""
        pass

    def run(self):
        self.player_turn = random.choice([True, False])
        player_choice = input("Choose your character!")

        if player_choice == "1":
            self.player = warden
        if player_choice == "2":
            self.player = angel
        if player_choice == "3":
            self.player = demon
        if player_choice == "4":
            self.player = jacob

        self.playing = True
        while self.playing:
            self.turn()
            self.check_winner()
    
def main():
    game = Game()
    game.run()
    

main()



