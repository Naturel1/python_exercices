from exercices import *
from exercices_sup import *
import pytest


def test_factoriel():
    with pytest.raises(ValueError):
        assert factoriel(-1)
    assert factoriel(0) == 1
    assert factoriel(1) == 1
    assert factoriel(2) == 2
    assert factoriel(3) == 6
    assert factoriel(4) == 24
    assert factoriel(5) == 120
    assert factoriel(6) == 720
    assert factoriel(7) == 5040
    assert factoriel(8) == 40320
    assert factoriel(9) == 362880
    assert factoriel(10) == 3628800
    assert factoriel(11) == 39916800
    assert factoriel(12) == 479001600
    assert factoriel(13) == 6227020800


def test_fibonacci():
    with pytest.raises(ValueError):
        assert fibonacci(-1)
    assert fibonacci(0) == 0
    assert fibonacci(1) == 1
    assert fibonacci(2) == 1
    assert fibonacci(3) == 2
    assert fibonacci(4) == 3
    assert fibonacci(5) == 5
    assert fibonacci(6) == 8
    assert fibonacci(7) == 13
    assert fibonacci(8) == 21
    assert fibonacci(9) == 34
    assert fibonacci(10) == 55
    assert fibonacci(11) == 89
    assert fibonacci(12) == 144
    assert fibonacci(13) == 233
    assert fibonacci(14) == 377


def test_binom():
    with pytest.raises(ValueError):
        assert binom(-1, 0)
    with pytest.raises(ValueError):
        assert binom(0, -1)
    assert binom(0, 0) == 1
    assert binom(1, 0) == 1
    assert binom(1, 1) == 1
    assert binom(2, 0) == 1
    assert binom(2, 1) == 2
    assert binom(2, 2) == 1
    assert binom(3, 0) == 1
    assert binom(3, 1) == 3
    assert binom(3, 2) == 3
    assert binom(3, 3) == 1
    assert binom(4, 0) == 1
    assert binom(4, 1) == 4


def test_exposant():
    with pytest.raises(ValueError):
        assert exposant(-1, 0)
    with pytest.raises(ValueError):
        assert exposant(0, -1)
    assert exposant(0, 0) == 1
    assert exposant(1, 0) == 1
    assert exposant(1, 1) == 1
    assert exposant(2, 0) == 1
    assert exposant(2, 1) == 2
    assert exposant(2, 2) == 4
    assert exposant(3, 0) == 1
    assert exposant(3, 1) == 3
    assert exposant(3, 2) == 9
    assert exposant(3, 3) == 27


def test_exposant_siplified():
    with pytest.raises(ValueError):
        assert exposant_siplified(-1, 0)
        assert exposant_siplified(0, -1)
    assert exposant_siplified(0, 0) == 1
    assert exposant_siplified(2, 24) == 16777216
    assert exposant_siplified(2, 26) == 67108864
    assert exposant_siplified(3, 28) == 22876792454961


def test_is_power():
    with pytest.raises(ValueError):
        assert is_power(-1, 0)
        assert is_power(0, -1)
        assert is_power(0, 0)
        assert is_power(1, 0)
    assert is_power(1, 1) is True
    assert is_power(2, 1) is False
    assert is_power(2, 2) is True
    assert is_power(3, 1) is False
    assert is_power(3, 2) is False
    assert is_power(3, 3) is True
    assert is_power(4, 1) is False
    assert is_power(4, 2) is True
    assert is_power(4, 3) is False
    assert is_power(4, 4) is True
    assert is_power(5, 1) is False


def test_pgcd():
    with pytest.raises(ValueError):
        assert pgcd(-1, 0)
        assert pgcd(0, -1)
        assert pgcd(0, 0)
    assert pgcd(1, 1) == 1
    assert pgcd(2, 1) == 1
    assert pgcd(2, 2) == 2
    assert pgcd(221, 782) == 17


def test_is_even():
    with pytest.raises(ValueError):
        assert is_even(-1)
    assert is_even(1) is False
    assert is_even(2) is True
    assert is_even(3) is False
    assert is_even(4) is True
    assert is_even(5) is False
    assert is_even(6) is True
    assert is_even(7) is False
    assert is_even(8) is True
    assert is_even(9) is False
    assert is_even(10) is True
    assert is_even(11) is False
    assert is_even(12) is True
    assert is_even(13) is False
    assert is_even(14) is True
    assert is_even(15) is False
    assert is_even(16) is True


def test_is_odd():
    with pytest.raises(ValueError):
        assert is_odd(-1)
    assert is_odd(1) is True
    assert is_odd(2) is False
    assert is_odd(3) is True
    assert is_odd(4) is False
    assert is_odd(5) is True
    assert is_odd(6) is False
    assert is_odd(7) is True
    assert is_odd(8) is False
    assert is_odd(9) is True
    assert is_odd(10) is False
    assert is_odd(11) is True
    assert is_odd(12) is False
    assert is_odd(13) is True
    assert is_odd(14) is False
    assert is_odd(15) is True
    assert is_odd(16) is False


def test_find_dicho():
    assert find_dicho([1, 2], 2) == 1
    assert find_dicho([1, 2, 3], 2) == 1
    assert find_dicho([1, 2, 3], 3) == 2
    assert find_dicho([1, 2, 3], 4) == -1


def test_my_range():
    assert my_range(1, 10) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    assert my_range(0, 10) == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    assert my_range(0, 0) == [0]
    assert my_range(0, 1) == [0, 1]


def test_perms():
    assert list(perms("0")) == [["0"]]
    assert list(perms("1")) == [["1"]]
    assert list(perms("12")) == [["1", "2"], ["2", "1"]]


def test_sum_number():
    assert sum_number(0) == 0
    assert sum_number(1) == 1
    assert sum_number(12) == 3
    assert sum_number(123) == 6
    assert sum_number(1234) == 10
    assert sum_number(12345) == 15
    assert sum_number(123456) == 21
    assert sum_number(1234567) == 28
    assert sum_number(12345678) == 36
    assert sum_number(123456789) == 45


def test_power():
    assert power(2, 0) == 1
    assert power(2, 1) == 2
    assert power(2, 2) == 4
    assert power(2, 3) == 8
    assert power(2, 4) == 16
    assert power(2, 5) == 32
    assert power(2, 6) == 64


def test_count_down():
    assert count_down(1) == "1"
    assert count_down(2) == "21"
    assert count_down(3) == "321"
    assert count_down(4) == "4321"
    assert count_down(5) == "54321"


def test_even_number():
    assert even_numbers([0]) == [0]
    assert even_numbers([1]) == []
    assert even_numbers([1, 2, 3, 4]) == [2, 4]
