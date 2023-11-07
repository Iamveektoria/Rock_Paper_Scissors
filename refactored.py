"""This program plays a game of Rock, Paper, Scissors between two Players,
and reports both Player's scores each round."""


# Importing needed modules
import random
import time


# List of moves available
moves = ['rock', 'paper', 'scissors']


# Prints statement slower by a second
def print_pause(statement):
    time.sleep(1)
    print(statement)


# Print texts in yellow
def print_yellow(statement):
    YELLOW = "\033[33m"
    RESET = "\033[0m"
    print_pause(YELLOW + statement + RESET)


# Prints texts in red
def print_red(statement):
    RED = "\033[31m"
    RESET = "\033[0m"
    print_pause(RED + statement + RESET)


# Prints text in green
def print_green(statement):
    GREEN = "\033[32m"
    RESET = "\033[0m"
    print_pause(GREEN + statement + RESET)


# Validates human input
def validate_user_input(human_input, is_valid):
    while human_input not in is_valid:
        if quit(human_input):
            break
        human_input = input("Enter a valid input!\n").lower()
        if human_input in is_valid:
            break

    return human_input


# Checks if a Player is human
def isHumanPlayer(the_player, human):
    return isinstance(the_player, human)


# Askes the human player how many time he/she wants to play
def num_rounds():

    round_amount = input("How many rounds do you want to play? (1 or 3)\n")
    while round_amount != "1" and round_amount != "3":
        round_amount = input("You can either play once or"
                             " thrice! Enter 1 or 3\n")
        if round_amount == "1" or round_amount == "3":
            break
    return round_amount


# This function change the words for the game play
# depending on if theres a human player
def game_style(function):
    round = 1
    while True:
        if round < 4:
            if round == 3:
                print_green(f"Final round:")
                round += 1
                if function() == "q":
                    return "q"
            else:
                print_green(f"Round {round}:")
                round += 1
                if function() == "q":
                    return "q"
        else:
            break


# This function prints the score of each players when called
def print_score(p1_score, p2_score, what_score, p1):
    if isHumanPlayer(p1, HumanPlayer):
        print_yellow(f"\n{what_score} --")
        print_pause(f"Your score: {p1_score}")
        print_pause(f"Opponent score: {p2_score}\n")
    else:
        print_yellow(f"\n{what_score} --")
        print_pause(f"Player1 score: {p1_score}")
        print_pause(f"Player2 score: {p2_score}\n")

# Prints out the final winner


def who_won(p1_score, p2_score, p1):
    if p1_score == p2_score:
        print("The game ended in a TIE! No player won.\n")
    elif p1_score > p2_score:
        if isHumanPlayer(p1, HumanPlayer):
            print("You are the final winner!\n")
        else:
            print("Player1 is the final winner!\n")
    else:
        if isHumanPlayer(p1, HumanPlayer):
            print("Your opponent is the final winner!\n")
        else:
            print("Player2 is the final winner!\n")

# Checks if a human player wants to quit


def quit(reply):
    if reply == "q":
        return True


# Returns True if player1 wins else False
# which implies player2 won or it's a TIE!
def beats(one, two):
    return ((one == 'rock' and two == 'scissors') or
            (one == 'scissors' and two == 'paper') or
            (one == 'paper' and two == 'rock'))


# The Player class is the parent class
# for all of the Players in this game
class Player:

    def __init__(self):
        self.score = 0
        self.my_move = None
        self.their_move = None

    def move(self):
        return 'rock'

    def learn(self, my_move, their_move):
        pass


# This player always plays Rock.
class AllRockPlayer(Player):
    pass


# A kind of player that generates moves at random
class RandomPlayer(Player):
    def __init__(self):
        super().__init__()

    def move(self):
        return random.choice(moves)


# A human player! the player plays the game by inputting choice
class HumanPlayer(Player):
    def __init__(self):
        super().__init__()
        self.human_choice = ""

    def move(self):
        self.human_choice = input(
            "rock, paper or scissors?\nYou "
            "can also enter 'q' to quit. \n").lower()
        return validate_user_input(self.human_choice, moves)


# A kind of player whose current move is always
# equal to the opponents previous move
# The players initial move is set to rock and
# then it learns the opponents move as the
# game play continues."""
class ReflectPlayer(Player):
    def __init__(self):
        super().__init__()
        self.my_prev_mood = ""
        self.my_move = random.choice(moves)

    def move(self):
        return self.my_move

    def learn(self, my_move, their_move):
        self.my_move = their_move
        self.my_prev_mood = my_move


# A kind of player that set to a
# move from the move list from 0 to 2
# accordingly using % 3
class CyclePlayer(Player):
    def __init__(self):
        super().__init__()
        self.my_move = random.choice(moves)
        self.current_index = 0

    # The move method cycles this players move according to the list
    # No matter where it starts from! It just keeps
    # increasing the index position till it gets
    # to the end of the list and starts again from zero
    def move(self):
        return moves[(moves.index(self.my_move) + 1) % len(moves)]

    def learn(self, my_move, their_move):
        self.my_move = my_move


# This is where the game play starts!
class Game:
    # Initiallizes variables to be used
    def __init__(self, p1, p2, plays_num):

        if isHumanPlayer(p1, HumanPlayer):
            self.p1 = p1
            self.p2 = p2
        elif isHumanPlayer(p2, HumanPlayer):
            self.p1 = p2
            self.p2 = p1
        elif (not isHumanPlayer(p1, HumanPlayer) and
              not isHumanPlayer(p2, HumanPlayer)):
            self.p1 = p1
            self.p2 = p2

        self.plays_num = plays_num

    # This method is called if the player wants to play once
    def play_single_round(self, function):
        print_green("Only Round --")
        # function()
        if not quit(function()):
            print_green("Thats the end!")
            print_score(self.p1.score, self.p2.score,
                        "FINAL SCORE", self.p1)
            who_won(self.p1.score, self.p2.score, self.p1)

    # This method is called if the player wants to play thrice
    def play_three_rounds(self, style):
        if isHumanPlayer(self.p1, HumanPlayer):
            print("\nRock Paper Scissors, Go! \n")
            result_from_game_style = game_style(style)
        else:
            print("\nGame start!\n")
            result_from_game_style = game_style(style)

        return result_from_game_style

    # This function takes care of the game play each round
    # and also considers if the player would like to quit!"""
    def play_round(self):
        move1 = self.p1.move()
        move2 = self.p2.move()

        if move1 == "q" or move2 == "q":
            print_pause("\nYou lost by quitting.")
            print_pause("Bye!")
            return "q"

        elif move1 != "q" and move2 != "q":

            if isHumanPlayer(self.p1, HumanPlayer):
                print_pause(f"You: {move1}  Opponent: {move2}")
            else:
                print_pause(f"Player1: {move1}  Player2: {move2}")

            if move1 == move2:
                print_pause("** TIE **")
                print_pause(f"{move1} doesn't beat {move2}")
                print_pause("No player won this round")
                print_score(self.p1.score, self.p2.score,
                            "Current score", self.p1)

            elif beats(move1, move2):
                self.p1.score += 1
                if isHumanPlayer(self.p1, HumanPlayer):
                    print_pause(f"{move1} beats {move2}")
                    print_pause("You won this round!")
                    print_score(self.p1.score, self.p2.score,
                                "Current score", self.p1)

                else:
                    print_pause(f"{move1} beats {move2}")
                    print_pause("Player 1 won this round!")
                    print_score(self.p1.score, self.p2.score,
                                "Current score", self.p1)

            else:
                self.p2.score += 1
                print_pause(f"{move2} beats {move1}")
                if isHumanPlayer(self.p1, HumanPlayer):
                    print_pause("Your opponent won this round!")
                else:
                    print_pause("Player 2 won this round")
                print_score(self.p1.score, self.p2.score,
                            "Current score", self.p1)

        # Calls the learn method to make the players
        # learn about the moves where applicable
        self.p1.learn(move1, move2)
        self.p2.learn(move2, move1)

    # This starts the game in a different way
    # depending on if theres a human player
    # It also announces game over/ who won!
    def play_game(self):
        result_from_game_style = ''
        if self.plays_num == "1":
            self.play_single_round(self.play_round)
        else:
            result_from_game_style = self.play_three_rounds(self.play_round)

        # If it gets to this part of the code, it means
        # The user did not quit and played thrice
        if result_from_game_style != "q" and self.plays_num != "1":
            print_red("Game over!")
            print_score(self.p1.score, self.p2.score, "FINAL SCORE", self.p1)
            who_won(self.p1.score, self.p2.score, self.p1)


if __name__ == '__main__':
    opponents = {
        '1': AllRockPlayer,
        '2': RandomPlayer,
        '3': ReflectPlayer,
        '4': CyclePlayer,
        '5': HumanPlayer
    }
    print("Player list:")
    for key, value in opponents.items():
        print(f"{key}. {value.__name__}")
    choose_player1 = input(f"Choose player 1:\n")
    p1 = opponents[validate_user_input(choose_player1, opponents)]
    choose_player2 = input(f"Choose player 2:\n")
    p2 = opponents[validate_user_input(choose_player2, opponents)]
    plays_num = num_rounds()
    game = Game(p1(), p2(), plays_num)
    game.play_game()
