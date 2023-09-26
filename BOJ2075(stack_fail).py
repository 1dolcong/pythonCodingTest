import sys
from collections import deque
input = sys.stdin.readline
N = int(input())
Stacktable = [deque(maxlen=1500) for _ in range(N)]
for i in range(N):
    temp = input().rstrip().split()
    for _ in range(N):
        Stacktable[_].append(temp[_])

count = 0
ans = 0
while count != N:
    maxIdx = 0
    maxValue = Stacktable[0][-1]
    for i in range(N):
        if maxValue < Stacktable[i][-1]:
            maxValue = Stacktable[i][-1]
            maxIdx = i
    ans = maxValue
    Stacktable[maxIdx].pop()
    count += 1
print(ans)