from sys import stdin

input = stdin.readline

N = int(input().rstrip())

"""
どういったものから優先的に選んでいけばよいのか
* 隙間なく埋め込む？報酬の高いやつから貪欲？
* N <= 8なら全探索で行ける
    * 全探索の場合は、貪欲法で金額が最大になるように仕事をとり、それが条件を満たす(スケジューリングできる)かを調べていく
"""