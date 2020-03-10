import random


# Task list

# This is only a user vs rand comp
# TODO make different modes

# Start game
def start(player_1=0, player_2=1):
    def has_won(list_grid):
        # Check Cols
        if list_grid[0] == "X" and list_grid[1] == "X" and list_grid[2] == "X":
            return True, True
        elif list_grid[3] == "X" and list_grid[4] == "X" and list_grid[5] == "X":
            return True, True
        elif list_grid[6] == "X" and list_grid[7] == "X" and list_grid[8] == "X":
            return True, True

        elif list_grid[0] == "O" and list_grid[1] == "O" and list_grid[2] == "O":
            return True, False
        elif list_grid[3] == "O" and list_grid[4] == "O" and list_grid[5] == "O":
            return True, False
        elif list_grid[6] == "O" and list_grid[7] == "O" and list_grid[8] == "O":
            return True, False

        # Check Rows
        elif list_grid[6] == "X" and list_grid[3] == "X" and list_grid[0] == "X":
            return True, True
        elif list_grid[7] == "X" and list_grid[4] == "X" and list_grid[1] == "X":
            return True, True
        elif list_grid[8] == "X" and list_grid[5] == "X" and list_grid[2] == "X":
            return True, True

        elif list_grid[6] == "O" and list_grid[3] == "O" and list_grid[0] == "O":
            return True, False
        elif list_grid[7] == "O" and list_grid[4] == "O" and list_grid[1] == "O":
            return True, False
        elif list_grid[8] == "O" and list_grid[5] == "O" and list_grid[2] == "O":
            return True, False

        # Check Diag
        elif list_grid[0] == "X" and list_grid[4] == "X" and list_grid[8] == "X":
            return True, True
        elif list_grid[2] == "X" and list_grid[4] == "X" and list_grid[6] == "X":
            return True, True

        elif list_grid[0] == "O" and list_grid[4] == "O" and list_grid[8] == "O":
            return True, False
        elif list_grid[2] == "O" and list_grid[4] == "O" and list_grid[6] == "O":
            return True, False

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
                # TODO don't print when its comp turn and dont print board
                print(f"hey, {index + 1} is not a valid input ")
                self.loop_input()

        def write_board(self, index):
            not_used = self.is_valid(index)
            if not_used:
                if self.is_x_turn:
                    self.board[index] = "X"
                if not self.is_x_turn:
                    self.board[index] = "O"
                self.take_turn()

        def display_board(self):
            return print(f"""
             {self.board[0]} | {self.board[1]} | {self.board[2]} 
            -----------
             {self.board[3]} | {self.board[4]} | {self.board[5]} 
            -----------
             {self.board[6]} | {self.board[7]} | {self.board[8]} \n\n""")

        @staticmethod
        def example_board():
            """Prints a board and tells user the number layout"""
            return print(f"""
    The number corresponds to the position for the move.
             {1} | {2} | {3} 
            -----------
             {4} | {5} | {6} 
            -----------
             {7} | {8} | {9} """)

        def is_it_x_turn(self):
            return print(self.is_x_turn)

        def take_turn(self):
            self.is_x_turn = not self.is_x_turn
            self.num_of_turns += 1
            # fixme print(f"its is {self.is_x_turn} that it is x's turn.")
            return self.is_x_turn

    # Setup
    b1 = Hashtag(is_x_turn=True)
    b2 = Hashtag()
    b2.example_board()

    # b2.display_board()



    # Main loop and check win
    while not has_won(b1.board) and 10 in b1.num_list:
        whosturn = ''
        if b1.is_x_turn:
            whosturn = 'X'
        elif not b1.is_x_turn:
            whosturn = 'O'

        # Player 1
        if b1.is_x_turn:
            if player_1 == 0:
                # Prompts Player 1 for their move
                var1 = input(f"It's {whosturn}'s turn. \nEnter your move here: ")
            elif player_1 == 1:
                var1 = random.randint(0, 9)
                var1 = str(var1)
            else:
                var1 = '0'
            # checks if the move if valid and if not loop input until valid
            while not var1.isdecimal():
                if player_1 == 0:
                    var1 = input("Enter your move here: ")
                elif player_1 == 1:
                    var1 = random.randint(0, 9)
                    var1 = str(var1)
            var1 = int(var1)
            if 1 <= var1 <= 9:
                var1 -= 1
                b1.write_board(var1)
                # Prints board to console
                b1.display_board()
        # Player 2
        elif not b1.is_x_turn:
            if player_2 == 0:
                # Prompts Player 2 for their move
                var1 = input(f"It's {whosturn}'s turn. \nEnter your move here: ")
            elif player_2 == 1:
                # Computer plays random move
                var1 = str(random.randint(0, 9))
            elif player_2 == 3:
                var1 = best_move()
            else:
                var1 = '0'

            # check if the move if valid and if not loop input until valid
            while not var1.isdecimal():
                if player_2 == 0:
                    var1 = input("Enter your move here: ")
                elif player_2 == 1:
                    var1 = str(random.randint(0, 9))
                elif player_2 == 2:
                    var1 = best_move()
            var1 = int(var1)
            if 1 <= var1 <= 9:
                var1 -= 1
                b1.write_board(var1)
                # Prints board to console
                b1.display_board()

    # Checks what type the end game was and then prints it
    if 10 not in b1.num_list and not has_won(b1.board):
        print("it's a tie")
    elif b1.is_x_turn:
        print("Yay O won!")
    elif not b1.is_x_turn:
        print("Yay X won!")

    init_func_game(True)


# TODO choose which player goes first and what piece they are
def init_func_game(other=False):
    if not other:
        # ask user if they want to play again: later
        init_game = input('Do you want to play a game?\n> ')
        init_game = init_game.lower()
        mode = input("Enter 1 or 2\n1: Human vs Human\n2: Human vs Computer Random.\n>")
        # TODO filter input
        if init_game == 'n' or init_game == 'no' or init_game == 'quit':
            quit()
        elif mode == '1':
            start(0, 0)
        elif mode == '2':
            start(0, 1)
    if other:
        # ask user if they want to play again: later
        init_game = input('Do you want to play again?\n>')
        init_game = init_game.lower()
        if init_game == 'n' or init_game == 'no' or init_game == 'quit':
            quit()
        else:
            start(0, 1)


init_func_game()
