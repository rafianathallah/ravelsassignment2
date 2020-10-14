# another idea: Jumbled Word Game -karen
import random

def word_choose():
    words = ["alphabets", "elephant", "tarantula", 'football', "despicable"]
    pick_words = random.choice(words)
    return pick_words
def jumbled_word(words):
    word_random = random.sample(words, len(words))
    jumbled = ''.join(word_random)
    return jumbled
# to loop
while True:
    print("Welcome to Jumbled Word Game")
    print("Now , we will start the game")

    pick_word = word_choose()
    jumble_question = jumbled_word(pick_word)
    print("Guess the word", jumble_question)

    answer = input("Your answer is: ")


    if answer == pick_word:
        print("You are correct.")
    else:
        print("You're answer is wrong")

    x = input("Do you wish to play again? (Yes/No): ")

    if x == "No":
        print("Thankyou for playing. See you next time!")
        break