from sys import stdin

readline = stdin.readline

N = int(readline().rstrip())
S = " " + readline().rstrip()
atcoder = " atcoder"
table = [[0] * (N + 1) for _ in range(len(atcoder))]
table[0] = [1] * (N + 1)

for i in range(1, len(atcoder)):
    for j in range(1, N + 1):
        if S[j] == atcoder[i]:
            table[i][j] = (table[i - 1][j - 1] + table[i][j - 1]) % 1000000007
        else:
            table[i][j] = table[i][j - 1]

print(table[len(atcoder) - 1][N])
