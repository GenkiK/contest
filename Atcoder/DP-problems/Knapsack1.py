from __future__ import annotations

N, W = map(int, input().rstrip().split())

"""
dp[i][j] := i番目までの各荷物を取捨選択して鞄の中身の重さがj以下のときの価値

重さが j 「以下」っていうのがポイント

dp[i][j] = max(dp[i-1][j-w[i]] + v[i], dp[i-1][j])
"""
dp = [[0] * (W + 1) for _ in range(N + 1)]
w_lst: list[int] = list()
v_lst: list[int] = list()

for _ in range(N):
    w, v = map(int, input().rstrip().split())
    w_lst.append(w)
    v_lst.append(v)

for i in range(1, N + 1):
    for j in range(W + 1):
        if j - w_lst[i - 1] >= 0:
            dp[i][j] = max(dp[i - 1][j - w_lst[i - 1]] + v_lst[i - 1], dp[i - 1][j])
        else:
            dp[i][j] = dp[i - 1][j]
print(dp[N][W])
