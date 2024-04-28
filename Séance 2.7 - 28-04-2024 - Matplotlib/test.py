import exercices


def test_equidistant_values():
    assert exercices.equidistant_values(2, 6, 21) == [2.0, 2.2, 2.4, 2.6, 2.8, 3.0, 3.2, 3.4000000000000004, 3.6, 3.8,
                                                      4.0, 4.2, 4.4, 4.6, 4.800000000000001, 5.0, 5.2, 5.4, 5.6,
                                                      5.800000000000001, 6.0]
