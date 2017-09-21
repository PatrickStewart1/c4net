from game import game

G = game()
G.board[5][5] = "red"
G.board[5][6] = "black"
G.board[2][2] = "red"
G.board[0][4] = "black"
G.board[0][0] = "red"
G._print_board()
print(G.list_open_columns())
for i in range(0,len(G.list_open_columns())):
    print(G.find_open_cell((G.list_open_columns()[i])))
