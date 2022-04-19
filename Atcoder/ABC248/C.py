from sys import stdin

input = stdin.readline

N, M, K = map(int, input().rstrip().split())


dp = [[0] * K for _ in range(N)]

# initialize
for k in range(K):
    if k >= K - M - 1:
        dp[0][k] = 1

for i in range(1, N):
    for k in range(K):
        total = 0
        for j in range(min(K - k - 1, M)):
            total += dp[i - 1][k + j + 1]
        dp[i][k] = total
print(sum(dp[N - 1][:]) % 998244353)

# dp = [[[0] * K] * M] * N

# # initialize dp
# for j in range(M):
#     for k in range(K):
#         if j > k:
#             dp[0][j][k] = 0
#         else:
#             dp[0][j][k] = 1

# for i in range(N):
#     for l in range()
#     dp[] =
