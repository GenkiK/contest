from sys import stdin

input = stdin.readline

P, Q = map(int, input().rstrip().split())
A = list(map(int, input().rstrip().split()))

"""
dp[i][j] := 囚人iから囚人jまでの部分になったとき，その中の囚人すべてを解放するのに必要なコインの最小枚数
dp[0]はフェイク(Aに格納された囚人indexが1-originなので，それに合わせるため)
"""

