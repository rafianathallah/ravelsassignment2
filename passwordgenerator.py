import random
import string

password_length = int(input("Please input the amount of characters you want for the password: "))
spec_or_not = input("Do you want your password to have special characters or not? (Yes/No): ")

def non_spec_char_pass(length):
    letters_and_digits = string.ascii_letters + string.digits
    result_str = ''.join((random.choice(letters_and_digits) for i in range(length)))
    return result_str

def spec_character_password(length):
    letters_and_digits = string.ascii_letters + string.digits + string.punctuation
    result_str = ''.join((random.choice(letters_and_digits) for i in range(length)))
    return result_str

if spec_or_not == 'Yes':
    print(spec_character_password(password_length))
elif spec_or_not == 'No':
    print(non_spec_char_pass(password_length))
else:
    spec_or_not = input("Invalid input. Please input either yes or no: ")
