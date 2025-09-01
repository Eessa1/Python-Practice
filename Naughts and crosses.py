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
 global GameOver
 while GameOver == False:
  global board
  if board == []:
    board = boardsetup()
  inputx, inputy = GetUserInput()
  board[inputy-1][inputx-1] = "X"
  for row in board:
    print(" | ".join(row))
  CheckIfWin()
  
def CheckIfWin():
 global board
 global GameOver
 x = 0
 y = 0
 if board[y][x] and board[y][x+1] and board[y][x+2] == 'X':
  GameOver = True
 
def GetUserInput():
 YValue = int(input("Enter the row 1-3 "))
 XValue = int(input("Enter the column 1-3 "))
 return XValue,YValue

GameOver= False
board = []
PlayerTurn = True
AiTurn = False
Game()