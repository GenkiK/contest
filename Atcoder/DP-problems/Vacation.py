N = int(input())

"""
dp[i][act_i]: 時点iまでに得た幸福度の総和．時点iに来るときにとった行動はact_i
"""

dp = [[0] * 3 for _ in range(N + 1)]

for i in range(1, N + 1):
    rewards = list(map(int, input().rstrip().split()))
    for act in range(3):
        if act != 1:
            dp[i][act] = max(
                dp[i - 1][abs(2 - act)] + rewards[abs(2 - act)],
                dp[i - 1][abs(1 - act)] + rewards[abs(1 - act)],
            )
        else:
            dp[i][act] = max(dp[i - 1][2] + rewards[2], dp[i - 1][0] + rewards[0])
print(max(dp[N]))
