from dataclasses import dataclass
from heapq import heapify, heappop, heappush

V = int(input())
INF = 10000000
d = [INF] * V  # スタート位置から各頂点までの距離


@dataclass
class Edge:
    to: int
    cost: int


"""
G:
[[e1, e2, e3, e4],  # v1の持つ辺
 [e3, e4],          # v2の持つ辺
 [e2, e5, e6]]      # v3の持つ辺

隣接リスト （C++では，`vector<edge> G[MAX_V]`）
"""
G: list[list[Edge]] = []


def dijkstra(s: int):
    """ダイクストラ法
    猪突猛進のイメージに近い．ゆえに負の重みがあるとスパイラルに陥る

    Args:
        s (int): start vertex
    """
    # 初期化
    ## (distance, vertex_number)のリストをヒープ化
    heap: list[tuple[int, int]] = []
    heapify(heap)
    d[s] = 0

    while not len(heap) == 0:
        dist, v = heappop(heap)
        if d[v] < dist:  # 最短距離が更新されていなかった過去の情報
            continue
        for i in range(len(G[v])):
            # ここでvに隣接した頂点(/辺)をループで取り出したいから，Edgeにfromという属性を持たせず，Gを二次元配列にしている
            e: Edge = G[v][i]
            if d[e.to] > d[v] + e.cost:
                d[e.to] = d[v] + e.cost
                heappush(heap, (d[e.to], e.to))
