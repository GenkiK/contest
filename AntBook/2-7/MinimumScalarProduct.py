from sys import stdin

input = stdin.readline

n = int(input())

v1 = list(map(int, input().rstrip().split()))
v2 = list(map(int, input().rstrip().split()))

v1.sort()
v2.sort(reverse=True)

total = 0
for i in range(n):
    total += v1[i] * v2[i]
print(total)
