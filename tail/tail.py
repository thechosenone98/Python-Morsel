from collections import deque


def tail(iterable, length):
    if length <= 0:
        return []
    # Avoid storing the whole iterable in memory by using a double ended queue with a length limitation
    return list(deque(iterable, maxlen=length))


if __name__ == "__main__":
    print(tail([1, 2, 3, 4, 5, 6], 3))
