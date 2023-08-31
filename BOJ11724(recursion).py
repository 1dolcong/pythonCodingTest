import sys

sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline
N,M = map(int, input().split())
adj = [[False] *(N) for _ in range(N)]
for _ in range(M):
    a,b = map(int, input().split())
    adj[a - 1][b - 1] = True
    adj[b - 1][a - 1] = True
ans = 0
chk = [False] * N

def dfs(i):
    for j in range(N):
        if adj[i][j] and not chk[j]:
            chk[j] = True
            dfs(j)
for i in range(N):
    if not chk[i]:
        ans += 1
        chk[i] =True
        dfs(i)

print(ans)