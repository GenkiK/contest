from sys import stdin

input = stdin.readline

N = int(input().rstrip())
s = input().rstrip()

# =================== 自分の解答 ===================
def select_start(start: int, end: int) -> bool:
    if s[start] < s[end]:
        return True
    elif s[start] > s[end] or start >= end:
        return False
    else:
        return select_start(start + 1, end - 1)


t = ""
while len(s) > 1:
    if select_start(0, len(s) - 1):
        t += s[0]
        s = s[1:]
    else:
        t += s[-1]
        s = s[:-1]
print(t + s)


# =================== 解答(ほぼ同じ) ===================

a = 0
b = N - 1
while a <= b:
    left = False
    for i in range(0, b - a + 1):
        if s[a + i] < s[b - i]:
            left = True
            break
        elif s[a + i] > s[b - i]:
            break
    if left:
        print(s[a], end="")
        a += 1
    else:
        print(s[b], end="")
        b -= 1
print("")
