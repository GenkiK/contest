from sys import stdin
from queue import Queue

readline = stdin.readline


N = int(readline().rstrip())

# 位置がそのノードの番号を表す
G = [[] for _ in range(N + 1)]  # 1-origin として使いたいので、要素の1つ目は使わない
for _ in range(N - 1):
    a, b = map(int, readline().rstrip().split())
    G[a].append(b)
    G[b].append(a)


def getdist(start: int, dist):
    # BFSで最短距離を計算
    q = Queue()
    q.put(start)
    dist[start] = 0

    while not q.empty():
        pos: int = q.get()
        for to in G[pos]:
            if dist[to] == float("inf"):  # 未探索の場合
                dist[to] = dist[pos] + 1
                q.put(to)


def main():
    dist = [float("inf") if i != 0 else 0 for i in range(N + 1)]
    getdist(1, dist)
    max_dist = -1
    max_dist_idx = -1
    for i in range(N+1):
        if max_dist < dist[i]:
            max_dist = dist[i]
            max_dist_idx = i

    dist = [float("inf") if i != 0 else 0 for i in range(N + 1)]
    getdist(max_dist_idx, dist)
    max_dist = max(dist)
    print(max_dist + 1)


main()
