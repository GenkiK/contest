from sys import stdin

input = stdin.readline

N = int(input().rstrip())
R = int(input().rstrip())
X = sorted(list(map(int, input().rstrip().split())))

"""
方針：左端を範囲に含むできる限り右側の点を塗る
"""

cnt = 0
i = 0
while i < N:
    # 左端の点
    s = X[i]
    i += 1
    while i < N and X[i] <= s + R:
        i += 1
    # 塗る点
    p = X[i - 1]
    # pから右にRの範囲にギリギリ入らない次の左端の点
    while i < N and X[i] <= p + R:
        i += 1
    cnt += 1

print(cnt)
