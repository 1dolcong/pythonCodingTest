import heapq, sys
num = int(input())
pq = []
inputList = []
for i in range(num):
    temp = int(sys.stdin.readline().rstrip())
    inputList.append(temp)
    if not temp == 0:
        heapq.heappush(pq, (abs(temp),temp))
        print(pq)
    else:
        if len(pq) > 0:
            print(heapq.heappop(pq)[1])
        else:
            print("0")