from math import floor

a, b = map(int, input().rstrip().split())

# [a, b)の整数たちがprimeかどうか
is_prime: list[bool] = [True] * (b - a + 1)  # 1-origin として扱うために +1 しておく
is_prime[0] = False  # 1-originなので最初の要素は使わない

# [0, √b]の整数たちがprimeかどうか
is_prime_small: list[bool] = [True] * (floor(b ** 0.5) + 1)  # 1-origin として扱うために+1しておく


def segment_sieve(a: int, b: int):
    """
    [a, b)の整数 i に対して篩を行う．is_prime[i - a] == True <=> iが素数
    """
    i = 2
    while i ** 2 < b:
        if is_prime_small[i]:
            j = 2 * i
            while j ** 2 < b:
                is_prime_small[j] = False
                j += i
            j = a + (-a) % i  # a以上の整数の中で，最小の i の倍数
            while j < b:
                is_prime[j - a] = False
                j += i
        i += 1
    print(sum(is_prime))


if __name__ == "__main__":
    segment_sieve(a, b)
