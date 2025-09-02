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
 if board[y][x] == 'X' and board[y][x+1] == 'X' and board[y][x+2] == 'X':
  GameOver = True
 if board[y][x] == 'O' and board[y][x+1] == 'O' and board[y][x+2] == 'O':
  GameOver = True

 if board[y][x] == 'X' and board[y+1][x] == 'X' and board[y+2][x] == 'X':
  GameOver = True
 if board[y][x] == 'O' and board[y+1][x] == 'O' and board[y+2][x] == 'O':
  GameOver = True

 if board[y+1][x] == 'X' and board[y+1][x+1] == 'X' and board[y+1][x+2] == 'X':
  GameOver = True
 if board[y+1][x] == 'O' and board[y+1][x+1] == 'O' and board[y+1][x+2] == 'O':
  GameOver = True

 if board[y+2][x] == 'X' and board[y+2][x+1] == 'X' and board[y+2][x+2] == 'X':
  GameOver = True
 if board[y+2][x] == 'O' and board[y+2][x+1] == 'O' and board[y+2][x+2] == 'O':
  GameOver = True

 if board[y][x+1] == 'X' and board[y+1][x+1] == 'X' and board[y+2][x+1] == 'X':
  GameOver = True
 if board[y][x+1] == 'O' and board[y+1][x+1] == 'O' and board[y+2][x+1] == 'O':
  GameOver = True

 if board[y][x+2] == 'X' and board[y+1][x+2] == 'X' and board[y+2][x+2] == 'X':
  GameOver = True
 if board[y][x+2] == 'O' and board[y+1][x+2] == 'O' and board[y+2][x+2] == 'O':
  GameOver = True

 if board[y][x] == 'X' and board[y+1][x+1] == 'X' and board[y+2][x+2] == 'X':
  GameOver = True
 if board[y][x] == 'O' and board[y+1][x+1] == 'O' and board[y+2][x+2] == 'O':
  GameOver = True

 if board[y][x+2] == 'X' and board[y+1][x+1] == 'X' and board[y+2][x] == 'X':
  GameOver = True
 if board[y][x+2] == 'O' and board[y+1][x+1] == 'O' and board[y+2][x] == 'O':
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