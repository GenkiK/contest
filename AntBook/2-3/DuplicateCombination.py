from sys import stdin

input = stdin.readline
n = int(input().rstrip())
m = int(input().rstrip())
a_lst = list(map(int, input().rstrip().split()))
M = int(input().rstrip())

"""
0 <= i <= n-1, 0 <= j <= m
dp[i+1][j] := i 番目までの品物から j 個選ぶ選び方
dp := (n+1) x (m+1)

dp[i+1][j] = sum(dp[i][j-k]), k = 0 to min(a_lst[i], j)
dp[i+1][j] = dp[i+1][j-1] + dp[i][j] - dp[i][j-1-a_lst[i]]
a_lst[i]は品物(i+1)の上限個数
"""

dp: list[list[int]] = [[0] * (m + 1) for _ in range(n + 1)]

# １つも選ばない方法は常に１通り
for i in range(0, n + 1):
    dp[i][0] = 1

for i in range(0, n):
    for j in range(1, m + 1):
        if j - 1 - a_lst[i] >= 0:
            dp[i + 1][j] = (dp[i + 1][j - 1] + dp[i][j] - dp[i][j - 1 - a_lst[i]]) % M
        else:
            dp[i + 1][j] = (dp[i + 1][j - 1] + dp[i][j]) % M
print(dp[n][m])
