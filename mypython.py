# # Initialize the board
# board = ["-", "-", "-",
#          "-", "-", "-",
#          "-", "-", "-"]

# # Function to display the current state of the board
# def display_board():
#   print(board[0] + " | " + board[1] + " | " + board[2])
#   print(board[3] + " | " + board[4] + " | " + board[5])
#   print(board[6] + " | " + board[7] + " | " + board[8])

# # Function to handle a player's turn
# def handle_turn(player):
#   # Get the player's move
#   print(player + "'s turn.")
#   position = input("Choose a position from 1-9: ")

#   # Make sure the input is valid
#   valid = False
#   while not valid:
#     while position not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
#       position = input("Choose a position from 1-9: ")
#     position = int(position) - 1
#     if board[position] == "-":
#       valid = True
#     else:
#       print("You can't go there. Go again.")

#   # Put the player's symbol on the board
#   board[position] = player

# # Function to check if the game is over
# def check_game_over():
#   # Check for a win
#   if (board[0] == board[1] == board[2] != "-") or \
#      (board[3] == board[4] == board[5] != "-") or \
#      (board[6] == board[7] == board[8] != "-") or \
#      (board[0] == board[3] == board[6] != "-") or \
#      (board[1] == board[4] == board[7] != "-") or \
#      (board[2] == board[5] == board[8] != "-") or \
#      (board[0] == board[4] == board[8] != "-") or \
#      (board[2] == board[4] == board[6] != "-"):
#     return True

#   # Check for a tie
#   tie = True
#   for i in range(9):
#     if board[i] == "-":
#       tie = False
#       break

#   # If the game is a tie, return True
#   if tie:
#     return True

#   # Otherwise, the game is not over
#   return False

# # Function to flip the current player
# def flip_player():
#   global current_player
#   if current_player == "X":
#     current_player = "O"
#   elif current_player == "O":
#     current_player = "X"

# # Function to start the game
# def start_game():
#   # Display the initial board
#   display_board()

#   # While the game is not over
#   while not check_game_over():
#     # Handle a turn
#     handle_turn(current_player)

#     # Display the updated board
#     display_board()

#     # Flip the current player
#     flip_player()

#   # Print a message if the

import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Set up the figure and axes
fig, ax = plt.subplots()

# Set up the planets
planets = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]
positions = [(0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0)]
scatter_plot = ax.scatter(x=positions, y=positions, s=200)

# Animate the planets
def animate(i):
    for j, planet in enumerate(planets):
        # Update the position of each planet
        positions[j] = (positions[j][0] + 1, positions[j][1] + 1)
        scatter_plot.set_offsets(positions)

# Run the animation
ani = animation.FuncAnimation(fig, animate, frames=360, interval=20)
plt.show()

