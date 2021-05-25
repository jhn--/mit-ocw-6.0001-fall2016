# Problem Set 4A
# Name: <your name here>
# Collaborators:
# Time Spent: x:xx

def get_permutations(sequence):
    '''
    Enumerate all permutations of a given string

    sequence (string): an arbitrary string to permute. Assume that it is a
    non-empty string.  

    You MUST use recursion for this part. Non-recursive solutions will not be
    accepted.

    Returns: a list of all permutations of sequence

    Example:
    >>> get_permutations('abc')
    ['abc', 'acb', 'bac', 'bca', 'cab', 'cba']

    Note: depending on your implementation, you may return the permutations in
    a different order than what is listed here.
    '''

    # pass #delete this line and replace with your code here
    # base case
    if len(sequence) == 1:  # if there's only one letter in sequence
        return [sequence]  # return sequence (in a list!!!)

    # remove one letter from the front of sequence (to be inserted)
    # and pump the remaining letters back
    # into permutations() whose results
    # will be the permutations of the
    # remaining letters
    list_of_permutations = get_permutations(sequence[1:])
    letter_to_insert = sequence[:1]
    result = []  # results to hold permutations

    # loop through each element in the list_of_permutations
    for permutation in list_of_permutations:
        # loop through each position of the permutation
        for i in range(len(permutation)+1):
            # inser the removed letter into the permutations
            # in the positition (i) as (i) traverse across
            result.append(permutation[:i] + letter_to_insert + permutation[i:])

    return result


if __name__ == '__main__':
    #    #EXAMPLE
    #    example_input = 'abc'
    #    print('Input:', example_input)
    #    print('Expected Output:', ['abc', 'acb', 'bac', 'bca', 'cab', 'cba'])
    #    print('Actual Output:', get_permutations(example_input))

    #    # Put three example test cases here (for your sanity, limit your inputs
    #    to be three characters or fewer as you will have n! permutations for a
    #    sequence of length n)

    # pass #delete this line and replace with your code here
    input = 'abc'
    print('Input: ', input)
    print('Expected Output: ', ['abc', 'acb', 'bac', 'bca', 'cab', 'cba'])
    print('Actual Output: ', get_permutations(input))

    input = 'ab'
    print('Input: ', input)
    print('Expected Output: ', ['ab', 'ba'])
    print('Actual Output: ', get_permutations(input))

    input = 'abcd'
    print('Input: ', input)
    print('Expected Output: ', ['abcd', 'bacd', 'bcad', 'bcda', 'acbd', 'cabd', 'cbad', 'cbda', 'acdb', 'cadb',
                                'cdab', 'cdba', 'abdc', 'badc', 'bdac', 'bdca', 'adbc', 'dabc', 'dbac', 'dbca', 'adcb', 'dacb', 'dcab', 'dcba'])
    print('Actual Output: ', get_permutations(input))
