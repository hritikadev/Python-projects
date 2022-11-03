import random
from words import terms
import string

def get_words(terms):
    word = random.choice(terms)
    while '-' in terms or ' ' in terms:
        word = random.choice(terms)
    return word.upper()
   ##find no of '-' ' ' and reduce the length --> mine

def game():
    word = get_words(terms)
    letters = set(word)
    alphabet = set(string.ascii_uppercase)
    guessed = set()

    lives = len(letters)
    
    while len(letters) > 0 and lives > 0:
        ## len() actully gives count of unique charcters, like for 'HOLLOW' the value is 4
        print("you have ", lives, "lives left.\nYou have used : ", ' '.join(guessed))
        curr_word = [char if char in guessed else '_' for char in word]
        print('The word guessed is', ' ' .join(curr_word), '\n')

        user_guess = input("Enter a character : ").upper()
        if user_guess in alphabet - guessed:
            guessed.add(user_guess)
            if user_guess in letters:
                letters.remove(user_guess)
            else:
                lives = lives-1
                print("Letter not in word.")
        elif user_guess in guessed:
            print("Already used")
        else:
            print('INVALID')
    if lives == 0:
        print(f"You died. The word was : {word}")
    else:  
        print(f"Tou have guessed correctly. The word was : {word}")
game()

        
