from datetime import timedelta

from collections.abc import Iterable
def deep_add(l, start=0):
    for item in l:
        if isinstance(item, Iterable):
            start = deep_add(item, start)
        else:
            start += item
    return start

if __name__ == "__main__":
    print(deep_add([1, [2, [3, 4], [], [[5, 6], [7, 8]]]]))
    print(deep_add([[timedelta(5), timedelta(10)], [timedelta(3)]], start=timedelta(0)))
