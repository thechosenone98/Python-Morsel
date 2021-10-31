from collections import Counter

def count_words(s: str):
    return Counter(s.split())

if __name__ == '__main__':
    print(count_words("oh what a day what a lovely day"))