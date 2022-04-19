from sys import stdin
import heapq

input = stdin.readline

N = int(input())
L: list[int] = list(map(int, input().rstrip().split()))
heapq.heapify(L)

# minヒープで最小とその次に小さい値を効率よく取り出す
# 取り出した値を合計してからヒープに戻す

cost = 0
while L:
    min_v = heapq.heappop(L)
    if not L:
        print(cost)
        break
    else:
        min_v += heapq.heappop(L)
        cost += min_v
        heapq.heappush(L, min_v)
