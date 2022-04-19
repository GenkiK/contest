x1 = 1
y1 = 11
x2 = 5
y2 = 3


def gcd(a: int, b: int) -> int:
    if b == 0:
        return a
    return gcd(b, a % b)
