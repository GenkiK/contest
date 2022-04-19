from dataclasses import dataclass


@dataclass
class Edge:
    from_: int
    to: int
    cost: int


V = 100  # no. of vertexes
E = 100  # no. of edges
INF = 10000000
es: list[Edge] = []  # full of Edges
d = [INF] * V


def shortest_path(s: int):
    """
    1. すべての辺に注目し，その辺を通った先の頂点のコストを小さくできればパスを更新
    2. 1.のプロセスを高々 |V|-1 回行う
        (1.のプロセスで少なくとも１つの頂点への最短距離は求まるので，ループ回数は高々|V|-1回（始点はすでに最短距離が求まっているので-1))

    1回目のループでは，(始点から移動できる頂点)の最短路が求められる
    2回目のループでは，(1回目で決まったルートから移動できる頂点)の最短路が求められる
    ...
    →じわじわと到達範囲を広げていくイメージ

    Args:
        s (int): start vertex
    """
    # initialize
    d[s] = 0
    while True:
        update = False
        for i in range(E):
            e: Edge = es[i]
            if d[e.from_] != INF and d[e.to] > d[e.from_] + e.cost:
                d[e.to] = d[e.from_] + e.cost
                update = True
        if not update:
            break
