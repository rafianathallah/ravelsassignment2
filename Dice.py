#Another Idea: Creating Dice using random Module

from random import randint

input_sides = int(input("How many sides does your die/dice contain?: "))
times_rolled = int(input("How many times would you like to roll?: "))
counter = 0

while counter < times_rolled:
    dice = randint(1,input_sides)
    print(dice)
    counter += 1