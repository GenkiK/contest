from sys import stdin

input = stdin.readline
n = int(input())

G: list[list[int]] = []  # 本来は入力されたものを隣接リストとしてこれに格納する
color: list[int] = [0] * n  # 1 or -1 で塗る


def dfs(v: int, c: int) -> bool:
    color[v] = c
    for i in range(len(G[v])):
        # 隣接している頂点が同じ色ならFalse
        if color[G[v][i]] == c:
            return False
        # 隣接している頂点がまだ塗られていないなら色を反転させて塗る
        elif color[G[v][i]] == 0 and not dfs(G[v][i], -c):
            return False
    return True


# １回の探索で，１かたまりの隣接グラフはすべて探索が終わる．
# ほかの孤立したグラフがあればそれを見ていく感じ
def main():
    for i in range(n):
        if color[i] == 0:
            # まだ頂点iが塗られていなければ1で塗る
            if not dfs(i, 1):
                print("No")
                return
    print("Yes")
