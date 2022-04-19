"""
前から単純に小さいものから順に探していくと、見つけた文字以降でK文字確保できないかもしれない
0~N-Kまでのの範囲での最小値を導く
文字列を対応するintに変換した配列がいる
"""
from sys import stdin

readline = stdin.readline

N, K = map(int, readline().rstrip().split())
S_origin: list[str] = list(readline().rstrip())
alphabet = list("abcdefghijklmnopqrstuvwxyz")
alphabet_dict = {k: v for v, k in enumerate(alphabet)}
S: list[int] = [alphabet_dict[k] for k in S_origin]

res = ""
begin = 0
end = N - K
while len(res) < K:
    min_idx = S[begin : end + 1].index(min(S[begin : end + 1])) + begin
    res += S_origin[min_idx]
    begin = min_idx + 1
    end = end + 1 if end < N - 1 else end
print(res)
