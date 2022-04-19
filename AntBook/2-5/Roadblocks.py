from dataclasses import dataclass
from heapq import heapify, heappop, heappush
from sys import stdin

input = stdin.readline
"""
Sample Input

4 4
1 2 100
2 4 200
2 3 250
3 4 100
"""
INF = 10 ** 8
N, R = map(int, input().rstrip().split())


@dataclass
class Edge:
    to: int
    cost: int


dist: list[int] = [INF] * N
dist2: list[int] = [INF] * N

# 隣接リスト
G: list[list[Edge]] = [[] for _ in range(N)]  # G[v]は頂点vに隣接する辺のリストを返す


def dijkstra():
    # 初期化
    dist[0] = 0
    # (distance, vertex_number)のリスト
    heap: list[tuple[int, int]] = []
    heapify(heap)
    heappush(heap, (0, 0))
    for _ in range(R):
        from_, to, cost = map(int, input().strip().split())
        G[from_].append(Edge(to, cost))
        G[to].append(Edge(from_, cost))

    while len(heap) != 0:
        d, v = heappop(heap)
        if dist2[v] < d:
            continue
        for i in range(len(G[v])):
            e: Edge = G[v][i]
            d_new: int = d + e.cost
            if dist[e.to] > d_new:
                dist[e.to] = d_new
                heappush(heap, (dist[e.to], e.to))
            if dist2[e.to] > d_new and dist[e.to] < d_new:
                dist2[e.to] = d_new
                heappush(heap, (dist2[e.to], e.to))
    print(f"{dist2[N-1]}")
