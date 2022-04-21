N = int(input())
h = list(map(int, input().rstrip().split()))

dp = [0] * N
dp[1] = abs(h[0] - h[1])
"""
dp[i] = min(dp[i-1] + |h[i-1] - h[i]|, dp[i-2] + |h[i-2] - h[i]|)
"""

for i in range(2, N):
    dp[i] = min(dp[i-1] + abs(h[i-1] - h[i]), dp[i-2] + abs(h[i-2] - h[i]))
print(dp[N-1])

