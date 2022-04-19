from sys import stdin
import heapq

input = stdin.readline


def main():
    N, L, P = map(int, input().rstrip().split())
    A = list(map(int, input().rstrip().split()))
    B = list(map(int, input().rstrip().split()))

    q: list[int] = []

    # ans: 補給回数, pos: 今いる場所, tank: タンクのガソリンの量
