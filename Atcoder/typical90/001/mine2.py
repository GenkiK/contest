from collections import deque

N, L = map(int, input().rstrip().split())
K = int(input())
A_lst = list(map(int, input().rstrip().split()))


def main():
    """
    まずN個の切れ目で切り分ける．そこから小さいものから順に(N-K)回くっつける動作を繰り返す．

    最終的には，len(diff_lst) == K + 1 になる．
    １回くっつけるたびに長さは1ずつ減っていく

    xx454yyyとなっているとき，どちらでまとめるべきか判断する必要がある（というより両方のパターンを探索する必要がある）
    値が最小となるindexを見つけて，そのindexと同じ値をとるインデックスをすべてキューに加えてBFSを行う
    """
    diff: list[int] = []
    prev_A = 0
    for i in range(N):
        A = A_lst[i]
        diff.append(A - prev_A)
        prev_A = A
    BFS(diff)


def BFS(diff: list[int]):
    que: deque[list[int]] = deque()
    que.append(diff)
    while len(que) > 0:
        diff = que.popleft()
        while len(diff) > K + 1:
            min_idx = 0
            for i in range(1, len(diff) - 1):
                if diff[i] + diff[i + 1] < diff[min_idx] + diff[min_idx + 1]:
                    min_idx = i
            for i in range(len(diff) - 1):
                if diff[i] + diff[i - 1] == diff[min_idx] + diff[min_idx + 1]:
                    que.append(diff[:min_idx] + [diff[min_idx] + diff[min_idx + 1]] + diff[min_idx + 2 :])
    print(min(diff))


main()
