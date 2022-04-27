N, K = map(int, input().split())

S_lst = [input() for _ in range(N)]

# Sの選び方につけた番号
bit = 0
ans = 0
while bit < (1 << N):  # 0 ~ 2**(N-1)回繰り返す（パターン数）
    alphabets_cnts = [0] * 26
    for i in range(N):
        if bit & (1 << i):  # 選ばれた文字列のとき
            for j in range(len(S_lst[i])):
                alphabets_cnts[ord(S_lst[i][j]) - ord("a")] += 1
    tmp_ans = len([cnt for cnt in alphabets_cnts if cnt == K])
    if tmp_ans > ans:
        ans = tmp_ans
    bit += 1
print(ans)
