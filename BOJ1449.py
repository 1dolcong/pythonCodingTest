import sys
input = sys.stdin.readline
N, L = tuple(map(int,input().split()))
leak_point = list(map(int,input().split()))

cnt = 1
point = leak_point[0] + L-1
for i in range(1, len(leak_point)):
    if leak_point[i] <= point:
        continue
    else:
        point = leak_point[i] + L-1
        cnt += 1
print(cnt)
