from sys import stdin

readline = stdin.readline


limits = list(map(int, readline().rstrip().split()))
coins = [1, 5, 10, 50, 100, 500]
A = int(readline().rstrip())


# def max_num(coin: int, A: int, limit: int):
#     for num in range(limit, -1, -1):
#         if coin * num <= A:
#             A -= coin * num
#             return num, A
# total_num = 0
# for coin, limit in zip(reversed(coins), reversed(limits)):
#     num, A = max_num(coin, A, limit)
#     total_num += num


total_num = 0
for coin, limit in zip(reversed(coins), reversed(limits)):
    tmp_num = A // coin
    num = tmp_num if tmp_num <= limit else limit
    A -= num * coin
    total_num += num
print(total_num)
