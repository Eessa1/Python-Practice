import random

def genNumber():
    x = int(random.randrange(1,101))
    return x

def play():
    GuessCount = 0
    num1 = genNumber()
    guess = int(input("Take a guess "))
    GuessCount +=1
    while guess != num1:
        
        if num1 > guess:
            print("too low")
            
        elif num1 < guess:
            print("too high")
            
        guess = int(input("Take a guess "))
        GuessCount +=1
    print("correct")
    print ("Guesses: ", GuessCount)
    Again = input("Type yes to play again or no").strip().lower()
    if Again == ("yes"):
        play()
    
play()