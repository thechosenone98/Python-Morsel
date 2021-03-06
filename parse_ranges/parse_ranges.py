from typing import List


def parse_ranges(s: str) -> List[int]:
    """Generator yielding number contained in all the subrange defined in the input string
    eg. s = "1-2, 4-4, 8-10" it will yield 1, 2, 4, 8, 9, 10"""
    # Remove all spaces from string
    s = s.translate(str.maketrans("", "", " "))
    for num_range in s.split(','):
        # Start by checking if there is an arrow in the range
        start, found, end = num_range.partition('-')
        if not found or end.startswith('>'):
            yield int(start)
        else:
            yield from range(int(start), int(end) + 1)

if __name__ == '__main__':
    print(list(parse_ranges("1-2,4-4,5,8-10")))
    