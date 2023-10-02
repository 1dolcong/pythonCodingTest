import sys
from collections import deque
import copy

dy = (1,0,-1,0)
dx = (0,1,0,-1)
input = sys.stdin.readline
R,C = map(int, input().split())
board = [input().rstrip() for _ in range(R)]
dq = deque()
dq.append((0,0,1, [board[0][0]]))

result = 1
while dq:
    for i in range(4):
        y, x, distance, alpa = dq[0]
        y, x, distance = y + dy[i], x + dx[i], distance+1
        alpa = alpa[:]
        if 0<=y<R and 0<=x<C and not board[y][x] in alpa:
            if result < distance:
                result = distance
            alpa.append(board[y][x])
            dq.append((y,x,distance,alpa))
    dq.popleft()
print(result)