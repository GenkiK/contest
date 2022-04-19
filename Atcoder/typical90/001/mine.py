from sys import stdin
import copy

readline = stdin.readline

N, L = map(int, readline().rstrip().split())
K = int(readline().rstrip())
array = list(map(int, readline().rstrip().split()))

"""
差をとって、全ての線で切ったときの各棒の長さを得る。

まず最小の棒とその両隣のうち小さいほうを取り出して、それらを組み合わせて１つの棒にする
棒の個数がK+1となるまでこれを繰り返す

最小値が複数ある場合には、そのうちの next + min_valが最小となる組をconcatする
"""

logs = [array[0]]
pre_elem = array[0]
for elem in array[1:]:
    logs.append(elem - pre_elem)
    pre_elem = elem
logs.append(L - array[-1])

logs_cp = copy.copy(logs)

while len(logs) > K + 1:
    min_val = min(logs)

    min_idxs = []
    for i, log in enumerate(logs):
        if log == min_val:
            min_idxs.append(i)

    min_idx = 0
    next_idx = 0
    next_min_val = 1000000000
    for tmp_min_idx in min_idxs:
        tmp_next_idx = 0
        # 左端
        if tmp_min_idx == 0:
            tmp_next_idx = tmp_min_idx + 1
        # 右端
        elif tmp_min_idx == len(logs) - 1:
            tmp_next_idx = tmp_min_idx - 1
        else:
            if logs[tmp_min_idx + 1] < logs[tmp_min_idx - 1]:
                tmp_next_idx = tmp_min_idx + 1
            else:
                tmp_next_idx = tmp_min_idx - 1
        # next_min_valが最小となるmin_idxを探す
        if logs[tmp_next_idx] < next_min_val:
            next_min_val = logs[tmp_next_idx]
            next_idx = tmp_next_idx
            min_idx = tmp_min_idx

    logs[min_idx] = min_val + logs[next_idx]
    del logs[next_idx]

print(min(logs))
