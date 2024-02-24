def factoriel(n) -> int:
    """
    Make a recursive function that returns the factorial of a given number.
    :param n:
    :return: the factoriel number
    """
    if n < 0:
        raise ValueError("n must be a positive integer")
    if n > 1:
        return n * factoriel(n - 1)
    else:
        return 1


def fibonacci(n) -> int:
    """
    Make a recursive function that returns the nth fibonacci number.
    :param n:
    :return: the nth fibonacci number
    """
    if n < 0:
        raise ValueError("n must be a positive integer")
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


def binom(n, k) -> int:
    """
    Make a recursive function that returns the binomial coefficient of n and k.
    :param n:
    :param k:
    :return: the binomial coefficient
    """
    if n < 0 or k < 0:
        raise ValueError("n and k must be positive integers")
    if k == 0 and n >= 0:
        return 1
    elif n == 0 and k > 0:
        return 0
    else:
        return binom(n - 1, k - 1) + binom(n - 1, k)


def exposant(a, n) -> int:
    """
    Make a recursive function that returns the exposant of a and n.
    :param a:
    :param n:
    :return: the exposant
    """
    if a < 0 or n < 0:
        raise ValueError("a and n must be positive integers")
    if n == 0:
        return 1
    else:
        return a * exposant(a, n - 1)


def exposant_siplified(a, n) -> int:
    """
    Make a recursive function that returns the exposant of a and n.
    :param a:
    :param n:
    :return: the exposant
    """
    if a < 0 or n < 0:
        raise ValueError("a and n must be positive integers")
    return exposant(a, n / 2) * exposant(a, n / 2)


def is_power(p, n) -> bool:
    """
    Make a recursive function that returns True if n is a power of p.
    :param p:
    :param n:
    :return: boolean
    """
    if p < 0 or n < 1:
        raise ValueError("p and n must be positive integers")
    if n == 1 and p != n:
        return False
    if p == n or (p % n == 0 and is_power(p / n, n)):
        return True
    return False


def pgcd(a, b) -> int:
    """
    Make a recursive function that returns the greatest common divisor of a and b.
    :param a:
    :param b:
    :return: the greatest common divisor
    """
    if a < 0 or b < 0:
        raise ValueError("a and b must be positive integers")
    if b == 0:
        return a
    else:
        return pgcd(b, a % b)


def is_even(n) -> bool:
    """
    Make a recursive function that returns True if n is a pair.
    :param n:
    :return: boolean
    """
    if n < 0:
        raise ValueError("n must be a positive integer")
    if n == 0:
        return True
    elif n == 1:
        return False
    else:
        return is_odd(n - 1)


def is_odd(n) -> bool:
    """
       Make a recursive function that returns True if n is a impair.
       :param n:
       :return: boolean
       """
    if n < 0:
        raise ValueError("n must be a positive integer")
    if n == 0:
        return False
    elif n == 1:
        return True
    else:
        return is_even(n - 1)


def find_dicho(arr, x, low=0, high=None) -> int:
    """
    Make a recursive function that returns True if x is present in arr.
    :param arr:
    :param x:
    :param low:
    :param high:
    :return: boolean
    """
    if high is None:
        high = len(arr) - 1
    if low > high:
        return -1
    mid: int = (low + high) // 2
    if arr[mid] == x:
        return mid
    elif arr[mid] < x:
        return find_dicho(arr, x, mid + 1, high)
    else:
        return find_dicho(arr, x, low, mid - 1)


# not reccursive but work
def my_range(a, b) -> list:
    """
    Return a list of integers from a to b
    :param a:
    :param b:
    :return:
    """
    return [i for i in range(a, b + 1)]


# thx internet
# https://stackoverflow.com/questions/13109274/python-recursion-permutations
def perms(n):
    if not n:
        yield []
    yield from ([n[i], *p] for i in range(len(n)) for p in perms(n[:i] + n[i + 1:]))
