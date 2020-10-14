
import random
import string

greeting = print("This program will generate a randomized password for your personal use.\n")
password_length = eval(input("Please input the amount of characters you want for the password: "))
spec_or_not = input("Do you want your password to have special characters or not? (Yes/No): ")

def non_spec_char_pass(length):
    letters_and_digits = string.ascii_letters + string.digits
    result_str = ''.join((random.choice(letters_and_digits) for i in range(length)))
    return result_str

def spec_character_password(length):
    letters_digits_symbols = string.ascii_letters + string.digits + string.punctuation
    result_str = ''.join((random.choice(letters_digits_symbols) for i in range(length)))
    return result_str

if spec_or_not == 'Yes':
    print(spec_character_password(password_length))
elif spec_or_not == 'No':
    print(non_spec_char_pass(password_length))
else:
    spec_or_not = input("Invalid input. Please input either yes or no: ")

#I'll just put possible improvements down here:
    #Maybe help me find a way so that if a person inputs string on password_length, the program will say that the input is invalid instead of returning an error.
    #Maybe we can make it so that the password will only havea certain/fixed number of numbers and symbols.




