import sys
input = sys.stdin.readline
time_list = [tuple(map(int,input().split())) for _ in range(int(input()))]

time_list.sort(key = lambda x: (x[1], x[0]))
cnt = 1
end_time = time_list[0][1]
for start,end in time_list:
     if start >= end_time:
          cnt += 1
          end_time = end
print(cnt)