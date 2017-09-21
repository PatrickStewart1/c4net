import copy
class game:

    #layout of board, board[height][width] is the bottom right corner of the board
    # ---------------
    # |(0,0)   (0,7)|
    # |             |
    # |             |
    # |(6,0)   (6,7)|
    # |_____________|


    def __init__(self):
        self.board_size = {"width":6, "height":7}  # (W,H) these literals shouldn't be explicitly used anywhere else
        self.board = self._init_board()            # fill board with empty space

    def _init_board(self):
        board = []
        width = self.board_size["width"]
        height = self.board_size["height"]

        for i in range(0, width):                 # add empty columns to board, board now width x 1
            board.append([])

        for i in range(0, len(board)):            # add empty cells to each column, board now width x height
            for j in range(0, height):
                board[i].append("empty")

        return board

    def _print_board(self):
        copy_board = copy.deepcopy(self.board)
        width = self.board_size["width"]
        height = self.board_size["height"]

        for i in range(0, width):
            for j in range(0, height):                   # convert names to 1 char for formatting
                if copy_board[i][j] == "empty":
                    copy_board[i][j] = "/"
                elif copy_board[i][j] == "red":
                    copy_board[i][j] = "R"
                elif copy_board[i][j] == "black":
                    copy_board[i][j] = "B"

                print(copy_board[i][j], end='')

            print("\n")

    def list_open_columns(self):                        # returns all columns that are currently legal for play
        open_columns = []
        width = self.board_size["width"]
        for i in range(0, width+1):
            if self.board[0][i] == "empty":
                open_columns.append(i)

        return open_columns

    def find_open_cell(self, col):                       # returns bottom available cell, used for placing pieces

        height = self.board_size["height"]

        for i in range(height - 1, -1, -1):
            if self.board[i - 1][col] == "empty":
                return i

        return -1                                       # return -1 on full column
