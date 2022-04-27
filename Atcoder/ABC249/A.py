A, B, C, D, E, F, X = map(int, input().split())

"""
X秒間の間に，走る休むのセットを何セット繰り返すか := X // (A + C) と X // (D + F)
余った秒数 X % (A + C) がAより短いならその分だけ走れる．Aより長いならAだけ走れる
"""

t_set_num = X // (A + C)
a_set_num = X // (D + F)

t_rest = X % (A + C) if X % (A + C) <= A else A
a_rest = X % (D + F) if X % (D + F) <= D else D

t_len = t_set_num * A * B + t_rest * B
a_len = a_set_num * D * E + a_rest * E

if t_len < a_len:
    print("Aoki")
elif t_len > a_len:
    print("Takahashi")
else:
    print("Draw")
