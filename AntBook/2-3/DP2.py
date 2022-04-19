from sys import stdin

input = stdin.readline
n: int = int(input().rstrip())
w: list[int] = list(map(int, input().rstrip().split()))
v: list[int] = list(map(int, input().rstrip().split()))
W: int = int(input().rstrip())

"""
dp[i+1 (i 番目までの品物)][j (価値の総和が j)] = 重さの総和の最小値

dp[i+1][j] = min(dp[i][j], dp[i][j - v[i]]+w[i])  i 番目の品物を選ばない or 選ぶ

答えは dp[n][j] <= W となる最大の j
"""
MAX_V = 100
MAX_N = 100
INF = 10000000000
dp: list[list[int]] = [[INF] * (MAX_N * MAX_V)]
dp[0][0] = 0


def solve():
    for i in range(n):
        for j in range(0, MAX_N * MAX_V + 1):
            if j < v[i]:
                dp[i + 1][j] = dp[i][j]
            else:
                dp[i + 1][j] = min(dp[i][j], dp[i][j - v[i]] + w[i])
    res = 0
    for j in range(0, MAX_N * MAX_V + 1):
        if dp[n][j] <= W:
            res = j
    print(res)
