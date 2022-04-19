from sys import stdin

input = stdin.readline
n = int(input().rstrip())
m = int(input().rstrip())
M = int(input().rstrip())

"""
dp[i][j]: 整数 j のi分割の総数
dp[i][j] = dp[i][j-i] + dp[i-1][j]
dp[i][j-i] := j を i 個に分割するパターン数
dp[i-1][j] := j を i-1 個以下に分割するパターン数

1 <= j <= n, 1 <= i <= m
"""

dp: list[list[int]] = [[0] * (n + 1) for _ in range(m + 1)]

dp[0][0] = 1
for i in range(1, m + 1):
    for j in range(0, n + 1):
        if j - i >= 0:
            dp[i][j] = (dp[i][j - i] + dp[i - 1][j]) % M
        else:
            dp[i][j] = dp[i - 1][j]
print(dp[m][n])
