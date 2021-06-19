# Problem Set 4B
# Name: <your name here>
# Collaborators:
# Time Spent: x:xx

import string

### HELPER CODE ###


def load_words(file_name):
    '''
    file_name (string): the name of the file containing
    the list of words to load

    Returns: a list of valid words. Words are strings of lowercase letters.

    Depending on the size of the word list, this function may
    take a while to finish.
    '''
    print("Loading word list from file...")
    # inFile: file
    inFile = open(file_name, 'r')
    # wordlist: list of strings
    wordlist = []
    for line in inFile:
        wordlist.extend([word.lower() for word in line.split(' ')])
    print("  ", len(wordlist), "words loaded.")
    return wordlist


def is_word(word_list, word):
    '''
    Determines if word is a valid word, ignoring
    capitalization and punctuation

    word_list (list): list of words in the dictionary.
    word (string): a possible word.

    Returns: True if word is in word_list, False otherwise

    Example:
    >>> is_word(word_list, 'bat') returns
    True
    >>> is_word(word_list, 'asdf') returns
    False
    '''
    word = word.lower()
    word = word.strip(" !@#$%^&*()-_+={}[]|\:;'<>?,./\"")
    return word in word_list


def get_story_string():
    """
    Returns: a story in encrypted text.
    """
    f = open("story.txt", "r")
    story = str(f.read())
    f.close()
    return story

### END HELPER CODE ###


WORDLIST_FILENAME = 'words.txt'


class Message(object):
    def __init__(self, text):
        '''
        Initializes a Message object

        text (string): the message's text

        a Message object has two attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words)
        '''
        # pass #delete this line and replace with your code here
        self.message_text = text
        self.valid_words = load_words('./words.txt')

    def get_message_text(self):
        '''
        Used to safely access self.message_text outside of the class

        Returns: self.message_text
        '''
        # pass #delete this line and replace with your code here
        # print(self.message_text.split())
        return self.message_text

    def get_valid_words(self):
        '''
        Used to safely access a copy of self.valid_words outside of the class.
        This helps you avoid accidentally mutating class attributes.

        Returns: a COPY of self.valid_words
        '''
        # pass #delete this line and replace with your code here
        self.valid_words_copy = self.valid_words
        return self.valid_words_copy

    def build_shift_dict(self, shift):
        '''
        Creates a dictionary that can be used to apply a cipher to a letter.
        The dictionary maps every uppercase and lowercase letter to a
        character shifted down the alphabet by the input shift. The dictionary
        should have 52 keys of all the uppercase letters and all the lowercase
        letters only.

        shift (integer): the amount by which to shift every letter of the
        alphabet. 0 <= shift < 26

        Returns: a dictionary mapping a letter (string) to
                 another letter (string).
        '''
        # pass #delete this line and replace with your code here
        upper_case = [65, 90]
        lower_case = [97, 122]
        self.shift_dict = {letter: '' for letter in string.ascii_letters}

        for letter in self.shift_dict.keys():  # for each letter in shift_dict
            # if we're shifting upper case
            if upper_case[0] <= ord(letter) <= upper_case[1]:
                if (ord(letter) + shift) > upper_case[1]:  # shift exceeds 'Z'
                    shifted_char = (((ord(letter) + shift) %
                                     upper_case[1]) + upper_case[0]) - 1  # loop back to 'A'
                else:
                    shifted_char = ord(letter) + shift
            else:  # shift lower case
                if (ord(letter) + shift) > lower_case[1]:  # shift exceeds 'z'
                    shifted_char = (((ord(letter) + shift) %
                                     lower_case[1]) + lower_case[0]) - 1  # loop back to 'a'
                else:
                    shifted_char = ord(letter) + shift
            self.shift_dict[letter] = chr((shifted_char))  # populate
        return self.shift_dict

    def apply_shift(self, shift):
        '''
        Applies the Caesar Cipher to self.message_text with the input shift.
        Creates a new string that is self.message_text shifted down the
        alphabet by some number of characters determined by the input shift

        shift (integer): the shift with which to encrypt the message.
        0 <= shift < 26

        Returns: the message text (string) in which every character is shifted
             down the alphabet by the input shift
        '''
        # pass  # delete this line and replace with your code here
        # convert self.get_message_text() to a list
        # for each element (i) in list
        # if i is an alphabet (both upper and lower case)
        # run it through self.shift_dict and return the corresponding shifted letter
        # else, just 'append' i and move on
        return ('').join([self.shift_dict[i] if i in string.ascii_letters else i for i in list(
            self.get_message_text())])


class PlaintextMessage(Message):
    def __init__(self, text, shift):
        '''
        Initializes a PlaintextMessage object

        text (string): the message's text
        shift (integer): the shift associated with this message

        A PlaintextMessage object inherits from Message and has five attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words)
            self.shift (integer, determined by input shift)
            self.encryption_dict (dictionary, built using shift)
            self.message_text_encrypted (string, created using shift)

        '''
        # pass  # delete this line and replace with your code here
        Message.__init__(self, text)
        self.message_text = text
        self.valid_words = self.get_valid_words()
        self.shift = shift
        self.encryption_dict = self.build_shift_dict(self.shift)
        self.message_text_encrypted = self.apply_shift(self.shift)

    def get_shift(self):
        '''
        Used to safely access self.shift outside of the class

        Returns: self.shift
        '''
        # pass  # delete this line and replace with your code here
        return self.shift

    def get_encryption_dict(self):
        '''
        Used to safely access a copy self.encryption_dict outside of the class

        Returns: a COPY of self.encryption_dict
        '''
        # pass  # delete this line and replace with your code here
        return self.encryption_dict

    def get_message_text_encrypted(self):
        '''
        Used to safely access self.message_text_encrypted outside of the class

        Returns: self.message_text_encrypted
        '''
        # pass  # delete this line and replace with your code here
        return self.message_text_encrypted

    def change_shift(self, shift):
        '''
        Changes self.shift of the PlaintextMessage and updates other
        attributes determined by shift.

        shift (integer): the new shift that should be associated with this message.
        0 <= shift < 26

        Returns: nothing
        '''
        # pass  # delete this line and replace with your code here
        if (shift <= 0) or (25 < shift):
            raise Exception("Number must be between 0 and 25.")
        else:
            try:
                self.shift = shift
            except Exception as e:
                raise Exception("Unable to assign new shift value, " + e)
            else:
                self.encryption_dict = self.build_shift_dict(self.shift)


class CiphertextMessage(Message):
    def __init__(self, text):
        '''
        Initializes a CiphertextMessage object

        text (string): the message's text

        a CiphertextMessage object has two attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words)
        '''
        # pass  # delete this line and replace with your code here
        Message.__init__(self, text)
        self.message_text = text
        self.valid_words = self.get_valid_words()
        self.best = {k: None for k in range(1, 27)}
        self.best_keys = []

    def decrypt_message(self):
        '''
        Decrypt self.message_text by trying every possible shift value
        and find the "best" one. We will define "best" as the shift that
        creates the maximum number of real words when we use apply_shift(shift)
        on the message text. If s is the original shift value used to encrypt
        the message, then we would expect 26 - s to be the best shift value
        for decrypting it.

        Note: if multiple shifts are equally good such that they all create
        the maximum number of valid words, you may choose any of those shifts
        (and their corresponding decrypted messages) to return

        Returns: a tuple of the best shift value used to decrypt the message
        and the decrypted message text using that shift value
        '''
        # pass  # delete this line and replace with your code here
        # create a dictionary of keys - shift and the number of valid words they produce post decryption
        for k in self.best.keys():
            # print(k)
            self.decryption_dict = self.build_shift_dict(k)
            self.best[k] = len([w for w in self.apply_shift(
                k).split() if is_word(self.valid_words, w)])

        # create a list of keys that produces the highest number of valid words
        for i in range(len(self.message_text), 0, -1):
            if i in self.best.values():
                self.best_keys = [
                    k for k in self.best.keys() if self.best[k] == i]
                break

        # have to rebuild self.shift_dict
        self.decryption_dict = self.build_shift_dict(self.best_keys[0])
        # just gonna return the first element in the list of potentially more than 1 keys
        return (self.best_keys[0], self.apply_shift(self.best_keys[0]))


if __name__ == '__main__':

    #    #Example test case (PlaintextMessage)
    #    plaintext = PlaintextMessage('hello', 2)
    #    print('Expected Output: jgnnq')
    #    print('Actual Output:', plaintext.get_message_text_encrypted())
    #
    #    #Example test case (CiphertextMessage)
    #    ciphertext = CiphertextMessage('jgnnq')
    #    print('Expected Output:', (24, 'hello'))
    #    print('Actual Output:', ciphertext.decrypt_message())

    # TODO: WRITE YOUR TEST CASES HERE

    # TODO: best shift value and unencrypted story

    # pass  # delete this line and replace with your code here
    # Example test case (PlaintextMessage)
    plaintext = PlaintextMessage('hello', 2)
    print('Expected Output: jgnnq')
    print('Actual Output:', plaintext.get_message_text_encrypted())

    # Example test case (CiphertextMessage)
    ciphertext = CiphertextMessage('jgnnq')
    print('Expected Output:', (24, 'hello'))
    print('Actual Output:', ciphertext.decrypt_message())

    ciphertext = CiphertextMessage(get_story_string())
    print(f'Actual Output: \n {ciphertext.decrypt_message()}')
