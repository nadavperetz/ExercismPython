from string import ascii_lowercase


def is_pangram(word):
    # Creating alphabet list
    full_list = [letter for letter in ascii_lowercase]
    for letter in word:
        letter = letter.lower()
        if letter in full_list:
            full_list.remove(letter)
    # Python empty list is equivalent to a boolean False, True otherwise
    return not full_list



