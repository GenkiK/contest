from sys import stdin

readline = stdin.readline

H, W = map(int, readline().rstrip().split())
field = [readline().rstrip().split() for _ in range(H)]

# 再帰的にdfs
def dfs(x: int, y: int) -> None:
    field[x][y] = "."
    # 移動する8方向をループする
    for dx in range(-1, 2):
        for dy in range(-1, 2):
            nx = x + dx
            ny = y + dy
            if 0 <= nx < H and 0 <= ny < W and field[nx][ny] == "W":
                dfs(nx, ny)
    return


total_num = 0
for x in range(H):
    for y in range(W):
        elem = field[x][y]
        if elem == "W":
            dfs(x, y)
            total_num += 1
print(total_num)

"""
memo:
    DFS(深さ優先探索)では、(暗に)スタックを用いている
"""
