import sys

input = sys.stdin.readline
N = int(input())
timeTable = [tuple(map(int,input().split())) for _ in range(N)]
timeTable = sorted(timeTable, key=lambda x:(x[1],x[0]))
cnt = 1
end = timeTable[0][1]
for i in range(1, N):
    if end <= timeTable[i][0]:
        cnt += 1
        end = timeTable[i][1]

print(cnt)

