from itertools import combinations as c

N, K = map(int, input().split())

"""
全文字列を見ていき，Kコの文字列に含まれる文字記号を探す
"""

S_lst = [input() for _ in range(N)]
lst = [i for i in range(N)]

ans = 0
for i in range(1, N + 1):
    combs_iter = c(lst, i)
    for comb_tuple in combs_iter:
        tmp_ans = 0
        dct = {
            k: 0
            for k in [
                "a",
                "b",
                "c",
                "d",
                "e",
                "f",
                "g",
                "h",
                "i",
                "j",
                "k",
                "l",
                "m",
                "n",
                "o",
                "p",
                "q",
                "r",
                "s",
                "t",
                "u",
                "v",
                "w",
                "x",
                "y",
                "z",
            ]
        }
        tmp_S_lst: list[str] = []
        comb_lst = list(comb_tuple)
        for S_num in comb_lst:
            for char in S_lst[S_num]:
                dct[char] += 1
        for v in dct.values():
            if v == K:
                tmp_ans += 1
        if tmp_ans > ans:
            ans = tmp_ans
print(ans)
