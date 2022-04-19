from sys import stdin

input = stdin.readline

N = int(input().rstrip())
As = sorted(list(map(int, input().rstrip().split())))
Q = int(input().rstrip())

for _ in range(Q):
    B = int(input().rstrip())
    min_diff = float("inf")
    has_printed = False
    for A in As:
        diff = abs(A - B)
        if min_diff <= diff:
            print(min_diff)
            has_printed = True
            break
        min_diff = diff
    if not has_printed:
        print(min_diff)
