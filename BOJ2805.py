import sys
input = sys.stdin.readline
N,M = map(int, input().split()) #나무의 수
trees = list(map(int, input().split()))
low = 0
high = max(trees)
answer = 0

while low < high:
    mid = (low + high) // 2
    s = sum(max(0, tree - mid) for tree in trees)

    if s >= M:
        answer = mid
        low = mid+1
    else:
        high = mid

print(answer)
