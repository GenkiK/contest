from sys import stdin

# from queue import LifoQueue as Stack

input = stdin.readline

H, W = map(int, input().rstrip().split())
Q = int(input().rstrip())

field = [[0] * W for _ in range(H)]
S: list[list[int]] = []


def dfs(goal: list[int]):
    while len(S) != 0:
        pos = S[-1]
        if pos == goal:
            print("Yes")
            S.clear()
            return
        x, y = pos
        for npos in [[x + 1, y], [x - 1, y], [x, y + 1], [x, y - 1]]:
            if 0 <= npos[0] <= W - 1 and 0 <= npos[1] <= H - 1 and field[npos[0]][npos[1]] == 1:
                S.append(npos)
    print("No")
    return


for _ in range(Q):
    q = list(map(int, input().rstrip().split()))
    if q[0] == 1:
        field[q[1] - 1][q[2] - 1] = 1
    elif field[q[1] - 1][q[2] - 1] == 1 and field[q[3] - 1][q[4] - 1] == 1:
        S.append([q[1] - 1, q[2] - 1])
        dfs([q[3] - 1, q[4] - 1])
    else:
        print("No")


# S: Stack[list[int]] = Stack()


# def dfs(goal: list[int]):
#     while not S.empty():
#         pos = S.get()
#         if pos == goal:
#             print("Yes")
#             S.task_done()
#             return
#         x, y = pos
#         for npos in [[x + 1, y], [x - 1, y], [x, y + 1], [x, y - 1]]:
#             if 0 <= npos[0] <= W - 1 and 0 <= npos[1] <= H - 1 and field[npos[0]][npos[1]] == 1:
#                 S.put(npos)
#     print("No")
#     return


# for _ in range(Q):
#     q = list(map(int, input().rstrip().split()))
#     if q[0] == 1:
#         field[q[1] - 1][q[2] - 1] = 1
#     elif field[q[1] - 1][q[2] - 1] == 1 and field[q[3] - 1][q[4] - 1] == 1:
#         S.put([q[1] - 1, q[2] - 1])
#         dfs([q[3] - 1, q[4] - 1])
#     else:
#         print("No")
