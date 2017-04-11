import re


def word_count(phrase):
    word_count_dict = {}
    # Using regular expression, replace ',' '.' '_' '\t' and '\n' to whitespace(' ')
    replaced_phrase = re.sub('[,._\t\n]+', ' ', phrase)
    for word in replaced_phrase.split(" "):
        # Remove non alphanumeric chars
        word = re.sub("[^a-z0-9]+", "", word.lower())
        if word:
            if word in word_count_dict:
                word_count_dict[word] += 1
            else:
                word_count_dict[word] = 1
    return word_count_dict


if __name__ == "__main__":
    print(word_count('rah rah ah ah ah\nroma roma ma\n'
                     'ga ga oh la la\nwant your bad romance'))
