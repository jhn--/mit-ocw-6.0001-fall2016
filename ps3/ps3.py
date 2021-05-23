# 6.0001 Problem Set 3
#
# The 6.0001 Word Game
# Created by: Kevin Luu <luuk> and Jenna Wiens <jwiens>
#
# Name          : <your name>
# Collaborators : <your collaborators>
# Time spent    : <total time>

import math
import random
import string

VOWELS = 'aeiou'
CONSONANTS = 'bcdfghjklmnpqrstvwxyz'
HAND_SIZE = 6  # reduce from 7 to make space for asterix '*'
YES = ['y', 'yes', 'Y', 'YES']
SCRABBLE_LETTER_VALUES = {
    'a': 1, 'b': 3, 'c': 3, 'd': 2, 'e': 1, 'f': 4, 'g': 2, 'h': 4, 'i': 1, 'j': 8, 'k': 5, 'l': 1, 'm': 3, 'n': 1, 'o': 1, 'p': 3, 'q': 10, 'r': 1, 's': 1, 't': 1, 'u': 1, 'v': 4, 'w': 4, 'x': 8, 'y': 4, 'z': 10
}

# -----------------------------------
# Helper code
# (you don't need to understand this helper code)

WORDLIST_FILENAME = "words.txt"


def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.

    Depending on the size of the word list, this function may
    take a while to finish.
    """

    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # wordlist: list of strings
    wordlist = []
    for line in inFile:
        wordlist.append(line.strip().lower())
    print("  ", len(wordlist), "words loaded.")
    return wordlist


def get_frequency_dict(sequence):
    """
    Returns a dictionary where the keys are elements of the sequence
    and the values are integer counts, for the number of times that
    an element is repeated in the sequence.

    sequence: string or list
    return: dictionary
    """

    # freqs: dictionary (element_type -> int)
    freq = {}
    for x in sequence:
        freq[x] = freq.get(x, 0) + 1
    return freq


# (end of helper code)
# -----------------------------------

#
# Problem #1: Scoring a word
#
def get_word_score(word='', n=0):
    """
    Returns the score for a word. Assumes the word is a
    valid word.

    You may assume that the input word is always either a string of letters, 
    or the empty string "". You may not assume that the string will only contain 
    lowercase letters, so you will have to handle uppercase and mixed case strings 
    appropriately. 

        The score for a word is the product of two components:

        The first component is the sum of the points for letters in the word.
        The second component is the larger of:
            1, or
            7*wordlen - 3*(n-wordlen), where wordlen is the length of the word
            and n is the hand length when the word was played

        Letters are scored as in Scrabble; A is worth 1, B is
        worth 3, C is worth 3, D is worth 2, E is worth 1, and so on.

    word: string
    n: int >= 0
    returns: int >= 0
    """

    # pass  # TO DO... Remove this line when you implement this function
    def component_1(word):
        word = word.lower()
        score = 0
        for i in word:
            if i == '*':
                pass  # do not include '*' in the first component of scoring
            else:
                score += SCRABBLE_LETTER_VALUES[i]
        return score

    def component_2(word, n):
        return (7*len(word) - (3*(n-len(word))))

    if len(word) == 0:
        return 0
    elif component_2(word, n) < 1:
        return component_1(word) * 1
    else:
        return component_1(word) * component_2(word, n)

#
# Make sure you understand how this function works and what it does!
#


def display_hand(hand):
    """
    Displays the letters currently in the hand.

    For example:
       display_hand({'a':1, 'x':2, 'l':3, 'e':1})
    Should print out something like:
       a x x l l l e
    The order of the letters is unimportant.

    hand: dictionary (string -> int)
    """
    display = []
    for letter in hand.keys():
        for j in range(hand[letter]):
            display.append(letter)
            # print(letter, end=' ')      # print all on the same line
    # print()                              # print an empty line
    return (' ').join(display)

#
# Make sure you understand how this function works and what it does!
# You will need to modify this for Problem #4.
#


def deal_hand(n):
    """
    Returns a random hand containing n lowercase letters.
    ceil(n/3) letters in the hand should be VOWELS (note,
    ceil(n/3) means the smallest integer not less than n/3).

    Hands are represented as dictionaries. The keys are
    letters and the values are the number of times the
    particular letter is repeated in that hand.

    n: int >= 0
    returns: dictionary (string -> int)
    """

    hand = {}
    num_vowels = int(math.ceil(n / 4))

    for i in range(num_vowels):
        x = random.choice(VOWELS)
        hand[x] = hand.get(x, 0) + 1

    for i in range(num_vowels, n):
        x = random.choice(CONSONANTS)
        hand[x] = hand.get(x, 0) + 1

    hand['*'] = 1

    return hand

#
# Problem #2: Update a hand by removing letters
#


def update_hand(hand, word):
    """
    Does NOT assume that hand contains every letter in word at least as
    many times as the letter appears in word. Letters in word that don't
    appear in hand should be ignored. Letters that appear in word more times
    than in hand should never result in a negative count; instead, set the
    count in the returned hand to 0 (or remove the letter from the
    dictionary, depending on how your code is structured). 

    Updates the hand: uses up the letters in the given word
    and returns the new hand, without those letters in it.

    Has no side effects: does not modify hand.

    word: string
    hand: dictionary (string -> int)    
    returns: dictionary (string -> int)
    """

    # pass  # TO DO... Remove this line when you implement this function
    # convert _LOWERED_ caps word into dict
    word_dic = get_frequency_dict(word.lower())
    hand_copy = hand.copy()  # create a copy of hand
    new_hand = {}

    for letter in word_dic.keys():
        if letter in hand.keys():  # if letter in word is also in hand
            # if letter count in word < letter count in hand
            if hand[letter] - word_dic[letter] > 0:
                # 'copy' the letters from hand to new_hand if remaining _count_ is greater than 0
                new_hand[letter] = hand[letter] - word_dic[letter]
            # delete letter from hand_copy, leaving hand untouched
            del hand_copy[letter]

    for letter in hand_copy.keys():
        # copy whatever's left in hand_copy to new_hand
        new_hand[letter] = hand_copy[letter]
    return new_hand

#
# Problem #3: Test word validity
#


def is_valid_word(word, hand, word_list):
    """
    Returns True if word is in the word_list and is entirely
    composed of letters in the hand. Otherwise, returns False.
    Does not mutate hand or word_list.

    word: string
    hand: dictionary (string -> int)
    word_list: list of lowercase strings
    returns: boolean
    """
    word = word.lower()
    word_dic = get_frequency_dict(word)
    aeoiu = {
        'a': 0,
        'e': 0,
        'i': 0,
        'o': 0,
        'u': 0
    }

    # pass  # TO DO... Remove this line when you implement this function
    def check_hand(word_dic):
        for letter in word_dic.keys():
            if letter == "*":
                pass
            if letter not in hand.keys():
                return False
            elif word_dic[letter] > hand[letter]:
                return False
        return True

    def check_word_list(word, word_list):
        # narrow down the search, use memory to contain
        # a list of words that has the same length as word
        word_list_of_same_length = [
            w for w in word_list if len(w) == len(word)]
        # get the position of the '*' in the word
        index_of_wildcard = word.find('*')

        if '*' in word:
            word_split = word.split('*')
            # i am DEFINITELY DOING SOMETHING INEFFICIENT here
            # i split the word into two - separated by the '*' character
            # then for both parts - which has a position in the word -
            # ie. 'sn*il': ['sn'] HAS to be at position 0
            # ['il'] HAS to be 3
            # once i have ascertained that we do have words that has ['sn'] at position
            # AND
            # ['il'] at position 3
            # I'll push all these words into a variable call word_list_w_wildcard
            #
            # why am i punishing myself like this? -.-"
            #
            # i cannot be sure (and i hate it) but it _feels_ like
            # while it is easier to check existence of words when '*' is in the first or last
            # position, checking if potential words exists when '*' is in the middle
            # will incur more 'if-else's.
            # so i came up w an approach checks the existence of combinations
            # in their exact locations in the other parts of the potential words
            # while keeping track of the position of '*'
            # in order to make sure that the letters of those potential words in that exact
            # position as '*' are vowels
            #
            # the simpler way, but ... feels like a more 'brute-forcey' way
            # will be to substitute '*' which every letter in VOWELS and make multiple
            # loops through either world_list or word_list_of_same_length,
            # keeping a count of successful results,
            # verifying the count is not 0 and return False if it is.
            #
            # on hindsight the brute-forcey way while more detour-y, probably easier to code. haha.
            word_list_w_wildcard = [i for i in word_list_of_same_length if
                                    (i.find(word_split[0], 0,
                                            index_of_wildcard) != -1)
                                    and
                                    (i.find(
                                        word_split[1], index_of_wildcard+1, len(word)) != -1)
                                    ]
            # if word_list_w_wildcard has 0 length, return False
            if len(word_list_w_wildcard) == 0:
                return False
            # but, if word_list_w_wildcard has words in it.
            # I'll consolidate all the letters which are in the same position as '*'
            # and if any of the letters are vowels,
            # i'll consolidate their quantity in dictionary 'aeiou'
            for j in word_list_w_wildcard:
                if j[index_of_wildcard] in aeoiu.keys():
                    aeoiu[j[index_of_wildcard]] += 1
            # if there are no words w any vowels in that particular position occupied by '*',
            # the sum of all the quantity will be 0
            if sum(aeoiu.values()) == 0:
                return False
        else:
            # if no '*' are used, just check if the word exists in the list of words that has the same length
            if word not in word_list_of_same_length:
                return False
        return True

    if (check_hand(word_dic) and check_word_list(word, word_list)) == True:
        return True
    else:
        return False

#
# Problem #5: Playing a hand
#


def calculate_handlen(hand):
    """ 
    Returns the length (number of letters) in the current hand.

    hand: dictionary (string-> int)
    returns: integer
    """
    return sum(hand.values())

    # pass  # TO DO... Remove this line when you implement this function


def play_hand(hand, word_list):
    """
    Allows the user to play the given hand, as follows:

    * The hand is displayed.

    * The user may input a word.

    * When any word is entered (valid or invalid), it uses up letters
      from the hand.

    * An invalid word is rejected, and a message is displayed asking
      the user to choose another word.

    * After every valid word: the score for that word is displayed,
      the remaining letters in the hand are displayed, and the user
      is asked to input another word.

    * The sum of the word scores is displayed when the hand finishes.

    * The hand finishes when there are no more unused letters.
      The user can also finish playing the hand by inputing two 
      exclamation points (the string '!!') instead of a word.

      hand: dictionary (string -> int)
      word_list: list of lowercase strings
      returns: the total score for the hand

    """

    # BEGIN PSEUDOCODE <-- Remove this comment when you implement this function
    # Keep track of the total score
    score = get_word_score()

    # As long as there are still letters left in the hand:
    while calculate_handlen(hand) != 0:
        # Display the hand
        print(f'\nCurrent Hand: {display_hand(hand)}')
        # Ask user for input
        word = input(
            "Enter word, or \"!!\" to indicate  that you are finished: ")
        # If the input is two exclamation points:
        if word == "!!":
            print(f"Total score: {score}")
            # End the game (break out of the loop)
            break
        # Otherwise (the input is not two exclamation points):
        else:
            # If the word is valid:
            if is_valid_word(word, hand, word_list):
                # Tell the user how many points the word earned,
                # and the updated total score
                score += get_word_score(word, calculate_handlen(hand))
                print(
                    f'"{word}" earned {get_word_score(word, calculate_handlen(hand))} points. Total: {score} points')
            # Otherwise (the word is not valid):
            else:
                # Reject invalid word (print a message)
                print(f'That is not a valid word. Please choose another word.')
            # update the user's hand by removing the letters of their inputted word
            hand = update_hand(hand, word)
    # Game is over (user entered '!!' or ran out of letters),
    # so tell user the total score
    if calculate_handlen(hand) == 0:
        print(f'Ran out of letters. Total score: {score} points')
    # Return the total score as result of function
    return score
#
# Problem #6: Playing a game
#


#
# procedure you will use to substitute a letter in a hand
#

def substitute_hand(hand, letter):
    """ 
    Allow the user to replace all copies of one letter in the hand (chosen by user)
    with a new letter chosen from the VOWELS and CONSONANTS at random. The new letter
    should be different from user's choice, and should not be any of the letters
    already in the hand.

    If user provide a letter not in the hand, the hand should be the same.

    Has no side effects: does not mutate hand.

    For example:
        substitute_hand({'h':1, 'e':1, 'l':2, 'o':1}, 'l')
    might return:
        {'h':1, 'e':1, 'o':1, 'x':2} -> if the new letter is 'x'
    The new letter should not be 'h', 'e', 'l', or 'o' since those letters were
    already in the hand.

    hand: dictionary (string -> int)
    letter: string
    returns: dictionary (string -> int)
    """

    # pass  # TO DO... Remove this line when you implement this function
    from random import choice

    # number of occurences for the letter we're replacing
    letter_count = hand[letter]
    new_hand = hand.copy()  # create a shallow copy of hand
    # select from list of letters there are not in hand
    all_letters = VOWELS + CONSONANTS  # create a string of all vowels and consonants
    # randomly choose a letter from all_letters which do not exist in hand
    sub_letter = choice([i for i in all_letters if i not in hand.keys()])
    del new_hand[letter]  # delete the letter we're replacing
    new_hand[sub_letter] = letter_count  # add the newly added letter
    return new_hand


def play_game(word_list):
    """
    Allow the user to play a series of hands

    * Asks the user to input a total number of hands

    * Accumulates the score for each hand into a total score for the 
      entire series

    * For each hand, before playing, ask the user if they want to substitute
      one letter for another. If the user inputs 'yes', prompt them for their
      desired letter. This can only be done once during the game. Once the
      substitue option is used, the user should not be asked if they want to
      substitute letters in the future.

    * For each hand, ask the user if they would like to replay the hand.
      If the user inputs 'yes', they will replay the hand and keep 
      the better of the two scores for that hand.  This can only be done once 
      during the game. Once the replay option is used, the user should not
      be asked if they want to replay future hands. Replaying the hand does
      not count as one of the total number of hands the user initially
      wanted to play.

            * Note: if you replay a hand, you do not get the option to substitute
                    a letter - you must play whatever hand you just had.

    * Returns the total score for the series of hands

    word_list: list of lowercase strings
    """

    # TO DO... Remove this line when you implement this function
    # print("play_game not implemented.")
    num_of_hands = int(input("Enter total number of hands: "))
    hand = deal_hand(HAND_SIZE)
    total_score = 0  # total score from the number of hands
    count = 0  # count the number of hands played
    while count < num_of_hands:  # while the number of hands played is less than the number of hands we want to play
        has_sub_letter = False  # hasn't substitute letter yet
        print(f'Current Hand: {display_hand(hand)}\n')  # show the hand
        if has_sub_letter == False:  # if the letter substitution has not been done
            while input("Would you like to substitute a letter? ").lower() not in YES:
                letter_to_sub = input(
                    "Which letter would you like to replace: ").lower()
                hand = substitute_hand(hand, letter_to_sub)
                has_sub_letter = True
            score = play_hand(hand, word_list)
            if count < num_of_hands:
                replay = input("Would you like to replay the hand? ").lower()
                if replay not in YES:
                    count += 1
                    total_score += score
                    hand = deal_hand(HAND_SIZE)
        print(f'Total score for this hand: {score}')
    print(f'----------')
    print(f'Total score over all hands: {total_score}')


#
# Build data structures used for entire session and play game
# Do not remove the "if __name__ == '__main__':" line - this code is executed
# when the program is run directly, instead of through an import statement
#
if __name__ == '__main__':
    word_list = load_words()
    play_game(word_list)
