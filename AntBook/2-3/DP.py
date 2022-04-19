from sys import stdin

input = stdin.readline

N = int(input().rstrip())
w = list(map(int, input().rstrip().split()))
v = list(map(int, input().rstrip().split()))

W = int(input().rstrip())

"""
品物を 0~j まで使って、重さの総和が i 以下となるよう品物を選ぶ時、価値の総和の最大になるように選ぶ。

dp[重さがiを超えない][品物jまで] = 価値の最大値
dp[i+1][j+1] = max(dp[i][j], dp[i-w[j+1]][j+1] + v[j+1]) or dp[i][j] (品物 j を選ぶと重さ i を超えてしまう時)

"""
dp = [[0] * (N + 1) for _ in range(W + 1)]

for i in range(0, W):
    for j in range(0, N):
        if i < w[j + 1]:
            dp[i + 1][j + 1] = dp[i][j]
        else:
            dp[i + 1][j + 1] = max(dp[i][j], dp[i - w[j + 1]][j + 1] + v[j + 1])

print(dp[W][N])
