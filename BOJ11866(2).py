from collections import deque

N,K = map(int, input().split())
num = [ _ for _ in range(1,N+1)]
deq = deque(num)
ans = []

while deq:
    deq.rotate(-1 * (K-1))
    ans.append(deq.popleft())
print('<', end='')
for _ in range(len(ans)):
    if not _ == len(ans)-1:
        print(ans[_], end=', ')
    else:
        print(ans[_], end='>')
