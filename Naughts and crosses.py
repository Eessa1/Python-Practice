def boardsetup():
 board = [
 [" ", " ", " "],
 [" ", " ", " "],
 [" ", " ", " "]
 ]
 for row in board:
  print(" | ".join(row))
 return board
def Game():
 board = boardsetup()
 inputx, inputy = GetUserInput()
 board[inputx][inputy] = "X"
 for row in board:
  print(" | ".join(row))
 
 
def GetUserInput():
 XValue = int(input("Enter the X value 0-2 inclusive"))
 YValue = int(input("Enter the Y value 0-2 inclusive"))
 return XValue,YValue

Game()