def Exercise1():
 print ("Hello World")

def Exercise2():
  name = input("Enter your name ")
  print(f"Hello", {name})

def Exercise3():
  num1 = int(input("Enter the first number "))
  num2 = int(input("Enter the second number "))
  calculation = input("What operation would you like ")
  if calculation == ("multiplication"):
   print(num1 * num2)
  elif calculation == ("addition"):
   print(num1 + num2)
  elif calculation == ("subtraction"):
   print(num1 - num2)
  elif calculation == ("division"):
   if num2 == 0:
    print("Can't divide by 0")
   else:
    print(num1 / num2)

def Exercise4():
 games = []
 num1 = int(input(" How many games do you want to enter "))
 for n in range (num1):
   games.append(input(" Enter a game you liked to add to the list. "))
 print(games)

Exercise4()

