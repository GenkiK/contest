"""
・クラスカル法
    -> 辺のコストを小さい順にみていき，閉路ができなければ追加する
・各頂点はUnion-Find木で管理(同じ連結成分かどうかの判定)
"""
from dataclasses import dataclass
from functools import cmp_to_key
import sys, os

sys.path.append(os.path.join(os.path.dirname(__file__), "..", "..", "util"))
from util.UnionFind import UnionFind


@dataclass
class Edge:
    u: int
    v: int
    cost: int


def comp(e1: Edge, e2: Edge):
    """
    equals to:

    if e1.cost < e2.cost: return 1
    elif e1.cost == e2.cost: return 0
    else: return -1
    """
    return e1.cost - e2.cost


es: list[Edge] = []
V, E = map(int, input().rstrip().split())


def kruscal():
    es.sort(key=cmp_to_key(comp))  # edge.costが小さい順にソートする
    tree = UnionFind(V)
    res = 0
    for i in range(V):
        e = es[i] # 最小コストの辺
        if not tree.is_same(e.u, e.v):
            tree.unite(e.u, e.v)
            res += e.cost
    return res


