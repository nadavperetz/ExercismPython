
def is_isogram(word):
    used_letters = []
    for letter in word:
        # ignore non letter character
        if letter.isalpha():
            # cast all letter to lower case
            letter = letter.lower()
            if letter not in used_letters:
                used_letters.append(letter)
            else:
                return False
    return True

