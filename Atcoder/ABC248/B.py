from sys import stdin

input = stdin.readline

A, B, K = map(int, input().rstrip().split())

cnt = 0
while A < B:
    A *= K
    cnt += 1
print(cnt)
