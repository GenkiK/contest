# 素数判定
def is_prime(n: int) -> bool:
    i = 2
    while i ** 2 <= n:
        if n % i == 0:
            return False
    # 1 は例外
    return n != 1


# 約数の列挙
def divisor(n: int) -> list[int]:
    res: list[int] = []
    i = 1
    while i ** 2 <= n:
        if n % i == 0:
            res.append(i)
            if i ** 2 != n:
                res.append(n // i)
    return res


# 素因数分解
def prime_factor(n: int) -> list[int]:
    res: list[int] = []
    i = 2
    while i ** 2 <= n:
        while n % i == 0:
            res.append(i)
            n //= i
    if n != 1:
        # n = (√nより小さい素数)x(√nより大きい素数)のとき
        res.append(n)
    return res


# 素因数分解(辞書型を返す)
def prime_factor_as_dict(n: int) -> dict[int, int]:
    res: dict[int, int] = {}
    i = 2
    while i ** 2 <= n:
        cnt = 0
        while n % i == 0:
            cnt += 1
            n //= i
        if cnt:
            res[i] = cnt
    if n != 1:
        res[n] = 1
    return res
