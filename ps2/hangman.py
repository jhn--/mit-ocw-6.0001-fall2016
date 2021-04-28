# Problem Set 2, hangman.py
# Name:
# Collaborators:
# Time spent:

# Hangman Game
# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)
import random
import string

WORDLIST_FILENAME = "words.txt"
_VOWELS = "aeiou"


def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.

    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist


def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    # return "tact"
    return random.choice(wordlist)

# end of helper code

# -----------------------------------


# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = load_words()


def is_word_guessed(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing; assumes all letters are
      lowercase
    letters_guessed: list (of letters), which letters have been guessed so far;
      assumes that all letters are lowercase
    returns: boolean, True if all the letters of secret_word are in letters_guessed;
      False otherwise
    '''
    if len(letters_guessed) == 0:
        return False
    else:
        for i in secret_word:
            if i not in letters_guessed:
                return False
    return True


def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string, comprised of letters, underscores (_), and spaces that represents
      which letters in secret_word have been guessed so far.
    '''
    tmp_secret_word = list(secret_word)
    for i in range(len(tmp_secret_word)):
        if tmp_secret_word[i] not in letters_guessed:
            tmp_secret_word[i] = '_ '
    return ('').join(tmp_secret_word)


def get_available_letters(letters_guessed):
    '''
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string (of letters), comprised of letters that represents which letters have not
      yet been guessed.
    '''
    alphabet = string.ascii_lowercase
    return ('').join([letter for letter in alphabet if letter not in letters_guessed])


def you_win(secret_word, guesses):
    points = len(set(secret_word)) * guesses
    win = f"Congratulations, you won!\nYour total score for this game is: {points}"
    return win


def hangman(secret_word):
    '''
    secret_word: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many
      letters the secret_word contains and how many guesses s/he starts with.

    * The user should start with 6 guesses

    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.

    * Ask the user to supply one guess per round. Remember to make
      sure that the user puts in a letter!

    * The user should receive feedback immediately after each guess
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the
      partially guessed word so far.

    Follows the other limitations detailed in the problem write-up.
    '''
    print(f'Welcome to the game Hangman!')
    print(f'I am thinking of a word that is {len(secret_word)} letters long.')
    print('-------------')
    letters_guessed = []
    guesses = 6
    warnings = 3
    is_it_solved = is_word_guessed(secret_word, letters_guessed)

    while guesses > 0:
        if is_it_solved == False:
            print(f'You have {warnings} warnings left.')
            print(f'You have {guesses} guesses left.')
            print(
                f'Available letters: {get_available_letters(letters_guessed)}')
            guess = input("Please guess a letter: ").lower()
            if guess not in string.ascii_lowercase:  # Verify if letters are in the alphabets
                if guess == ' ':
                    guess = input("Please guess a letter: ").lower()
                else:
                    if warnings <= 0:
                        guesses -= 1
                        print(
                            f'Oops! That is not a valid letter. You have {warnings} warnings left: {get_guessed_word(secret_word, letters_guessed)}')
                    else:
                        warnings -= 1
                        print(
                            f'Oops! That is not a valid letter. You have {warnings} warnings left: {get_guessed_word(secret_word, letters_guessed)}')
            else:
                if guess in letters_guessed:  # if letter has been guessed before
                    if warnings <= 0:  # if no more warnings, remove 1 guesses
                        guesses -= 1
                        print(
                            f"Oops! You've already guessed that letter. You have {warnings} warnings left, deducting 1 guess: {get_guessed_word(secret_word, letters_guessed)}")
                    else:  # remove 1 warning
                        warnings -= 1
                        print(
                            f"Oops! You've already guessed that letter. You now have {warnings} warnings: {get_guessed_word(secret_word, letters_guessed)}")
                else:
                    letters_guessed.append(guess)
                    if (guess in _VOWELS) and (guess not in secret_word):
                      # if letter is a vowel & not in secret_word
                        guesses -= 2
                        print(
                            f'Oops! That letter is not in my word: {get_guessed_word(secret_word, letters_guessed)}')
                    elif (guess not in _VOWELS) and (guess not in secret_word):
                      # if letter is a consonant & not in secret_word
                        guesses -= 1
                        print(
                            f'Oops! That letter is not in my word: {get_guessed_word(secret_word, letters_guessed)}')
                    elif guess in secret_word:
                        is_it_solved = is_word_guessed(
                            secret_word, letters_guessed)
                        print(
                            f"Good guess: {get_guessed_word(secret_word, letters_guessed)}")
                    # print(f"{letters_guessed}")
                    print('-------------')
        else:
            print(you_win(secret_word, guesses))
            return True
            # When you've completed your hangman function, scroll down to the bottom
            # of the file and uncomment the first two lines to test
            # (hint: you might want to pick your own
            # secret_word while you're doing your own testing)
            # -----------------------------------
    print(f"Sorry, you ran out of guesses. The word was {secret_word}.")
    return False


def remove_word_spaces(my_word):
    '''
    my_word: string with _ and ' ' (space) characters, current guess of secret word
    returns: string with ' ' (space) characters removed
    '''
    return ('').join(my_word.split())


def match_with_gaps(my_word, other_word):
    '''
    my_word: string with _ characters, current guess of secret word
    other_word: string, regular English word
    returns: boolean, True if all the actual letters of my_word match the
        corresponding letters of other_word, or the letter is the special symbol
        _ , and my_word and other_word are of the same length;
        False otherwise:
    '''
    if ' ' in my_word:
        # removed the " " spaces and join them back...
        my_word = remove_word_spaces(my_word)
    if len(my_word) != len(other_word):  # so that we can properly compare the length
        return False
    else:
        for i in range(len(my_word)):
            if (my_word[i] != "_") and my_word[i] != other_word[i]:
                return False
            else:
                continue
    return True


def show_possible_matches(my_word):
    '''
    my_word: string with _ characters, current guess of secret word
    returns: nothing, but should print out every word in wordlist that matches my_word
             Keep in mind that in hangman when a letter is guessed, all the positions
             at which that letter occurs in the secret word are revealed.
             Therefore, the hidden letter(_ ) cannot be one of the letters in the word
             that has already been revealed.

    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    possible_matches = [word for word in wordlist if match_with_gaps(
        my_word, word) == True]
    if len(possible_matches) == 0:
        print("No matches found")
    else:
        print(possible_matches)


def hangman_with_hints(secret_word):
    '''
    secret_word: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many
      letters the secret_word contains and how many guesses s/he starts with.

    * The user should start with 6 guesses

    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.

    * Ask the user to supply one guess per round. Make sure to check that the user guesses a letter

    * The user should receive feedback immediately after each guess
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the
      partially guessed word so far.

    * If the guess is the symbol *, print out all words in wordlist that
      matches the current guessed word.

    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    pass


# When you've completed your hangman_with_hint function, comment the two similar
# lines above that were used to run the hangman function, and then uncomment
# these two lines and run this file to test!
# Hint: You might want to pick your own secret_word while you're testing.

if __name__ == "__main__":
    # pass

    # To test part 2, comment out the pass line above and
    # uncomment the following two lines.

    secret_word = choose_word(wordlist)
    hangman(secret_word)

###############

    # To test part 3 re-comment out the above lines and
    # uncomment the following two lines.

    # secret_word = choose_word(wordlist)
    # hangman_with_hints(secret_word)
