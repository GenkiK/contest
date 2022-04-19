from sys import stdin

readline = stdin.readline

A_str, B_str = readline().strip().split()
A_str_lst = list(A_str)
B_str_lst = list(B_str)

is_hard = False
for a, b in zip(reversed(A_str_lst), reversed(B_str_lst)):
    a = int(a)
    b = int(b)
    if a + b >= 10:
        print("Hard")
        is_hard = True
        break
if not is_hard:
    print("Easy")
