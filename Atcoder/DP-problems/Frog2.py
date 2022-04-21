N, K = map(int, input().rstrip().split())
h = list(map(int, input().rstrip().split()))

"""
問題定義:
カエルはKこ先までの段差までならどこでもジャンプできる

dp[i]: i にたどり着くまでに支払ったコスト

再帰的に解くパターン
dp[i] = min_j (dp[j] + abs(h[j] - h[i]))
今 i にいて，j にジャンプするとき，最適な j を選ぶ

dp[j] = min_i (dp[i] + abs(h[i] - h[j]))
j は行き先．どのiからジャンプしてjにたどり着けばいいか
"""

dp = [0] * N

for j in range(1, N):
    min_i = j - 1
    for i in range(j - 2, j - K - 1, -1):
        if i < 0:
            break
        if dp[i] + abs(h[i] - h[j]) < dp[min_i] + abs(h[min_i] - h[j]):
            min_i = i
    dp[j] = dp[min_i] + abs(h[min_i] - h[j])
print(dp[N - 1])
