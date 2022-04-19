from sys import stdin

input = stdin.readline
N, M = map(int, input().rstrip().split())
"""
同じ値が3回出てくるとNo
循環するとNo
A<B という条件は大切

Aをkeyとして昇順に並び替えると、3回出てきたやつがわかりやすい？
"""

is_passed = [False] * N
graph_dct: dict[int, list[int]] = {}


def main():
    # グラフの作成
    A, B = 0, 0
    for _ in range(M):
        A, B = map(int, input().rstrip().split())
        if graph_dct.get(A):
            if len(graph_dct[A]) == 2:
                print("No")
                return
            graph_dct[A].append(B)
        else:
            graph_dct[A] = [B]
        if graph_dct.get(B):
            if len(graph_dct[B]) == 2:
                print("No")
                return
            graph_dct[B].append(A)
        else:
            graph_dct[B] = [A]

    for v in graph_dct.keys():
        if is_passed[v] == False:
            isCyclic = dfs(v, -1)
            if isCyclic:
                print("No")
                return
    print("Yes")
    return


def dfs(cur: int, prev: int):
    is_passed[cur] = True
    for next in graph_dct[cur]:
        if next == prev:
            # 前のノードに戻る場合
            continue
        if is_passed[next]:
            # 次に通るノードが過去に通ったことがある
            return True
        dfs(next, cur)
    return False


main()
