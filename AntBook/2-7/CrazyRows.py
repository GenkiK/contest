n = int(input())
m = [list(map(int, input().split())) for _ in range(n)]

res = 0
a: list[int] = [-1] * n
for i in range(n):
    for j in reversed(range(n)):
        if m[i][j] == 1:
            # i行目の右端の1の位置を格納
            a[i] = j
            break

for i in range(n):
    pos = -1
    for j in range(i, n):
        if a[j] <= i:
            pos = j
            break

    for j in range(pos, i, -1):
        a[j], a[j - 1] = a[j - 1], a[j]
        res += 1
print(res)
