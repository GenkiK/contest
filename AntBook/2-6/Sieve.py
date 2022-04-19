MAX_N = int(input())

prime: list[int] = []  # prime[i]がi番目の素数
is_prime: list[bool] = [True] * (MAX_N + 1)  # if is_prime[i] == True then i is prime


def sieve(n: int) -> int:
    """n以下の素数の数を返す"""
    # is_primeの初期化
    is_prime[0] = is_prime[1] = False

    for i in range(2, n + 1):
        if is_prime[i]:
            prime.append(i)
            j = 2 * i
            while j <= n:
                is_prime[j] = False
                j += i
    return len(prime)


if __name__ == "__main__":
    print(f"{MAX_N}以下の素数の数: {sieve(MAX_N)}")
    print(f"素数のリスト: {prime}")
