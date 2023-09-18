import sys
from collections import deque

N = int(input())
cards = [i+1 for i in range(N)]
deq = deque(cards)
while not len(deq) == 1:
    deq.popleft()
    deq.append(deq.popleft())

print(deq[0])