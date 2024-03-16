def ex_1():
    print("Exercice 1")
    # 1
    personne: dict = {"nom": "Arnaud", "age": 25, "ville": "Bruxelles"}
    print(personne)
    # 2
    personne["age"] += 5
    print(personne)
    # 3
    personne.pop("ville")
    print(personne)


def ex_2():
    print("Exercice 2")
    # 1
    ensemble1: set[int] = {4, 5, 6, 7, 8, 9}
    ensemble2: set[int] = {1, 2, 3, 4, 5, 6}
    # 2
    print(f"ensemble1 : {ensemble1}")
    print(f"ensemble2 : {ensemble2}")
    insertion = ensemble1 & ensemble2
    union = ensemble1 | ensemble2
    print(f"insertion : {insertion}")
    print(f"union : {union}")
    # 3
    ensemble1.add(10)
    ensemble2.remove(6)
    print(f"ensemble1 : {ensemble1}")
    print(f"ensemble2 : {ensemble2}")
    insertion = ensemble1 & ensemble2
    union = ensemble1 | ensemble2
    print(f"insertion : {insertion}")
    print(f"union : {union}")


def ex_3():
    print("Exercice 3")
    # 1
    with open("notes.txt", "w") as f:
        f.write("""|_|0|_|
|_|_|0|
|0|0|0|
""")
    # 2
    with open("notes.txt", "r") as f:
        print(f.read())
    # 3
    with open("notes.txt", "a") as f:
        f.write("""
Do you know the glider?""")
    with open("notes.txt", "r") as f:
        print(f.read())
    # 4
    with open("copie_notes.txt", "w") as f:
        with open("notes.txt", "r") as f1:
            notes = f1.read()
        f.write(notes)


def main():
    ex_1()
    ex_2()
    ex_3()


if __name__ == "__main__":
    main()
