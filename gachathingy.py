#another idea -rafian
import random

def rolling1x():
    resultofroll1x = random.randrange(1,1000)
    if resultofroll1x in range(1,601):
        print("Nice! You got a 2 star item.")
    if resultofroll1x in range(601,851):
        print("Congrats! You got a 3 star item.")
    if resultofroll1x in range(851,976):
        print("Wonderful! You got a 4 star item.")
    if resultofroll1x in range(976,1001):
        print("Amazing! You got a 5 star item. Nice luck!")

def rolling5x():
    for i in range(4):
        rolling1x()
    print("Congrats! You got a 3 star item.")

def rolling10x():
    for i in range(9):
        rolling1x()
    print("Wonderful! You got a 4 star item.")
    
def startscreen():
    print("Welcome to our gacha simulator!")
    print("What would you like to roll?")
    print("(1) Roll 1x")
    print("(2) Roll 5x (Guaranteed 3 star item)")
    print("(3) Roll 10x (Guaranteed 4 star item)")
    
    rollchoice = (int(input("Your choice: ")))
    print(rollchoice)
    
    if rollchoice > 3:
        print("Sorry! That choice is not valid.")
        
    if rollchoice < 1:
        print("Sorry! That choice is not valid.")
        
    if rollchoice == 1:
        rolling1x()

    if rollchoice == 2:
        rolling5x()
        
    if rollchoice == 3:
        rolling10x()
    
startscreen()

#need improvements on the guarantee system cause rn i just print at the end and it looks mega scuffed