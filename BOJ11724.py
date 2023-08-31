import sys
from collections import deque

def isChk():
    for i in range(N):
        if chk[i] == False:
            return i
    return -1

input = sys.stdin.readline
N, M = tuple(map(int, input().split()))
matrix = [[False] * N for _ in range(N)]  # Corrected initialization
chk = [False] * N
for i in range(M):
    s, e = tuple(map(int, input().split()))
    matrix[s - 1][e - 1] = True
    matrix[e - 1][s - 1] = True
cnt = 0
stack = deque()
while True:
    start_node = isChk()
    if start_node == -1:
        break

    stack.append(start_node)
    chk[start_node] = True

    while stack:
        top = stack[-1]
        found = False

        for i in range(N):
            if matrix[top][i] and not chk[i]:
                stack.append(i)
                chk[i] = True
                found = True
                break

        if not found:
            stack.pop()

    cnt += 1

print(cnt)