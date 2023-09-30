from collections import deque
import sys

def everyVisit(check, N):
    ret = False
    for i in range(N):
        if check[i] == False:
            ret = True
            break
    return ret


input = sys.stdin.readline
N, M = map(int,input().split())
Ajtable = [[False] * N for _ in range(N)]
for i in range(M):
    a,b = map(int,input().split())
    a= a-1
    b= b-1
    Ajtable[a][b] = True
    Ajtable[b][a] = True

result = 0
check = [False] * N
while(everyVisit(check,N)):
    dq = deque()
    for i in range(N):
        if check[i] == False:
            check[i] = True
            dq.append(i)
            break

    while(dq):
        for i in range(N):
            if check[i] != True and Ajtable[dq[0]][i] == True:
                check[i] = True
                dq.append(i)
        dq.popleft()
    result += 1
print(result)