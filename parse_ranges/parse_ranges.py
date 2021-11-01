from typing import List


def parse_ranges(s: str) -> List[int]:
    # Remove all spaces from string
    s = s.translate(str.maketrans("", "", " "))
    range_list = []
    for ranges in s.split(','):
        low, high = map(int, ranges.split('-'))
        range_list.extend(list(range(low, high + 1)))
    return range_list

if __name__ == '__main__':
    print(parse_ranges("1-2,4-4,8-10"))
    