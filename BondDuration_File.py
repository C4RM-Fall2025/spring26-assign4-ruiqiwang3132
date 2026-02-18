
def getBondDuration(y, face, couponRate, m, ppy=1):
    c = face * couponRate / ppy
    r = y / ppy
    n = m * ppy

    price = 0.0
    weighted_sum = 0.0

    for t in range(1, n + 1):
        pv = c / ((1 + r) ** t)
        price += pv
        weighted_sum += t * pv

    pv_face = face / ((1 + r) ** n)
    price += pv_face
    weighted_sum += n * pv_face

    duration = weighted_sum / price
    return round(duration / ppy, 2)

