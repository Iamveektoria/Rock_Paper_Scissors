"""This program plays a game of Rock, Paper, Scissors between two Players,
and reports both Player's scores each round."""

# Importing needed modules
import random
import time

# Prints statement slower by a second


def print_pause(statement):
    time.sleep(1)
    print(statement)


# List of moves available
moves = ['rock', 'paper', 'scissors']

"""The Player class is the parent class for all of the Players
in this game"""


class Player:
    def move(self):
        return 'rock'

    def learn(self, my_move, their_move):
        pass

# A kind of player that generates moves at random


class RandomPlayer(Player):
    def move(self):
        return random.choice(moves)

# A human player! the player plays the game by inputting choice


class HumanPlayer(Player):
    def __init__(self):
        self.human_choice = ""
        self.moves = ["rock", "paper", "scissors", "q"]

    def move(self):
        self.human_choice = input(
            "rock, paper or scissors?\nYou "
            "can also enter 'q' to quit. ").lower()

        # Validates your input
        while self.human_choice not in self.moves:
            print_pause("You have to enter 'rock', 'paper' or 'scissors'")
            print("But if you want to quit enter 'q'")
            self.human_choice = input().lower()
            if self.human_choice in self.moves:
                break

        return self.human_choice


"""A kind of player whose current move is always
 equal to the opponents previous move
The players initial move is set to rock and
then it learns the opponents move as the
game play continues."""


class ReflectPlayer(Player):
    def __init__(self):
        self.my_prev_mood = ""
        self.my_move = "rock"

    def move(self):
        return self.my_move

    def learn(self, my_move, their_move):
        self.my_move = their_move
        self.my_prev_mood = my_move


"""A kind of player that set to a move from the move list from 0 to 2
accordingly using % 3"""


class CyclePlayer(Player):
    def __init__(self):
        self.tracker = -1

    def move(self):
        self.tracker += 1
        return moves[self.tracker % 3]

# This function returns True if player 1 wins else it returns False


def beats(one, two):
    return ((one == 'rock' and two == 'scissors') or
            (one == 'scissors' and two == 'paper') or
            (one == 'paper' and two == 'rock'))

# This is where the game play starts!


class Game:
    # Initiallizes variables to be used
    def __init__(self, p1, p2):

        if isinstance(p1, HumanPlayer):
            self.p1 = p1
            self.p2 = p2
        elif isinstance(p2, HumanPlayer):
            self.p1 = p2
            self.p2 = p1
        else:
            self.p1 = p1
            self.p2 = p2

        self.p1_score = 0
        self.p2_score = 0

    # Returns True if theres a human player else False

    def isHumanPlayer(self):
        if isinstance(self.p1, HumanPlayer):
            return True
        else:
            return False

    # Askes the human player how many time he/she wants to play
    def num_rounds(self):

        round_amount = input("How many rounds do you want to play? (1 or 3)\n")
        while round_amount != "1" and round_amount != "3":
            round_amount = input("You can either play once or"
                                 " thrice! Enter 1 or 3\n")
            if round_amount == "1" or round_amount == "3":
                break
        return round_amount

    # This function prints the score of each players when called

    def print_score(self):
        if self.isHumanPlayer():
            print_pause(f"Score: You {self.p1_score},"
                        f"Opponent {self.p2_score}")
        else:
            print_pause(
                f"Score: Player1 {self.p1_score}, Player2 {self.p2_score}")

    """This function takes care of the game play each round
    and also considers if the player would like to quit!"""

    def play_round(self):
        move1 = self.p1.move()
        move2 = self.p2.move()

        if move1 == "q" or move2 == "q":
            print_pause("You lost by quitting.")
            print_pause("Bye!")
            return "q"

        if self.isHumanPlayer():
            print_pause(f"You: {move1}  Opponent: {move2}")
        else:
            print_pause(f"Player 1: {move1}  Player 2: {move2}")

        if move1 == move2:
            print_pause("** TIE **")
            self.print_score()
        elif beats(move1, move2):
            self.p1_score += 1
            if self.isHumanPlayer():
                print_pause("You won!")
                self.print_score()
            else:
                print_pause("Player 1 won!")
                self.print_score()

        else:
            self.p2_score += 1
            print_pause("Player 2 won")
            self.print_score()

        """ Calls the learn method to make the players
         learn about the moves where applicable"""
        self.p1.learn(move1, move2)
        self.p2.learn(move2, move1)

    """This function change the words for the game
    play depending on if theres a human player"""

    def game_style(self):
        round = 1
        while True:
            if round < 4:
                if round == 3:
                    print_pause(f"Final round:")
                    round += 1
                    if self.play_round() == "q":
                        return "q"
                else:
                    print_pause(f"Round {round}:")
                    round += 1
                    if self.play_round() == "q":
                        return "q"
            else:
                break

    """This starts the game in a different way
    depending on if theres a human player
    It also announces game over/ who won!"""

    def play_game(self):
        result_from_game_style = ''
        if self.isHumanPlayer():
            if self.num_rounds() == "1":
                self.play_round()
            else:
                print("Rock Paper Scissors, Go! \n")
                result_from_game_style = self.game_style()
        else:
            print("Game start!")
            result_from_game_style = self.game_style()

        if result_from_game_style != "q":
            print("Game over!")

            if self.p1_score == self.p2_score:
                print("The game ended in a TIE! No player won.")
            elif self.p1_score > self.p2_score:
                if self.isHumanPlayer():
                    print("You are the overall winner!")
                else:
                    print("Player1 is the overall winner!")
            else:
                print("Player2 is the overall winner!")


if __name__ == '__main__':
    game = Game(ReflectPlayer(), RandomPlayer())
    game.play_game()
