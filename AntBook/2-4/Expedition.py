from sys import stdin

input = stdin.readline


"""
燃料の残りはPであらわす
(A_i - 前回停車した点のA) + B_i が i で止まったときの進める距離
進める範囲内でこの価値が最大になるように点を取っていく
"""


def main():
    N, L, P = map(int, input().rstrip().split())
    A_lst = list(map(int, input().rstrip().split()))
    B_lst = list(map(int, input().rstrip().split()))

    loc = -1
    next_loc = 0
    cnt = 0
    while L > 0:
        idx = loc + 1
        max_dist = -1
        while P >= A_lst[idx] - (A_lst[loc] if loc >= 0 else 0):
            if max_dist < A_lst[idx] + B_lst[idx]:
                max_dist = A_lst[idx] + B_lst[idx]
                next_loc = idx
            idx += 1
            if idx >= N:
                # 全ての点で止まってもたどり着けなかった場合
                return -1
        if max_dist < 0:
            # 次のガソリンスタンドまでたどり着けなかった場合
            return -1
        else:
            cnt += 1
            P = P - (A_lst[next_loc] - (A_lst[loc] if loc >= 0 else 0)) + B_lst[next_loc]
            loc = next_loc
            L -= A_lst[next_loc]
    return cnt


print(main())
