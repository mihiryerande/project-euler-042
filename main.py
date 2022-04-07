# Problem 42:
#     Coded Triangle Numbers
#
# Description:
#     The n'th term of the sequence of triangle numbers is given by, t_n = ½n(n+1);
#       so the first ten triangle numbers are:
#         1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...
#
#     By converting each letter in a word to a number corresponding to its alphabetical position
#       and adding these values we form a word value.
#     For example, the word value for SKY is 19 + 11 + 25 = 55 = t10.
#     If the word value is a triangle number then we shall call the word a triangle word.
#
#     Using words.txt (right click and 'Save Link/Target As...'),
#       a 16K text file containing nearly two-thousand common English words,
#       how many are triangle words?

from math import floor, sqrt

ALPHA_BASE = ord('A') - 1


def is_triangle_word(w):
    """
    Returns True iff `w` is a 'triangle word',
      meaning the sum of its letters (as numbers) equals a triangle number.

    Args:
        w (str): String containing only uppercase alphabetical characters

    Returns:
        (bool): True iff `w` is a 'triangle word'

    Raises:
        AssertError: if incorrect args are given
    """
    assert type(w) == str and w.isalpha() and w.isupper()
    global ALPHA_BASE

    total = sum(map(lambda c: ord(c) - ALPHA_BASE, list(w)))
    n = floor(sqrt(2 * total))
    return n * (n+1) // 2 == total


def main(filename):
    """
    Returns the count of words in given text file `f` which are 'triangle words'.

    Args:
        filename (str): Name of text file containing words to check.

    Returns:
        (int): Count of `triangle words` in file `f`.

    Raises:
        AssertError: if incorrect args are given
    """
    assert type(filename) == str

    with open(filename, 'r') as f:
        words = list(map(lambda w: w.strip('"').upper(), f.read().strip().split(',')))

    return sum(map(lambda w: is_triangle_word(w), words))


if __name__ == '__main__':
    words_filename = 'words.txt'
    triangle_word_count = main(words_filename)
    print('Amount of triangle words found in file `{}`:'.format(words_filename))
    print('  {}'.format(triangle_word_count))
