from sys import stdin

from bisect import bisect_left

input = stdin.readline
n = int(input().rstrip())
a = list(map(int, input().rstrip().split()))

"""
同じ長さの増加部分列ならば、末尾の要素ができるだけ小さいほうが有利になる

dp[i] := 長さがi+1であるような増加部分列における末尾の要素の最小値(存在しない場合はINF)
"""

INF = 100000000
dp: list[int] = [INF] * n

for i in range(n):
    dp[bisect_left(dp, a[i])] = a[i]
print(bisect_left(dp, INF))
