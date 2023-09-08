from collections import deque
import sys

dx = (0, 0, -1, 1)
dy = (1, -1, 0, 0)

input = sys.stdin.readline
R,C = map(int, input().split())
board = [input().strip() for _ in range(R)]
chk = [[set() for _ in range(C)] for _ in range(R)] #set으로 중복 제거
ans = 0

def is_correct(y,x):
    return 0 <= y < R and 0 <= x < C

dq = deque()
chk[0][0].add(board[0][0])
dq.append((0,0,board[0][0]))

while dq:
    y, x, s = dq.popleft() #지나온길
    ans = max(ans, len(s))
    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]
        if is_correct(ny, nx) and board[ny][nx] not in s:
            ns = s + board[ny][nx]
            if ns not in chk[ny][nx]:
                chk[ny][nx].add(ns)
                dq.append((ny,nx,ns))
print(ans)




