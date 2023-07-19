from collections import deque

cards = deque([_ for _ in range(int(input()),0,-1)])
while len(cards) > 1:
    cards.pop()
    cards.appendleft(cards.pop())

print(cards[0])

