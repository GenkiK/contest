from sys import stdin
from math import acos, pi


def angle(l_pos: list[int], m_pos: list[int], r_pos: list[int]):
    v1 = [l_pos[0] - m_pos[0], l_pos[1] - m_pos[1]]
    v2 = [r_pos[0] - m_pos[0], r_pos[1] - m_pos[1]]
    cos_theta = (v1[0] * v2[0] + v1[1] * v2[1]) / (
        (v1[0] ** 2 + v1[1] ** 2) ** 0.5 * (v2[0] ** 2 + v2[1] ** 2) ** 0.5
    )
    return acos(cos_theta) * 180 / pi


readline = stdin.readline

N = int(readline().rstrip())

field = [list(map(int, readline().rstrip().split())) for _ in range(N)]

field_sorted_x = sorted(sorted(field, key=lambda x: x[1]), key=lambda x: x[0])
field_sorted_y = sorted(sorted(field, key=lambda x: x[0]), key=lambda x: x[1])

min_width_x = float("inf")
min_idx_x = 0
min_width_y = float("inf")
min_idx_y = 0
for i in range(N - 3):
    width_x = max([pos[0] for pos in field_sorted_x[i : i + 3]]) - min(
        [pos[0] for pos in field_sorted_x[i : i + 3]]
    )
    width_y = max([pos[1] for pos in field_sorted_y[i : i + 3]]) - min(
        [pos[1] for pos in field_sorted_y[i : i + 3]]
    )
    if width_x < min_width_x:
        min_width_x = width_x
        min_idx_x = i
    if width_y < min_width_y:
        min_width_y = width_y
        min_idx_y = i

field_sorted = []
is_x = True
if min_width_x < min_width_y:
    field_sorted = field_sorted_x[min_idx_x : min_idx_x + 3]
else:
    field_sorted = field_sorted_y[min_idx_y : min_idx_y + 3]
    is_x = False

# xの幅が小さいならば、y方向に長い
bottom_pos = min(field_sorted, key=lambda x: x[int(is_x)])
top_pos = max(field_sorted, key=lambda x: x[int(is_x)])
middle_pos = []
for pos in field_sorted:
    if pos != bottom_pos and pos != top_pos:
        middle_pos = pos

print(angle(top_pos, middle_pos, bottom_pos))
