import sys

input = sys.stdin.readline
N, L = map(int,input().split())
leak_point = sorted(map(int,input().split()))
pre = leak_point[0]
cnt = 1
for i in range(1,N):
    if pre+L > leak_point[i]:
        continue
    pre = leak_point[i]
    cnt += 1

print(cnt)