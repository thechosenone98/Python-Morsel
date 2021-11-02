import string
import unicodedata
from collections import Counter

def remove_accents(input_str):
    nfkd_form = unicodedata.normalize('NFKD', input_str)
    return u"".join([c for c in nfkd_form if not unicodedata.combining(c)])

def is_anagram(s1, s2):
    # Remove space characters along with punctuation
    s1 = s1.strip().translate(str.maketrans("", "", string.punctuation + " "))
    s2 = s2.strip().translate(str.maketrans("", "", string.punctuation + " "))
    # Remove accent from letters and make the strings lowercase
    s1 = remove_accents(s1).lower()
    s2 = remove_accents(s2).lower()
    if Counter(s1) == Counter(s2):
        return True
    return False

if __name__ == "__main__":
    print(is_anagram("abå", "ab'a"))