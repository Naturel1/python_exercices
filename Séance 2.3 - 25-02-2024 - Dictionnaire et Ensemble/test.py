from exercices import *


def test_adn_to_dict():
    assert adn_to_dict("ACCTAGCCATGTAGAATCGCCTAGGCTTTAGCTAGCTCTAGCTAGCTG") == {'AC': 1, 'CT': 2, 'AG': 3, 'CC': 1,
                                                                               'AT': 1, 'GT': 1, 'AA': 1, 'TC': 2,
                                                                               'GC': 6, 'TT': 1, 'TA': 4, 'TG': 1}
    assert adn_to_dict("AAGGTT") == {"AA": 1, "GG": 1, "TT": 1}
    assert adn_to_dict("") == {}


def test_dict_to_list():
    assert dict_to_list({}) == []
    assert dict_to_list({"a": 1, "b": 2}) == ["Key : a - Value : 1", "Key : b - Value : 2"]
    assert dict_to_list({"a": 1, "b": 2, "c": 3}) == ["Key : a - Value : 1", "Key : b - Value : 2",
                                                      "Key : c - Value : 3"]
    assert dict_to_list({"a": 1, "b": 2, "c": 3, "d": 4}) == ["Key : a - Value : 1", "Key : b - Value : 2",
                                                              "Key : c - Value : 3", "Key : d - Value : 4"]


def test_age_average():
    assert age_average([{'Age': 18, 'Name': 'Marie'},
                        {'Age': 19, 'Name': 'Robert'},
                        {'Age': 27, 'Name': 'Ilker'},
                        {'Age': 33, 'Name': 'Anastasia'}]) == 24.25
    assert age_average([{'Age': 18, 'Name': 'Marie'},
                        {'Age': 19, 'Name': 'Robert'},
                        {'Age': 27, 'Name': 'Ilker'},
                        {'Age': 33, 'Name': 'Anastasia'},
                        {'Age': 25, 'Name': 'Arnaud'}]) == 24.4
    assert age_average([]) == 0


def test_list_to_dict():
    assert list_to_dict([]) == {}
    assert list_to_dict([("a", 1), ("b", 2), ("c", 3)]) == {"a": 1, "b": 2, "c": 3}
    assert list_to_dict([("a", 1), ("b", 2), ("c", 3), ("d", 4)]) == {"a": 1, "b": 2, "c": 3, "d": 4}
    assert list_to_dict([("a", 1), ("b", 2), ("c", 3), ("d", 4), ("e", 5)]) == {"a": 1, "b": 2, "c": 3, "d": 4, "e": 5}


def test_fusion_dict():
    assert fusion_dict({"a": 1, "b": 2}, {"a": 3}) == {"a": 4, "b": 2}
    assert fusion_dict({"a": 1, "b": 2}, {"a": 3, "c": 4}) == {"a": 4, "b": 2, "c": 4}
    assert fusion_dict({}, {}) == {}


def test_invert_dico():
    assert invert_dict({"a": 1, "b": 2}) == {1: "a", 2: "b"}
    assert invert_dict({"a": 1, "b": 2, "c": 3}) == {1: "a", 2: "b", 3: "c"}
    assert invert_dict({}) == {}


def test_average_age_file():
    assert average_age_file("./prenom_trop_long.txt") == 50.2546980159077


def test_verif_password():
    assert verif_password("azerty") == {"minusule": True, "majuscule": False, "chiffre": False, "caractere": False}
    assert verif_password("$azerty1234$") == {"minusule": True, "majuscule": False, "chiffre": True, "caractere": True}
    assert verif_password("") == {"minusule": False, "majuscule": False, "chiffre": False, "caractere": False}
    assert verif_password("AzErTy123€") == {"minusule": True, "majuscule": True, "chiffre": True, "caractere": True}
