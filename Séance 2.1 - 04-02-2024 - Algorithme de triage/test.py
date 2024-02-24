import exercice


def test_trace():
    assert exercice.trace([[1, 2, 3], [4, 5, 6], [7, 8, 9]]) == 15
    assert exercice.trace([]) == 0
    assert exercice.trace([[-1, 2, 3], [4, 5, -6], [7, -8, 9]]) == 13


def test_count_negative():
    assert exercice.count_negative([[1, 2, 3], [4, 5, 6], [7, 8, 9]]) == 0
    assert exercice.count_negative([[-1, 2, 3], [4, 5, -6], [7, -8, 9]]) == 3
    assert exercice.count_negative([]) == 0


def test_sum_positive():
    assert exercice.sum_positive([[1, 2, 3], [4, 5, 6], [7, 8, 9]]) == 45
    assert exercice.sum_positive([[-1, 2, 3], [4, 5, -6], [7, -8, 9]]) == 30
    assert exercice.sum_positive([]) == 0


def test_symetrique():
    assert exercice.symetrique([[1, 4, 7],
                                [4, 5, 8],
                                [7, 8, 9]]) is True
    assert exercice.symetrique([]) is False
    assert exercice.symetrique([[1, 2, 3],
                                [4, 5, 6],
                                [7, 8, 9]]) is False


def test_antisymetrique():
    assert exercice.antisymetrique([[0, -4, -7],
                                    [4, 0, -8],
                                    [7, 8, 0]]) is True
    assert exercice.antisymetrique([]) is False
    assert exercice.antisymetrique([[0, 2, 3],
                                    [4, 0, 6],
                                    [7, 8, 0]]) is False


def test_matric_product():
    assert exercice.matric_product([[0, 1, 3, 0], [8, 5, 0, 6], [0, 0, 1, 1]],
                                   [[0, 1], [0, 0], [3, 3], [9, 5]]) == [[9, 9], [54, 38], [12, 8]]


def test_ne_triangle():
    assert exercice.ne_triangle(3) == ["***", " **", "  *"]


def test_ne_triangle_numbers():
    assert exercice.ne_triangle_numbers(3) == ["123", " 12", "  1"]


def test_tri_selection():
    assert exercice.tri_selection([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]
    assert exercice.tri_selection([4, 2, 1, 3, 5]) == [1, 2, 3, 4, 5]
    assert exercice.tri_selection([]) == []


def test_tri_insertion():
    assert exercice.tri_insertion([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]
    assert exercice.tri_insertion([4, 2, 1, 3, 5]) == [1, 2, 3, 4, 5]
    assert exercice.tri_insertion([]) == []


def test_dichotomy_search():
    assert exercice.dichotomy_search([1, 2, 3], 2) == 1
    assert exercice.dichotomy_search([1, 2, 3, 4, 5, 6, 7, 8, 9], 10) == -1
    assert exercice.dichotomy_search([1, 2, 3, 4, 5, 6, 7, 8, 9], 5) == 4


def test_lower_than_x():
    assert exercice.lower_than_x([1, 2, 3, 4], 5) == 0
    assert exercice.lower_than_x([4, 2, 3, 2], 3) == 1
    assert exercice.lower_than_x([6, 9, 3], 2) == -1


def main():
    test_trace()
    test_count_negative()
    test_sum_positive()
    test_symetrique()
    test_antisymetrique()
    test_matric_product()
    test_ne_triangle()
    test_ne_triangle_numbers()
    test_tri_selection()
    test_lower_than_x()


if __name__ == '__main__':
    main()
