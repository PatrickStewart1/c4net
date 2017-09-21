from c4net import *
from game import *


class playerbot:

    def __init__(self, neural_net):
        self.brain = neural_net
        self.is_first = -1  # this shouldn't be set when object is created, but rather should be changed from
                            # outside every time the player enters into a game

    def take_turn(self,board):
        boardstate = [int(self.is_first)]
        for i in range(0, len(board)):
            for j in range(0, len(board[i])):
                boardstate.append(int(board[i][j] == "red"))
                boardstate.append(int(board[i][j] == "black"))
                boardstate.append(int(board[i][j] == "empty"))

        print(boardstate)


net = general_net([1,2,3,4],[2,3,4,3,6,2,7])
G = game()
G.board[5][5] = "red"
G.board[5][6] = "black"
G.board[2][2] = "red"
G.board[0][4] = "black"
G.board[0][0] = "red"

pb = playerbot(net)
pb.take_turn(G.board)