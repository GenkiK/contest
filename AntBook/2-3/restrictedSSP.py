from sys import stdin

input = stdin.readline

n = int(input().rstrip())
a = list(map(int, input().rstrip().split()))
m = list(map(int, input().rstrip().split()))
K = int(input().rstrip())

"""
dp[i までの数を使う][総和が j となる] = True/False

i = 0 to n-1, j = 0 to n-1, k = 0 to min(m[i], j // a[i])
dp[i+1][j] = dp[i][j] or dp[i][j - k*a[i]] -> これでは無駄が多い(booleanを求めるDPは無駄があることが多い)

dp[i+1][j] = i番目まででjを作る際に余るi番目の最大個数(作れない場合は-1)

dp[i+1][j] =
    * m[i] (dp[i][j] >=0 (i番目を使わなくていい))
    * -1 (j < a[i] or dp[i+1][j - a[i]] <= 0 (作れないとき))
    * dp[i+1][j - a[i]]-1 (それ以外 (i番目まででj-a[i]を作る際にi番目をK個残すことができるならば、i番目をk-1個残してjを作ることができる))
      * dp[i][j-k*a[i]]ではなく、既にiを使ったもので総和が j より小さいものにもう一つi番目の値を使うことで総和をjにしている
"""

dp: list[list[int]] = [[-1] * (K + 1) for _ in range(n + 1)]
dp[0][0] = 0

for i in range(0, n):
    for j in range(0, K + 1):
        if dp[i][j] >= 0:
            dp[i + 1][j] = m[i]
        elif j < a[i] or dp[i + 1][j - a[i]] <= 0:
            dp[i + 1][j] = -1
        else:
            dp[i + 1][j] = dp[i + 1][j - a[i]] - 1
if dp[n][K] >= 0:
    print("Yes")
else:
    print("No")
