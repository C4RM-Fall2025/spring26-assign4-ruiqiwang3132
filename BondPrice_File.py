

def getBondPrice(y, face, couponRate, m, ppy=1):
    c = face * couponRate / ppy
    r = y / ppy
    n = m * ppy

    bondPrice = 0.0

    for t in range(1, n + 1):
        bondPrice += c / ((1 + r) ** t)

    bondPrice += face / ((1 + r) ** n)

    return round(bondPrice, 2)
