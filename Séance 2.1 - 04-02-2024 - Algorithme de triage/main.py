def find_less_than_50(data):
    for i in data:
        if i < 50:
            return i
    raise Exception("Could not find less than 50")


def find_index_of_less_than_50(data):
    for i in range(len(data)):
        if data[i] < 50:
            return i
    return -1


def find_if_less_than_50(data):
    for i in data:
        if i < 50:
            return True
    return False


def find_min(data):
    if len(data) == 0:
        raise Exception("The list must not be empty")
    minimum = data[0]
    for i in data:
        if i < minimum:
            minimum = i
    return minimum


def find_index_of_min(data):
    index_min = -1
    if len(data) != 0:
        minimum = data[0]
        for i in range(len(data)):
            if data[i] < minimum:
                minimum = data[i]
                index_min = i
    return index_min


def main():
    print("-1-")
    print("Must be 35")
    print(find_less_than_50([78, 65, 100, 50, 35, 60]))
    try:
        print("Must fail")
        print(find_less_than_50([78, 65, 100, 50, 75, 60]))
    except Exception as e:
        print(f"exeption raised at : {e}")
    try:
        print("Must fail")
        print(find_less_than_50([]))
    except Exception as e:
        print(f"exeption raised at : {e}")
    print("-2-")
    print("Must be 4")
    print(find_index_of_less_than_50([78, 65, 100, 50, 35, 60]))
    print("Must be -1")
    print(find_index_of_less_than_50([78, 65, 100, 50, 75, 60]))
    print("Must be -1")
    print(find_index_of_less_than_50([]))
    print("-3-")
    print("Must be true")
    print(find_if_less_than_50([78, 65, 100, 50, 35, 60]))
    print("Must be false")
    print(find_if_less_than_50([78, 65, 100, 50, 75, 60]))
    print("Must be false")
    print(find_if_less_than_50([]))
    print("-4-")
    print("Must be 35")
    print(find_min([78, 65, 100, 50, 35, 60]))
    try:
        print("Must fail")
        print(find_min([]))
    except Exception as e:
        print(f"exeption raised at : {e}")
    print("-5-")
    print("Must be 4")
    print(find_index_of_min([78, 65, 100, 50, 35, 60]))
    print("Must be 3")
    print(find_index_of_min([78, 65, 100, 50, 75, 60]))
    print("Must be -1")
    print(find_index_of_min([]))


if __name__ == '__main__':
    main()
