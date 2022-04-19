from sys import stdin

readline = stdin.readline



N = int(readline().rstrip())
# N + 1個の要素。1オリジンで各生徒にアクセスできる
C1 = [0]
C2 = [0]
for i in range(N):
    c, p = map(int, readline().rstrip().split())
    if c == 1:
        C1.append(C1[i] + p)
        C2.append(C2[i])
    else:
        C2.append(C2[i] + p)
        C1.append(C1[i])

Q = int(readline().rstrip())

# LR = [list(map(int, readline().rstrip().split())) for _ in range(Q)]
for _ in range(Q):
    cls1 = 0
    cls2 = 0
    l, r = map(int, readline().rstrip().split())
    print(C1[r] - C1[l - 1], C2[r] - C2[l - 1])
