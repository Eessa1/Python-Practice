import json
import os 

LibraryList = []
if os.path.exists("JSONFILE.json"):
 with open("JSONFile.json", "r") as file:
  LibraryList = json.load(file)

def Library():
 WelcomeChoice = input("What would you like to do today?\n Commands: Add, View, Filter ").lower()
 if WelcomeChoice == "add":
  AddBooks()
 elif WelcomeChoice == "view":
  ViewBooks()
 elif WelcomeChoice == "filter":  
  FilterBooks()

def AddBooks():
 title = input("Enter the title of the book ").lower()
 author = input("Enter the author of the book ").lower()
 genre = input("Enter the genre ").lower()
 rating = input("Enter the rating of the book ").lower()
 book = {
   "title": title,
   "author": author,
   "genre": genre,
   "rating": rating,
   
 }
 LibraryList.append(book)
 with open ("JSONFile.json", "w") as file:
  json.dump(LibraryList, file, indent = 4)
 Library()

def ViewBooks():
 for books in LibraryList:
  print(f"{books['title'].title()} by {books['author'].title()}, {books['genre'].title()} rated {books['rating'].title()}")
 Library()

def FilterBooks():
 filterchoice = input("What would you like to filter by?\nTitle, Author, Genre, Rating ").lower().strip()
 filterspecific = input("What is the " + filterchoice + " you would like to filter by").lower().strip()
 for book in LibraryList:
  if book[filterchoice] == filterspecific:
   print(f"{book['title'].title()} by {book['author'].title()}, {book['genre'].title()} rated {book['rating'].title()}")
 Library()   

Library()