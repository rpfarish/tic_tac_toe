# Imports the random module
import random


# TODO Add move blocking for AI


# Start game
def start(player_1=0, player_2=1):
    def has_won(list_grid):
        """Checks if Cols, Rows or Diagonal is occupied by either a X or an O
        :param list_grid type list
        :returns if there is a win and who won :return bool"""
        # TODO Try and reduce func
        # Check Cols X
        if list_grid[0] == "X" and list_grid[1] == "X" and list_grid[2] == "X":
            return True, True
        elif list_grid[3] == "X" and list_grid[4] == "X" and list_grid[5] == "X":
            return True, True
        elif list_grid[6] == "X" and list_grid[7] == "X" and list_grid[8] == "X":
            return True, True
        # Check Cols O
        elif list_grid[0] == "O" and list_grid[1] == "O" and list_grid[2] == "O":
            return True, False
        elif list_grid[3] == "O" and list_grid[4] == "O" and list_grid[5] == "O":
            return True, False
        elif list_grid[6] == "O" and list_grid[7] == "O" and list_grid[8] == "O":
            return True, False

        # Check Rows X
        elif list_grid[6] == "X" and list_grid[3] == "X" and list_grid[0] == "X":
            return True, True
        elif list_grid[7] == "X" and list_grid[4] == "X" and list_grid[1] == "X":
            return True, True
        elif list_grid[8] == "X" and list_grid[5] == "X" and list_grid[2] == "X":
            return True, True
        # Check Rows O
        elif list_grid[6] == "O" and list_grid[3] == "O" and list_grid[0] == "O":
            return True, False
        elif list_grid[7] == "O" and list_grid[4] == "O" and list_grid[1] == "O":
            return True, False
        elif list_grid[8] == "O" and list_grid[5] == "O" and list_grid[2] == "O":
            return True, False

        # Check Diagonals X
        elif list_grid[0] == "X" and list_grid[4] == "X" and list_grid[8] == "X":
            return True, True
        elif list_grid[2] == "X" and list_grid[4] == "X" and list_grid[6] == "X":
            return True, True
        # Check Diagonals O
        elif list_grid[0] == "O" and list_grid[4] == "O" and list_grid[8] == "O":
            return True, False
        elif list_grid[2] == "O" and list_grid[4] == "O" and list_grid[6] == "O":
            return True, False

    # create board object
    class Hashtag:
        def __init__(self, is_x_turn=None, board=None):
            """This is the docString for the class Hashtag.
            list of all funcs inside me"""
            # TODO create a docString
            # TODO make is_x_turn independent of comp and user

            # Keeps track of if a piece has been placed at a position
            self.move_list = [10] * 9
            # If is_x_turn param is not passed
            if is_x_turn is None:
                is_x_turn = True
            self.is_x_turn = is_x_turn
            if board is None:
                board = [" "] * 9
            self.board = board

        def is_valid(self, index):
            """Takes an int for the index of the value to be evaluated == 10.
            If True then returns True,
            and if not prints the index and warns user the index is not a valid input,
            and returns False.
            :param index type int
            :param index is the index of the value that is checked in move_list
            :returns bool"""

            if self.move_list[index] == 10:
                self.move_list[index] = index
                return True
            elif index in self.move_list:
                # TODO don't print when its comp turn and don't print board(make it stop)
                print(f"hey, {index + 1} is not a valid input ")
                return False

        def valid_move_list(self):
            """:param self.move_list
            :returns valid_li, list of open/valid moves"""
            valid_li = []
            # loops for then length of num list
            for i in range(len(self.move_list)):
                if self.move_list[i] == 10:
                    valid_li.append(i)

            return valid_li

        def write_board(self, index):
            not_used = self.is_valid(index)
            if not_used:
                if self.is_x_turn:
                    self.board[index] = "X"
                if not self.is_x_turn:
                    self.board[index] = "O"
                self.take_turn()
            # FIxME

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
            # fixme print(f"its is {self.is_x_turn} that it is x's turn.")
            return self.is_x_turn

    # Setup
    b1 = Hashtag(is_x_turn=True)
    b2 = Hashtag()
    b2.example_board()

    # make available list
    def best_move(avail, board_li, who):
        """If there are two pieces in a row it returns the winning move,
        else returns -1
        :param board_li: list
        :param avail: all the available positions to play
        :param who: str either X or O
        """
        print(f"print avail'{avail}'")

        for i in avail:
            new_board = board_li[:]
            new_board[i] = who
            good = has_won(new_board)
            # do the move
            if good:
                return str(i + 1)
            print(f"print avail'{avail}'")

        else:
            return -1

    #         The stop move func

    # b2.display_board()

    # Available spaces list
    # ip all moves from list and check if each produces a win
    # and if true return move

    # Main loop and check win
    while not has_won(b1.board) and 10 in b1.move_list:
        print(f"print move list '{b1.move_list}'")
        whosturn = ''
        if b1.is_x_turn:
            whosturn = 'X'
        elif not b1.is_x_turn:
            whosturn = 'O'

        # Player 1
        if b1.is_x_turn:
            hi2 = b1.valid_move_list()
            if player_1 == 0:
                # Prompts Player 1 for their move
                var1 = input(f"It's {whosturn}'s turn. \nEnter your move here: ")
            elif player_1 == 1:
                var1 = random.randint(0, 9)
                var1 = str(var1)
            elif player_1 == 3:
                gold = best_move(hi2, b1.board, 'X')
                if gold != -1:
                    var1 = str(gold)
                else:
                    var1 = str(random.randint(0, 9))
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
            hi = b1.valid_move_list()
            if player_2 == 0:
                # Prompts Player 2 for their move
                var2 = input(f"It's {whosturn}'s turn. \nEnter your move here: ")
            elif player_2 == 1:
                # Computer plays random move
                var2 = str(random.randint(0, 9))
            elif player_2 == 3:

                gold = best_move(hi, b1.board, 'O')
                if gold != -1:
                    var2 = gold
                else:
                    var2 = str(random.randint(0, 9))
            else:
                var2 = '0'

            # check if the move if valid and if not loop input until valid
            while not var2.isdecimal():
                if player_2 == 0:
                    var2 = input("Enter your move here: ")
                elif player_2 == 1:
                    var2 = str(random.randint(0, 9))
            var2 = int(var2)
            if 1 <= var2 <= 9:
                var2 -= 1
                b1.write_board(var2)
                # Prints board to console
                b1.display_board()

    # Checks what type the end game was and then prints it
    if 10 not in b1.move_list and not has_won(b1.board):
        print("it's a tie")
    #     Print who won to a text file
    elif b1.is_x_turn:
        print("Yay O won!")
    elif not b1.is_x_turn:
        print("Yay X won!")

    init_func_game(True)


# TODO choose which player goes first and what piece they are
def init_func_game(other=False):
    global thnx

    def ip_func(init_the_game):
        if init_the_game == '':
            pass
        elif init_the_game == 'n' or init_the_game == 'no' or init_the_game == 'quit' \
                or init_the_game == 'nope' or init_the_game[0] == 'n':
            quit()
        mode = input("Enter Option Number 1-9:\n\t1:Human vs Computer AI\n"
                     "\t2:Human vs Computer Random.\n"
                     "\t3:Human vs Human\n\t4:Computer AI vs Human\n"
                     "\t5:Computer Random vs Human\n"
                     "\t6:Computer Random vs Computer AI\n"
                     "\t7:Computer AI vs Computer Random\n"
                     "\t8:Computer AI vs Computer AI\n"
                     "\t9:Computer Random vs Computer Random\n\n>")
        return mode

    def start_mode(mode):
        # 0:Human 1:Comp Rand 3:Comp AI
        if mode == '1':
            start(0, 3)
        elif mode == '2':
            start(0, 1)
        elif mode == '3':
            start(0, 0)
        elif mode == '4':
            start(3, 0)
        elif mode == '5':
            start(1, 0)
        elif mode == '6':
            start(1, 3)
        elif mode == '7':
            start(3, 1)
        elif mode == '8':
            start(3, 3)
        elif mode == '9':
            start(1, 1)

    if not other:
        # ask user if they want to play again: later
        init_game = input('Do you want to play a game?\n> ')
        init_game = init_game.lower()
        thnx = ip_func(init_game)
        start_mode(thnx)
    if other:
        # TODO make it remember your mode
        # ask user if they want to play again: later
        init_the_game = input('Do you want to play again?\n>')
        if init_the_game == '':
            pass
        elif init_the_game == 'n' or init_the_game == 'no' or init_the_game == 'quit' \
                or init_the_game == 'nope' or init_the_game[0] == 'n':
            quit()
        start_mode(thnx)


init_func_game()
