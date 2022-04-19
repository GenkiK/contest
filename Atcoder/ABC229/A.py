from sys import stdin

readline = stdin.readline

s1 = list(readline().rstrip())
s2 = list(readline().rstrip())
s1_bits = [1 if elem == "#" else 0 for elem in s1]
s2_bits = [1 if elem == "#" else 0 for elem in s2]

lst = [sum(s1_bits), sum(s2_bits), s1_bits[0] + s2_bits[0], s1_bits[1] + s2_bits[1]]
if 2 in lst:
    print("Yes")
else:
    print("No")
