import random 

def boardsetup():
 boardSet = [
 [" ", " ", " "],
 [" ", " ", " "],
 [" ", " ", " "]
 ]
 for row in boardSet:
  print(" | ".join(row))
 return boardSet

def Game():
 global Result
 global PlayersTurn
 global GameOver
 while GameOver == False:
  global board
  if board == []:
    board = boardsetup()
  if PlayersTurn == True:
   inputx, inputy = GetUserInput()
   board[inputy-1][inputx-1] = "X"
  elif PlayersTurn == False:
   AiInputX, AiInputY = AiTurn()
   board[AiInputY][AiInputX] = "O"
  for row in board:
    print(" | ".join(row))
  CheckIfWin()
 GameState()
 print(Result)
  
def CheckIfWin():
 global Result
 global board
 global GameOver
 x = 0
 y = 0
 if board[y][x] == 'X' and board[y][x+1] == 'X' and board[y][x+2] == 'X':
  GameOver = True
  Result = "Player"
 if board[y][x] == 'O' and board[y][x+1] == 'O' and board[y][x+2] == 'O':
  GameOver = True
  Result = "Ai"

 if board[y][x] == 'X' and board[y+1][x] == 'X' and board[y+2][x] == 'X':
  GameOver = True
  Result = "Player"
 if board[y][x] == 'O' and board[y+1][x] == 'O' and board[y+2][x] == 'O':
  GameOver = True
  Result = "Ai"

 if board[y+1][x] == 'X' and board[y+1][x+1] == 'X' and board[y+1][x+2] == 'X':
  GameOver = True
  Result = "Player"
 if board[y+1][x] == 'O' and board[y+1][x+1] == 'O' and board[y+1][x+2] == 'O':
  GameOver = True
  Result = "Ai"

 if board[y+2][x] == 'X' and board[y+2][x+1] == 'X' and board[y+2][x+2] == 'X':
  GameOver = True
  Result = "Player"
 if board[y+2][x] == 'O' and board[y+2][x+1] == 'O' and board[y+2][x+2] == 'O':
  GameOver = True
  Result = "Ai"

 if board[y][x+1] == 'X' and board[y+1][x+1] == 'X' and board[y+2][x+1] == 'X':
  GameOver = True
  Result = "Player"
 if board[y][x+1] == 'O' and board[y+1][x+1] == 'O' and board[y+2][x+1] == 'O':
  GameOver = True
  Result = "Ai"

 if board[y][x+2] == 'X' and board[y+1][x+2] == 'X' and board[y+2][x+2] == 'X':
  GameOver = True
  Result = "Player"
 if board[y][x+2] == 'O' and board[y+1][x+2] == 'O' and board[y+2][x+2] == 'O':
  GameOver = True
  Result = "Ai"

 if board[y][x] == 'X' and board[y+1][x+1] == 'X' and board[y+2][x+2] == 'X':
  GameOver = True
  Result = "Player"
 if board[y][x] == 'O' and board[y+1][x+1] == 'O' and board[y+2][x+2] == 'O':
  GameOver = True
  Result = "Ai"

 if board[y][x+2] == 'X' and board[y+1][x+1] == 'X' and board[y+2][x] == 'X':
  GameOver = True
  Result = "Player"
 if board[y][x+2] == 'O' and board[y+1][x+1] == 'O' and board[y+2][x] == 'O':
  GameOver = True
  Result = "Ai"
 
def GameState():
 global Result
 global board
 global GameOver
 counter = 0
 for rows in board:
  for cell in rows:
   if cell == " ":
    counter += 1
 if counter == 0 and GameOver == False:
   GameOver = True
   Result = "Draw"

def miniMax():
 global board
 global Result
 global Maximising
 if GameOver:
  if Result == "Ai":
   return +1
  if Result =="Player":
   return -1
  if Result == "Draw":
   return 0
 for y, row in enumerate(board):
  for x, cell in enumerate(row):
   if cell == " ":
    if Maximising == True:
     board[y][x] = "O"

    if Maximising == False:
     board[y][x] = "X"
    Maximising = not Maximising


    


def AiTurn():
 global board
 global PlayersTurn
 moveWorth = miniMax()
 PlayersTurn = True 

def GetUserInput():
 global PlayersTurn
 YValue = int(input("Enter the row 1-3 "))
 XValue = int(input("Enter the column 1-3 "))
 PlayersTurn = False
 return XValue,YValue

Maximising = True
PlayersTurn = True
GameOver= False
board = []
PlayerTurn = True
Result = " "
Game()


