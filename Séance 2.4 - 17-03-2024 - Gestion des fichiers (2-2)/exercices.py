import string
import re
from unidecode import unidecode


def count_letters() -> list[tuple[chr, int]]:
    letters: dict = {}
    with open('hamlet.txt', 'r', encoding="utf-8") as f:
        for line in f:
            for letter in line:
                if letter in string.ascii_letters:
                    if letter not in letters:
                        letters[letter] = 1
                    else:
                        letters[letter] += 1
    return sorted(list(letters.items()), key=lambda x: x[1], reverse=True)


def count_words() -> list[tuple[str, int]]:
    words: dict[str, int] = {}
    with open('hamlet.txt', 'r', encoding="utf-8") as f:
        for line in f:
            for word in line.split(" "):
                _word = re.sub(r"[\n?.!;:\",]", "", word)
                if _word != "" and _word != "-":
                    if _word not in words:
                        words[_word] = 1
                    else:
                        words[_word] += 1
        return sorted(list(words.items()), key=lambda x: x[1], reverse=True)


def crypt_simple() -> None:
    with open("cryptage.txt", "w", encoding="utf-8") as f1:
        with open('hamlet.txt', 'r', encoding="utf-8") as f2:
            for line in f2:
                _line = unidecode(line)
                crypted_line = ""
                print(_line)
                for letter in _line:
                    if letter in string.ascii_letters:
                        if letter == 'z':
                            _letter = 'a'
                        elif letter == 'Z':
                            _letter = 'A'
                        else:
                            code_ascii = ord(letter)
                            _letter = chr(code_ascii + 1)
                        crypted_line += _letter
                    else:
                        crypted_line += letter
                f1.write(crypted_line)


def ex_1():
    # a
    print("Exercice : 1.a")
    print(count_letters())
    # b
    print("Exercice : 1.b")
    print(count_words())
    # c
    print("Exercice : 1.c")
    crypt_simple()



def main():
    ex_1()


if __name__ == '__main__':
    main()
