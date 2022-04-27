import sys

"""
1.vが最大になるような選び方のうち，rが最大になる選び方
2.rが最大になるような選び方のうち，vが最大になる選び方
1., 2. の選び方で重複があれば，それを取り除く
"""


def main(lines: list[str]):
    # input
    N, W = map(int, lines[0].split())
    w_lst: list[int] = []
    v_lst: list[int] = []
    r_lst: list[int] = []
    for line in lines:
        w, v, r = map(int, line.split())
        w_lst.append(w)
        v_lst.append(v)
        r_lst.append(r)
    dp4v = DP(N, W, w_lst, v_lst)
    routes4v = []
    restore(dp4v, v_lst, N, len(dp4v[0]) - 1, routes4v)
    dp4r = DP(N, W, w_lst, r_lst)
    routes4r = []
    restore(dp4r, r_lst, N, len(dp4r[0]) - 1, routes4r)


def DP(N: int, W: int, w_lst: list[int], v_lst: list[int]) -> list[list[int]]:
    """
    価値（または報酬）を最大にする荷物の取り方のリスト: [[1,2,3,4(荷物のナンバー)], [1,3,5]]

    dp[i][j] := i 番目までの荷物を取捨選択し価値が j となったとき，最小の重み
    dp[i][j] = min(dp[i-1][j-v_lst[i-1]] + w_lst[i-1], dp[i-1][j])
    """
    INF = 1 << 10
    V = sum(v_lst)
    dp: list[list[int]] = [[INF] * V for _ in range(N + 1)]
    dp[0][0] = 0
    for i in range(1, N + 1):
        for j in range(V):
            if j >= v_lst[i - 1]:
                dp[i][j] = min(dp[i - 1][j - v_lst[i - 1]] + w_lst[i - 1], dp[i - 1][j])
            else:
                dp[i][j] = dp[i - 1][j]

    # 総重量が W 以下のうち最大の価値を求める
    max_v = 0
    for j in reversed(range(V)):
        if dp[N][j] <= W:
            max_v = j
            break
    return dp[:][: max_v + 1]


def restore(
    dp: list[list[int]],
    v_lst: list[int],
    i: int,
    j: int,
    routes: list[list[int]],
    route: list[int] = [],
):
    # スタートに戻った
    if i == 0 and j == 0:
        routes.append(route)
    # 荷物iを追加しなかったとき
    if dp[i - 1][j] != 0:
        restore(dp, v_lst, i - 1, j, routes, route[:])
    # 荷物iを追加したとき
    if j >= v_lst[i - 1] and dp[i - 1][j - v_lst[i - 1]]:
        route.append(i)
        restore(dp, v_lst, i - 1, j - v_lst[i - 1], routes, route[:])


def restore(
    dp: list[list[int]],
    v_lst: list[int],
    i: int,
    j: int,
    routes: list[set[int]],
    route: tuple[int] = tuple(),
):
    # スタートに戻った
    if i == 0 and j == 0:
        routes.append(route)
    # 荷物iを追加しなかったとき
    if dp[i - 1][j] != 0:
        restore(dp, v_lst, i - 1, j, routes, route[:])
    # 荷物iを追加したとき
    if j >= v_lst[i - 1] and dp[i - 1][j - v_lst[i - 1]]:
        restore(dp, v_lst, i - 1, j - v_lst[i - 1], routes, route + (i,))


if __name__ == "__main__":
    lines: list[str] = []
    for l in sys.stdin:
        lines.append(l.rstrip("\r\n"))
    main(lines)
