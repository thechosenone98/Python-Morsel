from collections import Counter
from unicodedata import category as cat


def strip_punctuation(word):
    if cat(word[0]).startswith('P'):
        return word[1:]
    elif cat(word[-1]).startswith('P'):
        return word[:-1]
    return word

def count_words(s: str):
    # Split string into a word list
    word_list = s.lower().split()
    # Remove punctation outside of words
    word_list = [strip_punctuation(word) for word in word_list]
    return Counter(word_list)

if __name__ == '__main__':
    print(count_words("oh wha-t a, day what a lovely day"))