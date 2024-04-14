import exercices


def test_map_abs():
    assert exercices.map_abs([-1]) == [1]
    assert exercices.map_abs([1]) == [1]
    assert exercices.map_abs([1, 2, 3]) == [1, 2, 3]
    assert exercices.map_abs([-1, -2, -3]) == [1, 2, 3]


def test_divise_liste100():
    assert exercices.divise_liste100([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == [0.01, 0.02, 0.03, 0.04, 0.05, 0.06, 0.07,
                                                                          0.08, 0.09, 0.1]
    assert exercices.divise_liste100([100]) == [1]


def test_divise_list_len():
    assert exercices.divise_list_len([2, 4]) == [1, 2]
    assert exercices.divise_list_len([3, 6, 9]) == [1, 2, 3]


def test_only_even():
    assert exercices.only_even([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == [2, 4, 6, 8, 10]
    assert exercices.only_even([10, 35, 22, 11]) == [10, 22]


def test_divdable():
    assert exercices.divdable(1, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    assert exercices.divdable(2, [10, 35, 22, 11]) == [10, 22]
    assert exercices.divdable(3, [2, 3, 9, 18, 20]) == [3, 9, 18]


def test_product():
    assert exercices.product([1, 2, 3]) == 6
    assert exercices.product([1, 2, 3, 4]) == 24
    assert exercices.product([1, 2, 3, 4, 5]) == 120


def test_maximum():
    assert exercices.maximum([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 10


def test_inner_product():
    assert exercices.inner_product((3, 4), (5, 6)) == 39


def test_map_sinus():
    assert exercices.map_sinus([0]) == [0.0]
    assert exercices.map_sinus([0, 0.009999833334166664]) == [0.0, 0.009999666676666413]


def test_filter_dico():
    assert exercices.filter_dico({"A": 10, "T": 3, "C": 5, "G": 2}, 5) == {"A", "C"}


def test_count_palindrome():
    assert exercices.count_palindrome(["radar", "python", "sos", "socrate"]) == 2


def test_factorial():
    assert exercices.factorial(0) == 1
    assert exercices.factorial(1) == 1
    assert exercices.factorial(2) == 2
    assert exercices.factorial(3) == 6
    assert exercices.factorial(4) == 24
    assert exercices.factorial(5) == 120
    assert exercices.factorial(6) == 720
    assert exercices.factorial(7) == 5040
    assert exercices.factorial(8) == 40320
    assert exercices.factorial(9) == 362880
    assert exercices.factorial(10) == 3628800


