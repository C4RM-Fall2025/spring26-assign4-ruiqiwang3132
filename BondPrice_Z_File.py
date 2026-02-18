

def getBondPrice_Z(face, couponRate, times, yc):
    coupon = face * couponRate
    cashflows = [coupon] * (len(times) - 1) + [coupon + face]
    bondPrice = sum(cf / ((1 + y) ** t) for cf, y, t in zip(cashflows, yc, times))
    return round(bondPrice, 2)
