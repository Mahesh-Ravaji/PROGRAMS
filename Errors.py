# # Print(a)


# # for i in range (0,10)
# # print(i)

# if 9<4:
#     print("9 is greater")
# else  (4<3):
#     print("4 is greater")



# define a function to print the board
def print_board(board):
    for i in range(3):
        for j in range(3):
            print(board[i][j], end=" ")
        print()
    print()

# define the main function
def main():
    # create an empty board
    board = [["_" for i in range(3)] for j in range(3)]

    # keep track of the number of moves made
    num_moves = 0

    # keep playing until the game is over
    while True:
        # print the board
        print_board(board)

        # check if the game is over
        if num_moves == 9:
            print("It's a tie!")
            break

        # get the input from the current player
        player = "X" if num_moves % 2 == 0 else "O"
        x, y = map(int, input(f"Player {player}, enter your move (row column): ").split())

        # make sure the input is valid
        if x < 0 or x > 2 or y < 0 or y > 2 or board[x][y] != "_":
            print("Invalid move, try again!")
            continue

        # place the player's piece on the board
        board[x][y] = player

        # check if the player has won
        if (board[0][0] == player and board[0][1] == player and board[0][2] == player) or \
           (board[1][0] == player and board[1][1] == player and board[1][2] == player) or \
           (board[2][0] == player and board[2][1] == player and board[2][2] == player) or \
           (board[0][0] == player and board[1][0] == player and board[2][0] == player) or \
           (board[0][1] == player and board[1][1] == player and board[2][1] == player) or \
           (board[0][2] == player and board[1][2] == player and board[2][2] == player) or \
           (board[0][0] == player and board[1][1] == player and board[2][2] == player) or \
           (board[0][2] == player and board[1][1] == player and board[2][0] == player):
            print_board(board)
            print(f"Player {player} wins!")
            break

        # increment the number of moves made
        num_moves += 1

# run the main function
# main()
