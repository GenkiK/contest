import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), "..", "..", "util"))
print(list(map(os.path.normpath, sys.path)))

from sys import stdin
from util.UnionFind import UnionFind

input = stdin.readline

N = int(input())
K = int(input())

# x, x + N, x + 2 * N を x-A, x-B, x-Cの要素とする
tree = UnionFind(3 * N)

ans = 0
for _ in range(K):
    t, x, y = list(map(int, input().rstrip().split()))
    if x < 0 or x > N or y < 0 or y > N:
        ans += 1
        continue
    if t == 1:
        # 「xとyは同じ種類」という情報
        if tree.is_same(x, y + N) or tree.is_same(x, y + 2 * N):
            ans += 1
        else:
            tree.unite(x, y)
            tree.unite(x + N, y + N)
            tree.unite(x + 2 * N, y + 2 * N)
    else:
        # 「xはyを食べる」という情報
        if tree.is_same(x, y) or tree.is_same(x, y + 2 * N):
            ans += 1
        else:
            tree.unite(x, y + N)
            tree.unite(x + N, y + 2 * N)
            tree.unite(x + 2 * N, y)
print(ans)
