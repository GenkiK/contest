from sys import stdin

input = stdin.readline
N = int(input().rstrip())
dct = {}
for _ in range(N):
    s = input().rstrip()
    if dct.get(s):
        dct[s] += 1
    else:
        dct[s] = 1

print(max(dct, key=dct.get))
