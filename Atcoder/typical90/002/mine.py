from sys import stdin

readline = stdin.readline


def DFS(line: str, l_cnt: int, r_cnt: int):
    if l_cnt >= 0 and r_cnt >= 0:
        if l_cnt == r_cnt == 0:
            print(line)
        elif l_cnt <= r_cnt:
            DFS(line + "(", l_cnt - 1, r_cnt)
            DFS(line + ")", l_cnt, r_cnt - 1)
        else:
            return


def main():
    N = int(readline().rstrip())
    if N % 2 == 1:
        return
    n = int(N / 2)
    DFS("(", n - 1, n)


main()
