import math

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
   AiInputX, AiInputY = AiTurn(board)
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
 
def CheckHypotheticalWin(board):
 
 x = 0
 y = 0
 if board[y][x] == 'X' and board[y][x+1] == 'X' and board[y][x+2] == 'X':
  return "Player"
 if board[y][x] == 'O' and board[y][x+1] == 'O' and board[y][x+2] == 'O':
  return "Ai"

 if board[y][x] == 'X' and board[y+1][x] == 'X' and board[y+2][x] == 'X':
  return "Player"
 if board[y][x] == 'O' and board[y+1][x] == 'O' and board[y+2][x] == 'O':
  return "Ai"

 if board[y+1][x] == 'X' and board[y+1][x+1] == 'X' and board[y+1][x+2] == 'X':
  return "Player"
 if board[y+1][x] == 'O' and board[y+1][x+1] == 'O' and board[y+1][x+2] == 'O':
  return "Ai"

 if board[y+2][x] == 'X' and board[y+2][x+1] == 'X' and board[y+2][x+2] == 'X':
  return "Player"
 if board[y+2][x] == 'O' and board[y+2][x+1] == 'O' and board[y+2][x+2] == 'O':
  return "Ai"

 if board[y][x+1] == 'X' and board[y+1][x+1] == 'X' and board[y+2][x+1] == 'X':
  return "Player"
 if board[y][x+1] == 'O' and board[y+1][x+1] == 'O' and board[y+2][x+1] == 'O':
  return "Ai"

 if board[y][x+2] == 'X' and board[y+1][x+2] == 'X' and board[y+2][x+2] == 'X':
  return "Player"
 if board[y][x+2] == 'O' and board[y+1][x+2] == 'O' and board[y+2][x+2] == 'O':
  return "Ai"

 if board[y][x] == 'X' and board[y+1][x+1] == 'X' and board[y+2][x+2] == 'X':
  return "Player"
 if board[y][x] == 'O' and board[y+1][x+1] == 'O' and board[y+2][x+2] == 'O':
  return "Ai"

 if board[y][x+2] == 'X' and board[y+1][x+1] == 'X' and board[y+2][x] == 'X':
  return "Player"
 if board[y][x+2] == 'O' and board[y+1][x+1] == 'O' and board[y+2][x] == 'O':
  return "Ai"
 
 for row in board:
  for cell in row:
   if cell == " ":
    return None
   
 return "Draw"

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

def miniMax(isMaximising):
 FutureWinner = CheckHypotheticalWin(board)
 if FutureWinner == "Ai":
   return +1
 if FutureWinner =="Player":
   return -1
 if FutureWinner == "Draw":
   return 0
  
 if isMaximising:
    BestScore = -math.inf
    for y, row in enumerate(board):
      for x, cell in enumerate(row):
        if cell == " ":
          board[y][x] = "O"
          Score = miniMax(False)
          board[y][x] = " "
          BestScore = max(Score, BestScore)
    return BestScore
 else:
    BestScore = math.inf
    for y, row in enumerate(board):
     for x, cell in enumerate(row):
        if cell == " ":
          board[y][x] = "X"
          Score = miniMax(True)
          board[y][x] = " "
          BestScore = min(Score, BestScore)
    return BestScore

def AiTurn(board):
 global PlayersTurn
 BestScore = -math.inf
 for y, row in enumerate(board):
  for x, cell in enumerate(row):
   if cell == " ":
    board[y][x] = "O"
    Score = miniMax(False)
    board[y][x] = " "
    if Score> BestScore:
     BestScore = Score
     BestMove = (x,y)   
 PlayersTurn = True 
 return BestMove

def GetUserInput():
 global PlayersTurn
 YValue = int(input("Enter the row 1-3 "))
 XValue = int(input("Enter the column 1-3 "))
 PlayersTurn = False
 return XValue,YValue

PlayersTurn = True
GameOver= False
board = []
PlayerTurn = True
Result = " "
Game()


