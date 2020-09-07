
import random
import string

def printing_score ():
  print("-------------")
  print("Score:", computer_score,"-", user_score)
  print("-------------")

print("|----------------------------|")
print("|--- // Battleship game //---|")
print("|----------------------------|")

board = []

for i in range(5):
  board.append(['0']*5,)
    
  def print_board(board):
      print(" ", " ".join("ABCDE"))
      for letter, row in zip("12345", board):
          print(letter, " ".join(row))

print_board(board)

turn = 0
computer_score = 0
user_score = 0

letters = ['A', 'B','C','D','E','a','b','c','d','e']

letters_to_numbers = {
    'A': 0,
    'B': 1,
    'C': 2,
    'D': 3,
    'E': 4,
    'a': 0,
    'b': 1,
    'c': 2,
    'd': 3,
    'e': 4,
}

#main_program
computer_row = random.randint(1,5)
computer_col = random.choice(string.ascii_letters[0:4])

for turn in range(5):
    print("\n")
    turn += 1
    print("Turn", turn)

    user_row = input("Select row (1-5): ")
    while user_row not in "12345":
        print("Out of see! Choose 1, 2, 3, 4 or 5")
        user_row = input("Select row (1-5): ")

    user_col = input("Select column (A-E): ")
    while user_col not in "ABCDEabcde":
        print("Out of see! Choose A, B, C, D, E or a, b, c, d, e")
        user_col = input("Select column (A-E): ")
    user_row = int(user_row)

    column_number = letters_to_numbers[user_col]
    column_number_ai = letters_to_numbers[computer_col]

    if user_row == computer_row and user_col == computer_col:
      print("You sank my Battleship!")
      user_score += 1
      printing_score()
      break
    else: 
      computer_score += 1
      print("You missed my Battleship!")
      board[(user_row)-1][column_number] = "X"
      print_board(board)
      printing_score()

if computer_score > user_score:
  board[computer_row][column_number_ai] = "-"
  print_board(board)
  print ("Game Over!")
elif computer_score == user_score:
  print("Tie Game")
else:
  print("You win")