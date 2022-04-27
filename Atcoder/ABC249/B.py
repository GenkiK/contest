import re

S = input()

"""
大文字カウンタ・小文字カウンタを作り，あとはinでサーチする
もしくはソートすれば同じ文字が連続するはず
"""

sorted_S = sorted(list(S))

def main():
    if not re.search(r"[a-z]", S):
        print("No")
        return
    if not re.search(r"[A-Z]", S):
        print("No")
        return
    pre_char = sorted_S[0]
    for char in sorted_S[1:]:
        if pre_char == char:
            print("No")
            return
        pre_char = char
    print("Yes")


main()
