"""
・クラスカル法で解く(クラスカル法であれば，森の最小全域木を求められる)
"""


from dataclasses import dataclass
from functools import cmp_to_key


class UnionFind:
    """
    - 各要素は番号で管理
    - x == self.par[x]ならば,xは根
    - 男: 0 ~ N-1, 女: N ~ N + M -1
    """

    def __init__(self, n: int):
        self.par = [i for i in range(n)]
        self.rank = [0] * n

    def find(self, x: int) -> int:
        """
        根を見つける

        Args:
            x (int): 要素は番号

        Returns:
            int: 根の番号
        """
        if x == self.par[x]:
            return x
        self.par[x] = self.find(self.par[x])  # 縮約
        return self.par[x]

    def unite(self, x: int, y: int) -> None:
        """
        森を結合

        Args:
            x (int): 森1
            y (int): 森2
        """
        x = self.find(x)
        y = self.find(y)
        if x == y:
            return
        if self.rank[x] < self.rank[y]:
            # 高さが小さいほうを下にする
            self.par[x] = y
        else:
            self.par[y] = x
            if self.rank[x] == self.rank[y]:
                self.rank[x] += 1

    def is_same(self, x: int, y: int) -> bool:
        """同じ木に属するかを判定

        Args:
            x (int): 木
            y (int): 木

        Returns:
            bool: 判定結果
        """
        return self.find(x) == self.find(y)


@dataclass()
class Edge:
    from_: int
    to: int
    cost: int


def comp(e1: Edge, e2: Edge) -> int:
    return e1.cost - e2.cost


N, M, R = map(int, input().rstrip().split())

es: list[Edge] = []
for i in range(R):
    x, y, d = map(int, input().rstrip().split())
    es.append(Edge(from_=x, to=N + y, cost=-d))


def kruskal() -> int:
    total_d = 0
    tree: UnionFind = UnionFind(n=N + M)
    es.sort(key=cmp_to_key(comp))
    for i in range(R):
        e: Edge = es[i]
        if not tree.is_same(e.from_, e.to):
            total_d += e.cost
            tree.unite(e.from_, e.to)
    return total_d


print(10000 * (N + M) + kruskal())


# from dataclasses import dataclass
# from heapq import heappop, heappush

# N, M, R = map(int, input().rstrip().split())

# """
# ・プリム法により最小全域木を作成
# ・ノード間の距離を，(10000 - d)とする
# """


# @dataclass()
# class Edge:
#     to: int
#     cost: int


# # men: G[0 ~ N-1], women: G[N ~ N+M-1]
# G: list[list[Edge]] = [[] for _ in range(N + M)]

# # 追加するedgeの先がすでに追加されているかどうか確認するための配列
# used: list[bool] = [False] * (N + M)

# for _ in range(R):
#     x, y, d = map(int, input().rstrip().split())
#     y += N
#     G[x].append(Edge(to=y, cost=10000 - d))
#     G[y].append(Edge(to=x, cost=10000 - d))

# # 頂点の(集合Xからの距離, number)のリストをヒープ化
# heap: list[tuple[int, int]] = []

# ans = 0

# for i in range(N + M):
#     if not used[i]:
#         heappush(heap, (10000, i))
#         used[0] = True
#         while len(heap) > 0:
#             d, v = heappop(heap)
#             if used[v]:
#                 continue
#             used[v] = True
#             ans += d
#             for j in range(len(G[v])):
#                 e: Edge = G[v][j]
#                 if not used[e.to]:
#                     heappush(heap, (e.cost, e.to))
# print(ans)
