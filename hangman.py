import random
import man
#from man import HANGMANPICS

#STEP 1: we scan the words from file, then we devide them into 3 lists by their difficulty

def scanning():
    words = []
    words_sorted_by_difficulty = [[],[],[]]
    with open("countries-and-capitals.txt") as file:
        for line in file:
            words.append(line.rstrip().split(' | '))
    for i in range(len(words)):
        for j in range(2):
            if len(words[i][j]) <= 10:
                words_sorted_by_difficulty[0].append(words[i][j])
            elif 10 < len(words[i][j]) <= 20:
                words_sorted_by_difficulty[1].append(words[i][j])
            else:
                words_sorted_by_difficulty[2].append(words[i][j])
    return words_sorted_by_difficulty

# STEP 2
# ask the user about their chosen difficulty level

def difficulty(words_sorted_by_difficulty):
    while True:
        try:
            difficulty = int(input("\033[94mPlease select a level! Type 1 for Easy, 2 for Mediate or 3 for Master. \033[0m"))
            if difficulty == 1:
                diff = words_sorted_by_difficulty[0]
            elif difficulty == 2:
                diff = words_sorted_by_difficulty[1]
            elif difficulty == 3:
                diff = words_sorted_by_difficulty[2]
            else:
                print("Try another number, between 1 and 3")
                continue
            return diff
        except ValueError:
            print("That doesn't really look like a level number... Let's try again!")
            continue

# based on the chosen difficulty level, set the word to guess
def choose_a_word(diff):
    rnd = int(random.randrange(0,len(diff)+1))
    word_to_guess = diff[rnd]
    return word_to_guess

   
# STEP 3
# display the chosen word to guess with all letters replaced by "_"
# for example instead of "Cairo" display "_ _ _ _ _"
def guessed():
    guessed = []
    for i in range(len(word_to_guess)):
        if word_to_guess[i] == ' ':
            guessed.append(' ')
        else:
            guessed.append('_')
    kiir(guessed)
    return guessed
    
def kiir(guessed):
    print('\033[92m' + ' '.join(guessed) + '\033[0m')


# STEP 4
# ask the user to type a letter
# here you should validate if the typed letter is the word 
# "quit", "Quit", "QUit", "QUIt", "QUIT", "QuIT"... you get the idea :)
# HINT: use the upper() or lower() built-in Python functions

def validate_letter(already_tried_letters, letter):
    if letter.upper() == "QUIT":
        exit("Quitting...")
    elif letter.isalpha() == False:
        print("This didn't look like a letter.")
        return True
    elif is_already_tried(already_tried_letters, letter.lower()):
        print(f"\033[91mYou've already tried this letter {already_tried_letters}\033[0m")
        return True
    else:
        if letter.upper() in word_to_guess.upper():
            return True
        else:
            wrongies.append(letter)
            print(wrongies)
            return False

# if the letter is not present in the word decrease the value in the lives variable
# and display a hangman ASCII art. 
# STEP 5
# if the letter is present in the word iterate through all the letters in the variable
# word_to_guess. If that letter is present in the already_tried_letters then display it,
# otherwise display "_".
def bekeres(already_tried_letters, guessed, lives):
    letter = input("Please type a letter! ")
    if validate_letter(already_tried_letters, letter):
        for letters in range(len(word_to_guess)):
            if letter.upper() == word_to_guess[letters].upper():
                if word_to_guess[letters].isupper():
                    guessed[letters] = letter.upper()
                else:
                    guessed[letters] = letter.lower()
        kiir(guessed)
    else:
        print('\033[93m' + man.HANGMANPICS[7-lives] + '\033[0m')
        lives -= 1
    is_it_the_end(already_tried_letters, lives)
    return lives

# STEP 6
# validate if the typed letter is already in the tried letters
# If it is not, than append to the tried letters
# If it has already been typed, return to STEP 5. HINT: use a while loop here
# this list will contain all the tried letters
def is_already_tried(already_tried_letters, letter):
    letter.lower()
    if letter in already_tried_letters:
        return True
    else:
        already_tried_letters.append(letter)
        return False

def is_it_the_end(already_tried_letters, lives):
    if ''.join(guessed) == word_to_guess:
        exit("You won this time!")
    elif lives == 0:
        exit("You have run out of lives. Good bye!")
    else:
        bekeres(already_tried_letters, guessed, lives)


if __name__ == "__main__":
    wrongies = []
    already_tried_letters = []
    lives = 7
    words_sorted_by_difficulty = scanning()
    diff = difficulty(words_sorted_by_difficulty)
    word_to_guess = choose_a_word(diff)
    guessed = guessed()
    lives = bekeres(already_tried_letters, guessed, lives)
