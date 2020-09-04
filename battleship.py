"""  van egy 5 x 5 os boardunk
1. ki kell printelni:
    0 0 0 0 0
    0 0 0 0 0
    0 0 0 0 0
    0 0 0 0 0
2. kiiratni h hanyadik korben vagyunk (5 korig mehet)                  
3. bekerni 1-5-ig a sort
4. bekerni 1-5-ig az oszlopot 
5. randomint-el bekerni egy szamot a sorban es az oszlopban a computertol
6. megnezni h egyeznek -e
7. kiirni h eltalalt -e
8. kiprintelni a tombot benne a kivalasztott elemet x-el jelolve
9. megnezni az allast es kiiratni h ki nyert
"""

import random

def printing_score ():
  print("-------------")
  print("Score:", computer_score,"-", user_score)
  print("-------------")

print("|----------------------------|")
print("|--- // Battleship game //---|")
print("|----------------------------|")

turn = 0
board = []
for i in range(5):
  board.append(['0']*5)
    
  def board_printing(board):
      print("\n")
      for row in board:
        print(' '.join(row))
        
board_printing(board)

computer_score = 0
user_score = 0

for turn in range(5):
    print("\n")
    turn += 1
    print("Turn", turn)

    user_row = int(input("Select row (1-5): "))
    user_col = int(input("Select col (1-5): "))


    computer_row = random.randint(1,5)
    computer_col = random.randint(1,5)

    if ( 5 < user_row or user_row < 1 ) or ( 5 < user_col or user_col < 1 ):
      print("You are out of see\n")
      computer_score += 1
      printing_score()
    elif user_row == computer_row and user_col == computer_col:
      print("You sank my Battleship!")
      user_score += 1
      printing_score()
    else: 
      computer_score += 1
      print("You missed my Battleship!")
      board[(user_row)-1][(user_col)-1] = "X"
      board_printing(board)
      printing_score()

if computer_score > user_score:
  print ("You Lose!")
elif computer_score == user_score:
  print("Tie Game")
else:
  print("You win")