from sys import stdin

input = stdin.readline

s = list(map(int, list(input().rstrip())))
s.sort()

for i in range(10):
    if i != s[i]:
        print(i)
        break
