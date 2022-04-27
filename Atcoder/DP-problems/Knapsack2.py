from __future__ import annotations

N, W = map(int, input().rstrip().split())

w_lst: list[int] = []
v_lst: list[int] = []

for i in range(N):
    w, v = map(int, input().split())
    w_lst.append(w)
    v_lst.append(v)

"""
dp[i][j] := i番目までの荷物を取捨選択したとき，価値が j になるうちで最小の重み

dp[i][j] = min(dp[i-1][j - v_lst[i]] + w_lst[i], dp[i-1][j])
"""
INF = 10 ** 9 * W
sum_v = sum(v_lst) + 1
dp = [[INF] * sum_v for _ in range(N + 1)]
dp[0][0] = 0

for i in range(1, N + 1):
    for j in range(sum_v):
        if j >= v_lst[i - 1]:
            dp[i][j] = min(dp[i - 1][j - v_lst[i - 1]] + w_lst[i - 1], dp[i - 1][j])
        else:
            dp[i][j] = dp[i - 1][j]

for j in reversed(range(sum_v)):
    if dp[N][j] <= W:
        print(j)
        break
