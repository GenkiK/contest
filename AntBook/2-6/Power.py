# def power(x: int, n: int) -> int:
#     if n == 0:
#         return 0
#     elif n % 2 == 0:
#         return power(x ** 2, n // 2)
#     else:
#         return x * power(x ** 2, (n - 1) // 2)


def power(x: int, n: int) -> int:
    res = 1
    while n != 0:
        if n % 2 == 0:
            x **= 2
            n //= 2
        else:
            res *= x
            x **= 2
            n = (n - 1) // 2
    return res * x ** n


if __name__ == "__main__":
    print(power(5, 5))
