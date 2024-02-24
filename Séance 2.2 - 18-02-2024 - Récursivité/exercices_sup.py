def sum_number(number) -> int:
    """
    Make a recursive function that returns the sum of a given number.
    :param number:
    :return: the sum of the number
    """
    number = list(str(number))

    def recursive_sum(list_number):
        if len(list_number) == 1:
            return int(list_number[0])
        else:
            return int(list_number[0]) + recursive_sum(list_number[1:])

    return recursive_sum(number)


def power(number, exponent) -> int:
    """
    Make a recursive function that returns the power of a given number.
    :param number:
    :param exponent:
    :return: the power of the number
    """
    if exponent == 0:
        return 1
    else:
        return number * power(number, exponent - 1)


def count_down(number) -> str:
    """
    Create a string that counts down from a given number to one.
    :param number:
    :return:
    """
    if number == 1:
        return "1"
    else:
        return str(number) + count_down(number - 1)


def even_numbers(numbers) -> list:
    """
    Make a recursive function that returns a list of the even numbers in a given list.
    :param numbers:
    :return:
    """
    if len(numbers) == 0:
        return []
    elif len(numbers) == 1:
        if numbers[0] % 2 == 0:
            return [numbers[0]]
        else:
            return []
    else:
        if numbers[0] % 2 == 0:
            return [numbers[0]] + even_numbers(numbers[1:])
        else:
            return even_numbers(numbers[1:])
