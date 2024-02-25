def adn_to_dict(adn) -> dict:
    """
    Make a function that takes an adn string and returns a dictionary
    :param adn:
    :return:
    """
    adn_dict: dict = {}
    for i in range(0, len(adn), 2):
        nucle = adn[i] + adn[i + 1]
        if nucle not in adn_dict:
            adn_dict[nucle] = 1
        else:
            adn_dict[nucle] += 1
    return adn_dict


def dict_to_list(dico) -> list:
    """
    Make a function that takes a dictionary and returns a list
    :param dico:
    :return:
    """
    output: list = []
    for x in dico:
        output.append("Key : " + str(x) + " - Value : " + str(dico[x]))
    return output


def age_average(personnes) -> float:
    """
    Make a function that takes a list of dictionaries and returns the average age
    :param personnes:
    :return:
    """
    if len(personnes) == 0:
        return 0
    age_sum = 0
    for personne in personnes:
        age_sum += personne['Age']
    return age_sum / len(personnes)


def ex4_demo() -> None:
    """
    Make a demo for the exercice 4
    """
    city = {"nom": "Montreal", "pays": "Canada", "province": "Quebec", "pop": 1825208, "superficie": 315}
    city["superficie"] = 365
    city["densite"] = 4992
    city["population"] = city["pop"]
    del city["pop"]


def list_to_dict(l) -> dict:
    """
    Make a function that takes a list and returns a dictionary
    :param l:
    :return:
    """
    d: dict = {}
    for x in l:
        d[x[0]] = x[1]
    return d


def fusion_dict(d1, d2) -> dict:
    """
    Make a function that takes two dictionaries and returns a new dictionary
    :param d1:
    :param d2:
    :return:
    """
    for x in d2:
        if x in d1:
            d1[x] += d2[x]
        else:
            d1[x] = d2[x]
    return d1


def invert_dict(dico) -> dict:
    """
    Make a function that takes a dictionary and returns an inverted dictionary
    :param dico:
    :return:
    """
    output: dict = {}
    for x in dico:
        output[dico[x]] = x
    return output


def average_age_file(file) -> float:
    """
    Make a function that takes a list of dictionaries and returns the average age
    :param file:
    :return:
    """
    av: float = 0
    with open(file, "r") as f:
        test = f.readline().strip("{").strip("}").split(", ")
        for i in test:
            temp: int = int(i.split(":")[1])
            av += temp
        return av / len(test)


def verif_password(password):
    """
    Make a function that return a dictonary indicate if the password is correct or not
    :param password:
    :return:
    """
    info: dict = {"minusule": False, "majuscule": False, "chiffre": False, "caractere": False}
    for x in password:
        if x.islower():
            info["minusule"] = True
        elif x.isupper():
            info["majuscule"] = True
        elif x.isdigit():
            info["chiffre"] = True
        else:
            info["caractere"] = True
    return info


def find_info(file) -> bool:
    """
    find in the file the minimum, maximum and average of the data
    :param file:
    :return:
    """
    with open(file, "r", encoding='utf-8') as f:
        info: list = f.readline()[::-1].split("\t")
        print(info)


def main():
    find_info("./ods087.txt")


if __name__ == "__main__":
    main()
