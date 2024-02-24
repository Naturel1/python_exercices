def trace(matrice) -> int:
    """
    Trace of a matrix
    :param matrice:
    :return: the trace of the matrix
    """
    trace_val = 0
    for i in range(len(matrice)):
        trace_val += matrice[i][i]
    return trace_val


def count_negative(matrice) -> int:
    """
    Count the number of negative values in a matrix
    :param matrice:
    :return: the number of negative values in the matrix
    """
    count = 0
    for i in matrice:
        for j in i:
            if j < 0:
                count += 1
    return count


def sum_positive(matrice) -> int:
    """
    Sum the positive values in a matrix
    :param matrice:
    :return: the sum of the positive values in the matrix
    """
    sum_val = 0
    for i in matrice:
        for j in i:
            if j > 0:
                sum_val += j
    return sum_val


def symetrique(matrice) -> bool:
    """
    verify if the matrix is symetric or not
    :param matrice:
    :return: boolean if the matrix is symetric or not
    """
    if len(matrice) == 0 or len(matrice[0]) == 0:
        return False
    for i in range(len(matrice)):
        for j in range(i):
            if matrice[i][j] != matrice[j][i]:
                return False
    return True


def antisymetrique(matrice) -> bool:
    """
    verify if the matrix is antisymetric or not
    :param matrice:
    :return: boolean if the matrix is antisymetric or not
    """
    if len(matrice) == 0 or len(matrice[0]) == 0:
        return False
    for i in range(len(matrice)):
        for j in range(i):
            if matrice[i][j] + matrice[j][i] != 0:
                return False
    return True


def matric_product(matrice1, matrice2) -> list:
    """
    Product of two matrices
    :param matrice1:
    :param matrice2:
    :return: product of the two matrices
    """
    matrice_product = []
    for i in range(len(matrice1)):
        matrice_product.append([])
        for k in range(len(matrice2[i])):
            result = 0
            for j in range(len(matrice1[i])):
                result += matrice1[i][j] * matrice2[j][k]
            matrice_product[i].append(result)

    return matrice_product


def ne_triangle(n) -> list:
    """
    print a triangle of size n
    :param n:
    :return list of * in forme of triangle:
    """
    triangle = []
    for i in range(n, 0, -1):
        triangle.append((" " * (n - i)) + ("*" * i))
    return triangle


def ne_triangle_numbers(n) -> list:
    """
    print a triangle of size n
    :param n:
    :return: list of numbers in forme of triangle
    """
    triangle = []
    for i in range(n, 0, -1):
        layer = " " * (n - i)
        for j in range(i):
            layer += str(j + 1)
        triangle.append(layer)
    return triangle


def tri_selection(list_to_sort) -> list:
    """
    Sort a list of integers
    :param list_to_sort:
    :return: sorted list
    """
    for i in range(len(list_to_sort)):
        mini = i
        for j in range(i + 1, len(list_to_sort)):
            if list_to_sort[j] < list_to_sort[mini]:
                mini = j
        list_to_sort[i], list_to_sort[mini] = list_to_sort[mini], list_to_sort[i]
    return list_to_sort


def tri_insertion(list_to_sort) -> list:
    """
    Sort a list of integers
    :param list_to_sort:
    :return: a sorted list
    """
    for i in range(1, len(list_to_sort)):
        keep = list_to_sort[i]
        j = i - 1
        while j >= 0 and list_to_sort[j] > keep:
            list_to_sort[j + 1] = list_to_sort[j]
            j -= 1
        list_to_sort[j + 1] = keep
    return list_to_sort


def dichotomy_search(list_to_sort, element) -> list:
    """
    Search for the element in a list and return the index of the element in the sorted list
    :param list_to_sort:
    :param element:
    :return: the index of the element in the sorted list
    """
    bi, bs = 0, len(list_to_sort)
    m = (bi + bs) // 2
    while bi < bs and element != list_to_sort[m]:
        m = (bi + bs) // 2
        if list_to_sort[m] < element:
            bi = m + 1
        else:
            bs = m
    if len(list_to_sort) <= m or list_to_sort[m] != element:
        m = -1
    return m


def lower_than_x(liste, x):
    index = -1
    for i in range(len(liste)):
        if liste[i] < x:
            index = i
            return index
    return index


def main():
    raise Exception("This file must not be executed as main")


if __name__ == '__main__':
    main()
