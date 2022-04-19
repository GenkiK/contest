from sys import stdin

input = stdin.readline
INF = 10 ** 8
V = int(input().rstrip())  # 頂点数

cost: list[list[int]] = [[INF] * V for _ in range(V)]  # cost[u][v] := 辺e=(u, v)のコスト
mincost: list[int] = [INF] * V  # 集合Xから頂点vにつながる辺の最小コスト := mincost[v]
used: list[bool] = [False] * V  # used[v] := 頂点vを使用したか


def prim():
    """input
    V
    u_1 v_1 c_1
    u_2 v_2 c_2
    ...
    """
    # 初期化
    for _ in range(V):
        u, v, c = map(int, input().rstrip().split())
        cost[u][v] = c
        cost[v][u] = c

    mincost[0] = 0
    res = 0
    while True:
        v = -1
        # Xに属さない頂点のうちXからの辺のコストが最小になる頂点を探す
        # usedを使わない & mincostをminヒープとすることで書き換え可能
        for u in range(V):
            if not used[u] and (v == -1 or mincost[u] < mincost[v]):
                v = u
        # 更新するものがない
        if v == -1:
            break

        used[v] = True
        res += mincost[v]

        for u in range(V):
            mincost[u] = min(mincost[u], cost[v][u])
    return res
