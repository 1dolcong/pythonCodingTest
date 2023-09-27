import sys

input = sys.stdin.readline
N = int(input())
timeTable = [tuple(map(int,input().split())) for _ in range(N)]
sTimeTable = sorted(timeTable, key=lambda x:x[1])
cnt = 0
idx = 0
while idx < N:
    end = sTimeTable[idx][1]
    while idx + 1 < N and sTimeTable[idx+1][0] < end:
        idx = idx + 1
    cnt += 1
    idx += 1

print(cnt)

