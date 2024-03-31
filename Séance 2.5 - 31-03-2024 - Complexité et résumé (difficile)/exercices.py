# ex 1 opti
def tri_poly(poly: list[list[int]]) -> list[list[int]]:
    return sorted(poly, key=lambda x: (len(x), x[-1]), reverse=True)


# ex 1
def tri_critere(polynome1: list[int], polynome2: list[int]) -> bool:
    if len(polynome1) < len(polynome2):
        return True
    elif len(polynome1) > len(polynome2):
        return False
    else:
        if polynome1[-1] > polynome2[-1]:
            return False
        else:
            return True


# ex 2
def tri_poly_insert(poly: list[list[int]]) -> list[list[int]]:
    if len(poly) == 0:
        return poly
    _poly = [poly.pop()]
    while len(poly) > 0:
        polynome = poly.pop()
        for x in range(len(_poly)):
            if tri_critere(polynome, _poly[x]):
                _poly.insert(x, polynome)
                break
            if x == len(_poly) - 1:
                _poly.append(polynome)
    return _poly


# ex 3
def alpha(cible: float) -> float:
    def fonction(a: float) -> float:
        return sum(1 / n ** a for n in range(2, 1001))

    bi: float = 1
    bs: float = 100
    m: float = (bi + bs) / 2
    result: float = 0
    count: int = 0
    while abs(result - cible) > 1e-3:  # 1*10**-3
        count += 1
        m = (bi + bs) / 2
        result = fonction(m)
        if result > cible:
            bi = m
        else:
            bs = m
    # print(f"nombre d'itération : {count}")
    return m


def main():
    print(alpha(5))


if __name__ == "__main__":
    main()
