from sys import stdin

input = stdin.readline

a, b = map(int, input().rstrip().split())


def extgcd(a: int, b: int) -> tuple[int, int, int]:
    d = a
    if b != 0:
        d, y, x = extgcd(b, a % b)
        y -= (a // b) * x
    else:
        x = 1
        y = 0
    return d, x, y


d, x, y = extgcd(a, b)

if d == 1:
    L = [0] * 4
    if x > 0:
        L[0] += x
    else:
        L[2] -= x
    if y > 0:
        L[1] += y
    else:
        L[3] -= y
    print(*L)

else:
    print(-1)
