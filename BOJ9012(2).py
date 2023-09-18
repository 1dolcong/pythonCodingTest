from collections import deque
import sys

input = sys.stdin.readline
N = int(input())
for _ in range(N):
    s = input().rstrip()
    stk = deque()
    is_VPS = True

    for i in range(len(s)):
        if s[i] == '(':
            stk.append(s[i])
        else:
            if stk:
                stk.pop()
            else:
                is_VPS = False
    if is_VPS and not stk:
        print("YES")
    else:
        print("NO")