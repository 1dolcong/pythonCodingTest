import sys
from collections import deque

input = sys.stdin.readline
N, M = map(int, input().split())

dx = (1, -1, 0, 0)
dy = (0, 0, 1, -1)

def is_valid(y, x, route):
    if 0 <= y < N and 0 <= x < M and route[y][x] == '1':
        return True
    else:
        return False

route = [input().rstrip() for i in range(N)]
chk = [[False] * M for _ in range(N)]
queue = deque()
queue.append((0, 0, 1))
chk[0][0] = True
found = False
while queue and not found:
    y, x, cnt = queue.popleft()
    for i in range(4):
        new_x = x + dx[i]
        new_y = y + dy[i]
        new_cnt = cnt + 1
        if is_valid(new_y, new_x, route) and not chk[new_y][new_x]:
            if (new_y, new_x) == (N-1, M-1):
                chk[new_y][new_x] = True
                print(new_cnt)
                found = True
                break
            chk[new_y][new_x] = True
            queue.append((new_y, new_x, new_cnt))
