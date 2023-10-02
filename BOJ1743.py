import sys
from collections import deque

dy = (1, -1, 0, 0)
dx = (0, 0, 1, -1)

input = sys.stdin.readline
N, M, K = map(int,input().split())

table = [[False] * M for _ in range(N)]
idx = []
chk = {}
for _ in range(K):
    i,j = map(int,input().split())
    i,j = i-1,j-1
    table[i][j] = True
    chk[(i,j)] = False
    idx.append((i,j))

result = 0
for i in range(len(idx)):
    if chk[idx[i]] == True:
        continue
    else:
        sz = 1
        chk[idx[i]] = True
        dq = deque()
        dq.append(idx[i])
        while dq:
            y,x = dq.popleft()
            for k in range(4):
                ny, nx = y +dy[k], x+dx[k]
                if (ny,nx) in idx and chk[(ny,nx)] == False:
                    sz += 1
                    if result < sz:
                        result = sz
                    chk[(ny,nx)] = True
                    dq.append((ny,nx))

print(result)