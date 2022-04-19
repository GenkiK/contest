from sys import stdin

readline = stdin.readline

N, W = map(int, readline().rstrip().split())
A = []
B = []
for i in range(N):
    a, b = map(int, readline().rstrip().split())
    A.append(a)
    B.append(b)

# メモ
dp = [[-1] * (W + 1) for _ in range(N + 1)]

# i番目以降のチーズから重さの総和がｊ以下となるように選ぶ
def rec(i, j):
    if dp[i][j] >= 0:
        return dp[i][j]
    res = 0
    if i == N:
        # チーズは残っていない
        res = 0
    else:
        # 0, 1, 2, 3, ...
        for b in range(B[i] + 1):
            if j >= b:
                res_tmp = rec(i + 1, j - b) + A[i] * b
                if res_tmp > res:
                    res = res_tmp
    dp[i][j] = res
    return res


print(rec(0, W))
