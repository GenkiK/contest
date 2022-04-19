from sys import stdin

input = stdin.readline
n = int(input().rstrip())
a_lst = list(map(int, input().rstrip().split()))

"""
dp[i] ;= 最後がa_iであるような最長の増加部分列の長さ
       = a_iのみからなる文字列 or j<iのときa_j < a_iであるようなa_jで終わる増加部分列にa_iを付け足した部分列
dp[i] = max(1, {dp[j]+1| j<i and a[j]<a[i]})
"""

dp: list[int] = [0] * n
dp[0] = 1

for i in range(1, n):
    tmp_max = 0
    for j in range(0, i):
        if a_lst[j] < a_lst[i] and tmp_max < dp[j] + 1:
            tmp_max = dp[j] + 1
    dp[i] = max(tmp_max, 1)
print(max(dp))
