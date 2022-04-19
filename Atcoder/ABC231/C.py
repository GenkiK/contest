from sys import stdin
from bisect import bisect_left

input = stdin.readline
N, Q = map(int, input().rstrip().split())
A_lst = sorted(list(map(int, input().rstrip().split())))

# 二分探索
for _ in range(Q):
    x = int(input().rstrip())
    idx = bisect_left(A_lst, x)
    print(N - idx)
