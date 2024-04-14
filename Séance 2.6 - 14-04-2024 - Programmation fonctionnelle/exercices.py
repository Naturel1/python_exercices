import math
from functools import reduce


# ex 1

def map_abs(x: list) -> list:
    return list(map(abs, x))


# ex 2
def divise_liste100(x: list) -> list:
    return list(map(lambda i: i / 100, x))


# ex 3
def divise_list_len(x: list) -> list:
    return list(map(lambda i: i / len(x), x))


# ex 4
def only_even(x: list) -> list:
    return list(filter(lambda i: i % 2 == 0, x))


# ex 5
def divdable(div, x: list) -> list:
    return list(filter(lambda i: i % div == 0, x))


# ex 6
def product(x: list) -> int:
    return reduce(lambda i, j: i * j, x)


# ex 7
def maximum(x: list) -> int:
    return reduce(lambda i, j: i if i > j else j, x)


# ex 8
def inner_product(x: tuple[int, ...], y: tuple[int, ...]) -> int:
    return sum(list(map(lambda i, j: i * j, x, y)))


# ex 9
def map_sinus(x: list) -> list:
    return list(map(lambda i: math.sin(i), x))


# ex 10
def filter_dico(x: dict, index) -> set:
    return {key for key, value in x.items() if value >= index}


# ex 11
def count_palindrome(x: list[str]) -> int:
    def is_palindrome(y: str) -> bool:
        for i in range(len(y) // 2):
            print(y[i], y[-i - 1])
            if y[i] != y[-i - 1]:
                return False
        return True

    return len(list(filter(is_palindrome, x)))


# ex 12
def factorial(x: int) -> int:
    if x == 0:
        return 1
    return reduce(lambda i, j: i * j, range(1, x + 1))


# ex 13
