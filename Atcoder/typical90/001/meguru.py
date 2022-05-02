from __future__ import annotations

N, L = map(int, input().rstrip().split())
K = int(input())
A = list(map(int, input().rstrip().split()))

"""
keyword: 答えで二分探索
・「最小値の最大化」という形式の問題では有効
・「答えがMとなるように最小値を選べるか」と考えていく
"""


def is_ok(M: int):
    cnt = 0
    pre = 0
    for i in range(N):
        if A[i] - pre >= M and L - A[i] >= M:  # 今見ているピース長さがM以上かつここまでで切ったピースの余りの長さがM以上
            cnt += 1
            pre = A[i]
    if cnt >= K:
        return True
    return False


def main():
    # めぐる式二分探索
    # left: 条件を満たす領域の最大値
    # right: 条件を満たさない領域の最小値
    left = 1
    right = L + 1
    while right - left > 1:
        mid = left + (right - left) // 2
        if is_ok(mid):
            left = mid
        else:
            right = mid
    print(left)


"""
めぐる式二分探索のお気持ち．

・条件を満たす最小値を求めるとき
leftは条件を満たさない最大の値（or index）
rightは条件を満たす最小の値（or index）
leftより左は条件を満たさないことがわかっている．rightより右は条件を満たすことがわかっている．leftとrightの間はわからない．この間を埋めていき，最終的に right - left == 1 つまり間がなくなることを目標とする

・条件を満たす最大値を求めるとき
leftは条件を満たす領域の最大値（or index）
rightは条件を満たさない領域の最小値（or index）

上記のパターンで異なるのは，leftが条件を満たす領域にはいっているかどうか．
"""
