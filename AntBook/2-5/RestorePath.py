from sys import stdin

input = stdin.readline

INF = 10 ** 8
V, E = map(int, input().rstrip().split())
cost = [[INF] * V for _ in range(V)]  # cost[u][v] は辺e=(u, v)のコスト(存在しない場所はINF)

# costの構成
for _ in range(E):
    s, t, c = map(int, input().split())
    cost[s][t] = c
    cost[t][s] = c

d = [INF for _ in range(V)]  # 最短距離
used = [False] * V
prev = [-1] * V


def dijkstra(s: int) -> None:
    d[s] = 0
    while True:
        v = -1
        # まだ使われていない頂点のうち，sとの距離が最小のものを探す(minヒープでやるともっと効率がいい)
        for u in range(V):
            if not used[u] and (v == -1 or d[u] < d[v]):
                v = u
        if v == -1:
            break
        used[v] = True
        for u in range(V):
            if d[u] > d[v] + cost[v][u]:
                d[u] = d[v] + cost[v][u]
                prev[u] = v


def get_shortest_path(t: int) -> list[int]:
    path: list[int] = []
    while t != -1:
        path.append(t)  # t が s になるまでprev[t]をたどっていく
        t = prev[t]
    # このままだとt->sの逆順になっているので順序を反転
    path.reverse()
    return path
