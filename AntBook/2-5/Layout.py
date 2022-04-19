"""
牛iの座標をd[i]とすると，
d[i] <= d[i+1]
d[BL] - d[AL] <= DL
d[BD] - d[AD] >= DD

まとめると，
d[i + 1] + 0 >= d[i]
d[AL] + DL >= d[BL]
d[BD] - DD >= d[AD]

d[from] + w >= d[to]の構成
"""
INF = 10 ** 10
N, ML, MD = map(int, input().rstrip().split())

AL: list[int] = []
BL: list[int] = []
DL: list[int] = []
AD: list[int] = []
BD: list[int] = []
DD: list[int] = []

for _ in range(ML):
    al, bl, dl = map(int, input().rstrip().split())
    AL.append(al - 1)
    BL.append(bl - 1)
    DL.append(dl)

for _ in range(MD):
    ad, bd, dd = map(int, input().rstrip().split())
    AD.append(ad - 1)
    BD.append(bd - 1)
    DD.append(dd)


def solve():
    d = [INF] * N
    d[0] = 0
    # ベルマンフォードによりdを計算する
    for _ in range(N):
        # i+1からiへコスト0
        for i in range(N - 1):
            if d[i + 1] < INF:
                d[i] = min(d[i], d[i + 1])

        # AL->BLへコストDL
        for i in range(ML):
            if d[AL[i]] < INF:
                d[BL[i]] = min(d[BL[i]], d[AL[i]] + DL[i])

        # BD->ADへコストDD
        for i in range(MD):
            if d[BD[i]] < INF:
                d[AD[i]] = min(d[AD[i]], d[BD[i]] - DD[i])

    res = d[N - 1]
    if d[0] < 0:
        # 負の閉路が存在=解なし
        res = -1
    elif res == INF:
        res = -2
    print(res)


# @dataclass
# class Edge:
#     from_: int
#     to: int
#     cost: int


# es: list[Edge] = [Edge(i, i + 1, 0) for i in range(1, N)]
# for _ in range(ML):
#     AL, BL, DL = map(int, input().rstrip().split())
#     es.append(Edge(AL, BL, DL))
# for _ in range(MD):
#     AD, BD, DD = map(int, input().rstrip().split())
#     es.append(Edge(BD, AD, -DD))

# d: list[int] = [INF]


# def bellman_ford(s: int, g: int):
#     d[s] = 0
#     update = True
#     while update:
#         update = False
#         for i in range(len(es)):
#             e: Edge = es[i]
#             if d[e.from_] + e.cost < d[e.to]:
#                 d[e.to] = d[e.from_] + e.cost
#                 update = True
#     print(d[g])
