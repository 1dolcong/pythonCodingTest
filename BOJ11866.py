import sys

input = sys.stdin.readline()
N, K = map(int, input.split())
circle = list(range(1,N+1))
result = []
idx = 0
while(circle):
    idx = (idx+(K-1))%len(circle)
    result.append(circle[idx])
    circle.pop(idx)

print(f"<{', '.join(map(str,result))}>")