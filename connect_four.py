"""
board object
user vs user; ip int for rows
if 4 in a row, col or diag then game ends

"""

import random


# todo create a win func that's not spaghetti hard code it
# search 4 separate grids?


class Grid:
    def __init__(self, turn, board=None, avail_cols=None, ):
        self.turn = turn
        if board is None:
            board = [[' ', ' ', ' ', ' '],
                     [' ', ' ', ' ', ' '],
                     [' ', ' ', ' ', ' '],
                     [' ', ' ', ' ', ' ']
                     ]
            self.board = board
        if avail_cols is None:
            avail_cols = [0, 0, 0, 0]
            self.avail_cols = avail_cols

    def draw_board(self):
        return print(
            f"""       -----------------
       | {self.board[3][0]} | {self.board[3][1]} | {self.board[3][2]} | {self.board[3][3]} |
       ----------------
       | {self.board[2][0]} | {self.board[2][1]} | {self.board[2][2]} | {self.board[2][3]} |
       ----------------
       | {self.board[1][0]} | {self.board[1][1]} | {self.board[1][2]} | {self.board[1][3]} |
       ----------------
       | {self.board[0][0]} | {self.board[0][1]} | {self.board[0][2]} | {self.board[0][3]} |\n\t   -----------------""")

    def move(self, row, who):

        # fixme self.board[int(self.avail_cols[row])][row] = who
        # fixme IndexError: list index out of range
        # when user plays on a full row

        row -= 1
        self.board[int(self.avail_cols[row])][row] = who
        self.avail_cols[row] += 1
        self.turn = not self.turn
        return self.board, self.turn


user = True
piece = 'X'
my4x4 = Grid(user)

my4x4.draw_board()
var = 0

while var < 16:
    user_ip = "0"
    # check for win
    if user:
        user_ip = input("enter your row to take a move in for X.\nRows go left to right 1 to 4\n>")

    var += 1
    if user_ip.isdecimal():
        user_ip = int(round(float(user_ip)))
        if not user:
            user_ip = random.randint(1, 5)
            # have comp pick from a list
            # user_ip = input("enter your row to take a move in for O.\nRows go left to right 1 to 4\n>")
        if 1 <= user_ip <= 4:
            if my4x4.turn:
                piece = 'X'
            elif not my4x4.turn:
                piece = 'O'
            _, user = my4x4.move(user_ip, piece)
            my4x4.draw_board()
