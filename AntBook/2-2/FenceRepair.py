from sys import stdin

input = stdin.readline

n = int(input().rstrip())
L = list(map(int, input().rstrip()))

"""
最も短い板とその次に短い板を組み合わせて新たな板とする。これをN-1回繰り返す。
ハフマン符号と似ている
"""

total = 0

# 配列の要素を削除するとことなく、使用する配列の範囲を狭めていく
while n > 1:
    mii1 = 0
    mii2 = 1
    # 常にL[mii1] <= L[mii2]の状態を保つため
    if L[mii1] > L[mii2]:
        tmp = L[mii1]
        L[mii1] = L[mii2]
        L[mii2] = tmp

    for i in range(2, n):
        if L[i] < L[mii1]:
            mii2 = mii1
            mii1 = i
        elif L[i] < L[mii2]:
            mii2 = i

    # 併合
    t = L[mii1] + L[mii2]
    total += t

    if mii1 == n - 1:
        tmp = L[mii1]
        L[mii1] = L[mii2]
        L[mii2] = tmp
    L[mii1] = t
    L[mii2] = L[n - 1]
    n -= 1
print(total)
