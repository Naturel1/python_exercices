import exercices


def test_tri_poly():
    assert exercices.tri_poly([]) == []
    assert exercices.tri_poly(
        ([[4, 5, 6], [7, 8, 9], [1, 0, 3, 2], [1, 2, 3]])) == [[1, 0, 3, 2], [7, 8, 9], [4, 5, 6], [1, 2, 3]]
    assert exercices.tri_poly(
        ([[4, 5, 6, 1], [7, 8, 9], [1, 2], [1, 0, 3, 2], [0, 2, 11]])) == [[1, 0, 3, 2], [4, 5, 6, 1], [0, 2, 11],
                                                                           [7, 8, 9], [1, 2]]


def test_tri_poly_insert():
    assert exercices.tri_poly_insert([]) == []
    assert exercices.tri_poly_insert(
        ([[4, 5, 6], [7, 8, 9], [1, 0, 3, 2], [1, 2, 3]])) == [[1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 0, 3, 2]]
    assert exercices.tri_poly_insert(
        ([[4, 5, 6, 1], [7, 8, 9], [1, 2], [1, 0, 3, 2], [0, 2, 11]])) == [[1, 2],
                                                                           [7, 8, 9], [0, 2, 11], [4, 5, 6, 1],
                                                                           [1, 0, 3, 2]]


def test_alpha():
    assert exercices.alpha(0.5) == 2.184326171875
    assert exercices.alpha(0.2) == 3.006103515625
