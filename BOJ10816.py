import sys
import bisect
input = sys.stdin.readline

N = int(input())
cards = sorted(list(map(int,input().split())))
M = int(input())
matching = list(map(int,input().split()))

for i in range(M):
    l = bisect.bisect_left(cards,matching[i])
    r = bisect.bisect_right(cards,matching[i])
    print(r-l, end=' ')
