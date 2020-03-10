import win_condition as win

import random


# Task list

# This is only a user vs rand comp

# Start game


# create board object
class Hashtag:
    def __init__(self, num_of_turns=0, is_x_turn=None, board=None):
        self.num_of_turns = num_of_turns
        self.num_list = [10] * 9
        if is_x_turn is None:
            is_x_turn = True
        self.is_x_turn = is_x_turn
        if board is None:
            board = [" "] * 9
        self.board = board

    def clear_board(self):
        self.board = [None] * 9

    def loop_input(self):
        # TODO loop input
        pass

    def is_valid(self, index):
        """:returns bool"""

        if self.num_list[index] == 10:
            self.num_list[index] = index
            return True
        elif index in self.num_list:
            print(f"hey, {index} is not a valid input ")
            self.loop_input()

    def write_board(self, index):
        not_used = self.is_valid(index)
        if not_used:
            if self.is_x_turn:
                self.board[index] = "X"
                print(self.num_list)
            if not self.is_x_turn:
                self.board[index] = "O"
            self.take_turn()

    def display_board(self):
        return print(f"""
        -------------
        | {self.board[0]} | {self.board[1]} | {self.board[2]} |
        -------------
        | {self.board[3]} | {self.board[4]} | {self.board[5]} |
        -------------
        | {self.board[6]} | {self.board[7]} | {self.board[8]} |
        -------------""")

    def is_it_x_turn(self):
        return print(self.is_x_turn)

    def take_turn(self):
        self.is_x_turn = not self.is_x_turn
        self.num_of_turns += 1
        # fixme print(f"its is {self.is_x_turn} that it is x's turn.")
        return self.is_x_turn


# Setup
b1 = Hashtag(is_x_turn=True)

while not win.has_won(b1.board) and 10 in b1.num_list:

    print(b1.num_list)
    # var1 = input("Enter here: ")
    var1 = random.randint(0, 9)
    var1 = str(var1)
    while not var1.isdecimal():
        # var1 = input("Enter here: ")
        var1 = random.randint(0, 9)
        var1 = str(var1)
    var1 = int(var1)
    if 0 <= var1 <= 8:
        b1.write_board(var1)
        b1.display_board()

if 10 not in b1.num_list and not win.has_won(b1.board):
    print("it's a tie")
elif b1.is_x_turn:
    print("Yay O won!")
elif not b1.is_x_turn:
    print("Yay X won!")

# Print empty board and tell user the number layout
# choose which player goes first and what piece they are

# Main loop
# Player 1
# Prompts user for their move
# check if the move if valid
# if not loop input until valid
# Prints board to console

# Player 2
# Switch piece type
# Computer plays random move
# check if the move if valid
# if not loop input until valid
# Prints board to console

# check win

# ask user if they want to play again: later
