from sys import stdin

readline = stdin.readline

H, W = map(int, readline().rstrip().split())
matrix = []
row_sum = []
col_sum = []
for _ in range(H):
    new_row = list(map(int, readline().rstrip().split()))
    matrix.append(new_row)
    row_sum.append(sum(new_row))

for j in range(W):
    col_sum.append(sum([col[j] for col in matrix]))

for i in range(H):
    for j in range(W):
        if j != W - 1:
            print(row_sum[i] + col_sum[j] - matrix[i][j], end=" ")
        else:
            print(row_sum[i] + col_sum[j] - matrix[i][j], end="\n")
