import sys
from collections import deque
input = sys.stdin.readline
for _ in range(int(input())):
    keys = input().rstrip()
    lq = deque()
    rq = deque()
    for key in keys:
        if key == '<':
            if lq:
                rq.appendleft(lq.pop())
        elif key == '>':
            if rq:
                lq.append(rq.popleft())
        elif key == '-':
            if lq:
                lq.pop()
        else: # 일반 키
            lq.append(key)
    print("".join(lq)+"".join(rq))
    


