BookList = []
def Exercise1():
 print ("Hello World")

def Exercise2():
  name = input("Enter your name ")
  print("Hello", name)


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
 return games

def Exercise5(list_of_games):
  for game in list_of_games:
    print(game, end = ', ')

def Exercise6():
  GameDict = {}  
  Quantity = int(input("How many games would you like to enter? "))
  for n in range(Quantity):
    GameDict[n] = [input("Enter the name of the game ")]
    GameDict[n] += [input("Enter the genre of the game ")]
    GameDict[n] += [float(input("Enter the rating of the game "))]
  filter_choice = input("Would you like to filter the list for any specific genre?").strip().lower()
  if filter_choice == "yes":
   genrefilter = input("What genre would you like to filter by?")
   for key, value in GameDict.items():
    if(value[1] == genrefilter):
     print(GameDict[key])
  else:
   print(GameDict)
      

def Library():
 action = input("Welcome to the library what would you like to do today?\n You can add books, view all of our books or filter by author / genre\n Just Enter 'View', 'Add' or 'Filter").strip().lower()
 if action == "add":
  NewBook = AddBooks()
  BookList.append(NewBook)
 elif action == "view":
  print(BookList)
 elif action == "filter":
  returnedFilter = FilterBooks()
  filterType = returnedFilter[0]
  filterSpecify = returnedFilter[1]
  for BookDictionary in BookList:
   for key, value in BookDictionary.items():
    if value[filterType] == filterSpecify:
     print(BookDictionary)
 recurse = input("Do you want to perform another action? ").strip().lower()
 if recurse == "yes":
  Library()
 else:
  print("Have a nice day!")


def FilterBooks():
 filterChoice = input("What would you like to filter by genre or author? ").strip().lower()
 filterValue = input(f"Enter the {filterChoice} " ).strip().lower()
 return filterChoice, filterValue

def AddBooks():
 BookDict = {}
 Book = input("Enter the book name ")
 BookDict[Book] = {
  "author": input("Enter the Author ").strip().lower(),
  "genre": input("Enter the Genre ").strip().lower(),
  "year": int(input("Enter the Year "))
 }
 return BookDict
 


Library()
    
  
