from collections import deque
import sys

input = sys.stdin.readline
N,M = map(int, input().split()) # N y좌표, M 좌표
table = [ input().rstrip() for _ in range(N)]

dy = (1, 0, -1, 0)
dx = (0, 1, 0, -1)

def vaild(i, j, table, chk):
    global N,M
    if 0 <= i < N and 0<= j < M and chk[i][j] == False and table[i][j] == '1':
        return True
    return False

dq = deque()
chk = [[False] * M for _ in range(N)]
chk[0][0] = True
dq.append((0,0,1)) #y,x, 거리

while dq:
    for i in range(4):
        y, x = dq[0][0] + dy[i], dq[0][1] + dx[i]
        distance = dq[0][2]
        if vaild(y,x, table, chk):
            if y == N - 1 and x == M - 1:
                print(distance + 1)
                while dq:
                    dq.popleft()
                break
            chk[y][x] = True
            dq.append((y,x, distance + 1))
    if dq:
        dq.popleft()