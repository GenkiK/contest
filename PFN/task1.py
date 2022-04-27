import sys


def main(lines: list[str]):
    N, X = map(int, lines[0].split())
    cnt = 0
    for i in reversed(range(N)):
        cnt += X >> i
        X = X & ((1 << i) - 1)
    print(cnt)


lines = ["4 14"]
main(lines)

# import sys

# def main(lines):
#     # このコードは標準入力と標準出力を用いたサンプルコードです。
#     # このコードは好きなように編集・削除してもらって構いません。
#     # ---
#     # This is a sample code to use stdin and stdout.
#     # Edit and remove this code as you like.

#     for i, v in enumerate(lines):
#         print("line[{0}]: {1}".format(i, v))

# if __name__ == '__main__':
#     lines = []
#     for l in sys.stdin:
#         lines.append(l.rstrip('\r\n'))
#     main(lines)
