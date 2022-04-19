from sys import stdin

input = stdin.readline

N = int(input().rstrip())
ws: list[int] = []
vs: list[int] = []
for _ in range(N):
    w_v = list(map(int, input().rstrip().split()))
    ws.append(w_v[0])
    vs.append(w_v[1])

W = int(input().rstrip())

"""
dp[iまでの荷物][重さjを超えない] = 最大の価値

i = 0 to N-1, j = 0 to W

k = 0 to (j // ws[i])
dp[i+1][j] = max_k_(dp[i][j-ws[i]*k] + vs[i]*k)
"""
dp: list[list[int]] = [[0] * (W + 1) for _ in range(N + 1)]

for i in range(N):
    max_val = 0
    for j in range(W + 1):
        for k in range(0, j // ws[i]):
            tmp_max = dp[i][j - ws[i] * k] + vs[i] * k
            max_val = tmp_max if tmp_max > max_val else max_val
        dp[i + 1][j] = max_val

print(dp[N][W])
