from __future__ import annotations
from sys import stdin
from queue import Queue as Q

readline = stdin.readline
INF = float("inf")

H, W = map(int, readline().rstrip().split())

field: list[list[str]] = []
dist: list[list[int | float]] = []
for _ in range(H):
    field.append(list(readline().rstrip().split()))
    dist.append([float("inf")] * W)

q: Q[list[int]] = Q()


def bfs():
    while not q.empty():
        x, y = q.get()
        # 今いる地点がゴールの時、探索をやめる（探索を辞めずにキューが空になるまで続けていると、各点までの最短距離が求められる)
        if field[x][y] == "G":
            print(dist[x][y])
            return
        npos_lst = [[x + 1, y], [x, y + 1], [x - 1, y], [x, y - 1]]
        for npos in npos_lst:
            nx, ny = npos
            if (
                0 <= nx < H
                and 0 <= ny < W
                and field[nx][ny] != "#"
                and dist[nx][ny] == float("inf")
            ):
                dist[nx][ny] = dist[x][y] + 1
                q.put([nx, ny])


def main():
    for x in range(H):
        for y in range(W):
            if field[x][y] == "S":
                q.put([x, y])
                bfs()
                return
